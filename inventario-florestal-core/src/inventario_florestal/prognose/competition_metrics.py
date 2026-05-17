from __future__ import annotations

from dataclasses import dataclass
from math import log10, sqrt


@dataclass(frozen=True)
class ResultadoCompeticao:
    densidade_reineke_percentual: float
    hart_becking_percentual: float
    zona_reineke: str
    zona_hart_becking: str


class ErroCompeticao(Exception):
    pass



def calcular_reineke_percentual(
    n_arvores_ha: float,
    dap_medio_cm: float,
    constante_a: float = 120000,
) -> float:
    """
    Calcula percentual relativo da densidade máxima de Reineke.

    Primeira implementação simplificada.
    """

    if n_arvores_ha <= 0 or dap_medio_cm <= 0:
        raise ErroCompeticao(
            "N e DAP devem ser maiores que zero."
        )

    n_max = 10 ** (
        log10(constante_a)
        - 1.605 * log10(dap_medio_cm)
    )

    return (n_arvores_ha / n_max) * 100



def classificar_reineke(percentual: float) -> str:
    if percentual > 45:
        return "pre_desbaste"

    if percentual >= 25:
        return "manejo_ideal"

    return "baixa_densidade"



def calcular_hart_becking(
    n_arvores_ha: float,
    altura_dominante_m: float,
) -> float:
    """
    Calcula índice de Hart-Becking.
    """

    if n_arvores_ha <= 0 or altura_dominante_m <= 0:
        raise ErroCompeticao(
            "N e altura dominante devem ser maiores que zero."
        )

    espacamento_medio = sqrt(10000 / n_arvores_ha)

    return (
        espacamento_medio
        / altura_dominante_m
    ) * 100



def classificar_hart_becking(percentual: float) -> str:
    if percentual < 20:
        return "superlotacao"

    if percentual <= 35:
        return "manejo_adequado"

    return "baixa_ocupacao"



def calcular_metricas_competicao(
    n_arvores_ha: float,
    dap_medio_cm: float,
    altura_dominante_m: float,
) -> ResultadoCompeticao:
    """
    Calcula métricas estruturais de competição.
    """

    reineke = calcular_reineke_percentual(
        n_arvores_ha=n_arvores_ha,
        dap_medio_cm=dap_medio_cm,
    )

    hart = calcular_hart_becking(
        n_arvores_ha=n_arvores_ha,
        altura_dominante_m=altura_dominante_m,
    )

    return ResultadoCompeticao(
        densidade_reineke_percentual=float(reineke),
        hart_becking_percentual=float(hart),
        zona_reineke=classificar_reineke(reineke),
        zona_hart_becking=classificar_hart_becking(hart),
    )
