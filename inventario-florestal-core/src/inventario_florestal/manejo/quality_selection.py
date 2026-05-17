from __future__ import annotations

from dataclasses import dataclass


QUALIDADE_CODIGOS = {
    1: "boa",
    2: "torta",
    3: "bifurcacao_baixa",
    4: "bifurcacao_alta",
    5: "falha",
    6: "dupla",
    7: "final_de_linha",
    8: "macaco_prego",
    9: "morta",
    10: "copa_quebrada",
}


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
    codigo_qualidade: int
    dap: float
    area_basal: float
    volume: float

    @property
    def qualidade(self) -> str:
        return QUALIDADE_CODIGOS.get(
            self.codigo_qualidade,
            "desconhecida",
        )


class ErroSelecaoQualitativa(Exception):
    pass



def ordenar_para_remocao(
    arvores: list[ArvoreQualitativa],
) -> list[ArvoreQualitativa]:
    """
    Ordena arvores da pior para melhor qualidade.

    Utiliza prioridade qualitativa operacional.
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
