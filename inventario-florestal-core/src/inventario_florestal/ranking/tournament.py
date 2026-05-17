"""Torneio universal de modelos biometricos.

O torneio executa modelos lineares, linearizados e nao lineares registrados no
catalogo, retornando ranking unico por grupo biometrico.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from inventario_florestal.ajuste.fit_from_model import (
    ErroAjusteModelo,
    ResultadoAjusteModelo,
    ajustar_modelo_linear_catalogo,
)
from inventario_florestal.ajuste.fit_nonlinear_from_model import (
    ErroExecucaoModeloNaoLinear,
    ajustar_modelo_nao_linear,
)
from inventario_florestal.ajuste.nonlinear_regression import (
    ErroRegressaoNaoLinear,
)
from inventario_florestal.modelos.schema import CatalogoModelos, GrupoModelo
from inventario_florestal.ranking.ranking_engine import (
    calcular_pontuacao_padrao,
    combinar_metricas_com_diagnostico,
)


@dataclass(frozen=True)
class ItemRankingModelo:
    """Item individual do ranking de modelos."""

    posicao: int
    modelo_id: str
    nome_modelo: str
    grupo: str
    pontuacao: float
    metricas: dict[str, float]
    aic: float | None
    bic: float | None
    ajuste: Any | None = None
    erro: str | None = None


@dataclass(frozen=True)
class ResultadoTorneioModelos:
    """Resultado completo de um torneio biometrico."""

    grupo: str
    ranking: list[ItemRankingModelo] = field(default_factory=list)
    modelos_com_erro: list[ItemRankingModelo] = field(default_factory=list)

    @property
    def vencedor(self) -> ItemRankingModelo | None:
        """Retorna o primeiro colocado do ranking."""
        if not self.ranking:
            return None
        return self.ranking[0]



def _criar_item_erro(modelo, mensagem: str) -> ItemRankingModelo:
    return ItemRankingModelo(
        posicao=0,
        modelo_id=modelo.id,
        nome_modelo=modelo.nome,
        grupo=modelo.grupo,
        pontuacao=float("-inf"),
        metricas={},
        aic=None,
        bic=None,
        ajuste=None,
        erro=mensagem,
    )



def _ordenar_ranking(itens_validos: list[ItemRankingModelo]) -> list[ItemRankingModelo]:
    itens_ordenados = sorted(
        itens_validos,
        key=lambda item: item.pontuacao,
        reverse=True,
    )

    return [
        ItemRankingModelo(
            posicao=idx,
            modelo_id=item.modelo_id,
            nome_modelo=item.nome_modelo,
            grupo=item.grupo,
            pontuacao=item.pontuacao,
            metricas=item.metricas,
            aic=item.aic,
            bic=item.bic,
            ajuste=item.ajuste,
            erro=item.erro,
        )
        for idx, item in enumerate(itens_ordenados, start=1)
    ]



def executar_torneio(
    catalogo: CatalogoModelos,
    dados: pd.DataFrame,
    grupo: GrupoModelo,
    incluir_experimentais: bool = True,
) -> ResultadoTorneioModelos:
    """Executa torneio entre modelos suportados de um grupo biometrico."""

    modelos = catalogo.filtrar_por_grupo(grupo)

    itens_validos: list[ItemRankingModelo] = []
    itens_erro: list[ItemRankingModelo] = []

    for modelo in modelos:
        if modelo.status_validacao == "experimental" and not incluir_experimentais:
            itens_erro.append(
                _criar_item_erro(
                    modelo,
                    "Modelo experimental ignorado por configuracao do torneio.",
                )
            )
            continue

        try:
            if modelo.tipo_regressao in {"linear", "linear_sem_intercepto"}:
                ajuste: ResultadoAjusteModelo = ajustar_modelo_linear_catalogo(
                    modelo,
                    dados,
                )

                metricas_base = (
                    ajuste.metricas_escala_original
                    if ajuste.metricas_escala_original is not None
                    else ajuste.resultado_linear.metricas
                )

                metricas = combinar_metricas_com_diagnostico(
                    metricas=metricas_base,
                    diagnostico=ajuste.diagnostico_residual,
                )

                aic = ajuste.resultado_linear.aic
                bic = ajuste.resultado_linear.bic

            elif modelo.tipo_regressao == "nao_linear":
                ajuste = ajustar_modelo_nao_linear(modelo, dados)

                metricas = combinar_metricas_com_diagnostico(
                    metricas=ajuste.metricas,
                    diagnostico=ajuste.diagnostico_residual,
                )

                aic = None
                bic = None

            else:
                itens_erro.append(
                    _criar_item_erro(
                        modelo,
                        f"Tipo de regressao ainda nao suportado: {modelo.tipo_regressao}",
                    )
                )
                continue

            pontuacao = calcular_pontuacao_padrao(metricas)

            itens_validos.append(
                ItemRankingModelo(
                    posicao=0,
                    modelo_id=modelo.id,
                    nome_modelo=modelo.nome,
                    grupo=modelo.grupo,
                    pontuacao=pontuacao,
                    metricas=metricas,
                    aic=aic,
                    bic=bic,
                    ajuste=ajuste,
                    erro=None,
                )
            )

        except (
            ErroAjusteModelo,
            ErroExecucaoModeloNaoLinear,
            ErroRegressaoNaoLinear,
            ValueError,
            KeyError,
        ) as exc:
            itens_erro.append(_criar_item_erro(modelo, str(exc)))

    return ResultadoTorneioModelos(
        grupo=grupo,
        ranking=_ordenar_ranking(itens_validos),
        modelos_com_erro=itens_erro,
    )



def executar_torneio_linear(
    catalogo: CatalogoModelos,
    dados: pd.DataFrame,
    grupo: GrupoModelo,
) -> ResultadoTorneioModelos:
    """Compatibilidade: executa torneio apenas com modelos lineares."""

    modelos_originais = catalogo.modelos
    catalogo_linear = CatalogoModelos(
        metadata=catalogo.metadata,
        modelos=[
            modelo
            for modelo in modelos_originais
            if modelo.tipo_regressao in {"linear", "linear_sem_intercepto"}
        ],
    )

    return executar_torneio(
        catalogo=catalogo_linear,
        dados=dados,
        grupo=grupo,
    )
