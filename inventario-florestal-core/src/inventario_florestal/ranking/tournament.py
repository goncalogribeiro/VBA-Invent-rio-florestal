"""Torneio universal de modelos biometricos.

Versao inicial limitada a modelos lineares e linearizados. Modelos nao lineares
serao incorporados posteriormente, apos estabilizacao do pipeline linear.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from inventario_florestal.ajuste.fit_from_model import (
    ErroAjusteModelo,
    ResultadoAjusteModelo,
    ajustar_modelo_linear_catalogo,
)
from inventario_florestal.modelos.schema import CatalogoModelos, GrupoModelo
from inventario_florestal.ranking.ranking_engine import calcular_pontuacao_padrao


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
    ajuste: ResultadoAjusteModelo | None = None
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



def executar_torneio_linear(
    catalogo: CatalogoModelos,
    dados: pd.DataFrame,
    grupo: GrupoModelo,
) -> ResultadoTorneioModelos:
    """Executa torneio entre modelos lineares/linearizados de um grupo.

    Parameters
    ----------
    catalogo:
        Catalogo validado de modelos biometricos.
    dados:
        Dados observados.
    grupo:
        Grupo biometrico a ser avaliado.
    """

    modelos = catalogo.filtrar_por_grupo(grupo)

    itens_validos: list[ItemRankingModelo] = []
    itens_erro: list[ItemRankingModelo] = []

    for modelo in modelos:
        if modelo.tipo_regressao not in {"linear", "linear_sem_intercepto"}:
            itens_erro.append(
                ItemRankingModelo(
                    posicao=0,
                    modelo_id=modelo.id,
                    nome_modelo=modelo.nome,
                    grupo=modelo.grupo,
                    pontuacao=float("-inf"),
                    metricas={},
                    aic=None,
                    bic=None,
                    ajuste=None,
                    erro="Modelo nao linear ignorado nesta fase do torneio.",
                )
            )
            continue

        try:
            ajuste = ajustar_modelo_linear_catalogo(modelo, dados)

            metricas = (
                ajuste.metricas_escala_original
                if ajuste.metricas_escala_original is not None
                else ajuste.resultado_linear.metricas
            )

            pontuacao = calcular_pontuacao_padrao(metricas)

            itens_validos.append(
                ItemRankingModelo(
                    posicao=0,
                    modelo_id=modelo.id,
                    nome_modelo=modelo.nome,
                    grupo=modelo.grupo,
                    pontuacao=pontuacao,
                    metricas=metricas,
                    aic=ajuste.resultado_linear.aic,
                    bic=ajuste.resultado_linear.bic,
                    ajuste=ajuste,
                    erro=None,
                )
            )
        except (ErroAjusteModelo, ValueError, KeyError) as exc:
            itens_erro.append(
                ItemRankingModelo(
                    posicao=0,
                    modelo_id=modelo.id,
                    nome_modelo=modelo.nome,
                    grupo=modelo.grupo,
                    pontuacao=float("-inf"),
                    metricas={},
                    aic=None,
                    bic=None,
                    ajuste=None,
                    erro=str(exc),
                )
            )

    itens_ordenados = sorted(
        itens_validos,
        key=lambda item: item.pontuacao,
        reverse=True,
    )

    ranking = [
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

    return ResultadoTorneioModelos(
        grupo=grupo,
        ranking=ranking,
        modelos_com_erro=itens_erro,
    )
