from __future__ import annotations

from dataclasses import dataclass


ORDEM_PRIORIDADE_QUALIDADE = [
    "copa_quebrada",
    "bifurcacao_baixa",
    "macaco_prego",
    "torta",
    "bifurcacao_alta",
]


@dataclass(frozen=True)
class ArvoreQualitativa:
    """Representacao simplificada de arvore para selecao qualitativa."""

    id_arvore: str
    qualidade: str
    dap: float
    area_basal: float
    volume: float


class ErroSelecaoQualitativa(Exception):
    pass



def ordenar_para_remocao(
    arvores: list[ArvoreQualitativa],
) -> list[ArvoreQualitativa]:
    """
    Ordena arvores da pior para melhor qualidade.

    Esta primeira implementacao utiliza apenas prioridade qualitativa.
    """

    prioridade = {
        nome: indice
        for indice, nome in enumerate(
            ORDEM_PRIORIDADE_QUALIDADE
        )
    }

    return sorted(
        arvores,
        key=lambda arv: prioridade.get(arv.qualidade, 999),
    )



def selecionar_por_percentual_arvores(
    arvores: list[ArvoreQualitativa],
    intensidade: float,
) -> list[ArvoreQualitativa]:
    """
    Seleciona arvores para remocao por percentual de N.
    """

    if intensidade <= 0 or intensidade >= 1:
        raise ErroSelecaoQualitativa(
            "Intensidade deve estar entre 0 e 1."
        )

    ordenadas = ordenar_para_remocao(arvores)

    quantidade = int(len(ordenadas) * intensidade)

    return ordenadas[:quantidade]
