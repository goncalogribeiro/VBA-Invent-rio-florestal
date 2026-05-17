from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ObservacaoEcofisiologica:
    identificador: str
    dap_cm: float
    altura_m: float
    lai: float
    npp: float
    indice_competicao: float
    crescimento_observado: float


class ErroMLEcofisiologico(Exception):
    pass



def estimar_crescimento_ml(
    observacao: ObservacaoEcofisiologica,
) -> float:
    """
    Primeira camada simplificada de aprendizado ecofisiológico.

    Estrutura propositalmente auditável.
    """

    crescimento = (
        (observacao.dap_cm * 0.02)
        + (observacao.altura_m * 0.01)
        + (observacao.lai * 0.5)
        + (observacao.npp * 0.03)
    )

    penalizacao = (
        observacao.indice_competicao * 0.05
    )

    return max(0.0, crescimento - penalizacao)



def erro_prognose(
    observado: float,
    previsto: float,
) -> float:
    """
    Erro absoluto simplificado.
    """

    return abs(observado - previsto)



def analisar_aprendizado_ecofisiologico(
    observacao: ObservacaoEcofisiologica,
) -> dict[str, float]:
    """
    Primeira camada de aprendizado adaptativo.

    Futuramente:
    - random forest;
    - xgboost;
    - deep learning;
    - aprendizado temporal;
    - IA adaptativa.
    """

    previsto = estimar_crescimento_ml(
        observacao
    )

    erro = erro_prognose(
        observacao.crescimento_observado,
        previsto,
    )

    return {
        "crescimento_previsto": float(previsto),
        "erro_prognose": float(erro),
    }
