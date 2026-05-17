from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.economico.financial_engine import (
    ResultadoFinanceiro,
)
from inventario_florestal.economico.monte_carlo_engine import (
    ResultadoMonteCarlo,
)


@dataclass(frozen=True)
class RegimeManejo:
    nome: str
    idade_corte: int
    numero_desbastes: int
    intensidade_desbaste: float
    cenario_operacional: str


@dataclass(frozen=True)
class ResultadoOtimizacao:
    regime: RegimeManejo
    score: float
    vpl: float
    relacao_bc: float
    risco_negativo: float


class ErroOtimizacao(Exception):
    pass



def calcular_score_regime(
    resultado_financeiro: ResultadoFinanceiro,
    resultado_risco: ResultadoMonteCarlo,
) -> float:
    """Calcula score econômico ponderado por risco."""

    penalidade_risco = (
        resultado_risco.probabilidade_vpl_negativo / 100
    )

    score = (
        resultado_financeiro.vpl
        * resultado_financeiro.relacao_bc
        * (1 - penalidade_risco)
    )

    return float(score)



def selecionar_melhor_regime(
    candidatos: list[
        tuple[
            RegimeManejo,
            ResultadoFinanceiro,
            ResultadoMonteCarlo,
        ]
    ],
) -> ResultadoOtimizacao:
    """Seleciona o melhor regime de manejo."""

    if not candidatos:
        raise ErroOtimizacao(
            "Nenhum regime candidato informado."
        )

    melhor: ResultadoOtimizacao | None = None

    for regime, financeiro, risco in candidatos:
        score = calcular_score_regime(
            resultado_financeiro=financeiro,
            resultado_risco=risco,
        )

        atual = ResultadoOtimizacao(
            regime=regime,
            score=float(score),
            vpl=float(financeiro.vpl),
            relacao_bc=float(financeiro.relacao_bc),
            risco_negativo=float(
                risco.probabilidade_vpl_negativo
            ),
        )

        if melhor is None:
            melhor = atual
            continue

        if atual.score > melhor.score:
            melhor = atual

    return melhor
