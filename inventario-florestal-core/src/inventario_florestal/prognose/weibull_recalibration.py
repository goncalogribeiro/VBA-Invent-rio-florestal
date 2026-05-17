from __future__ import annotations

from dataclasses import dataclass
from math import gamma
from statistics import mean

from inventario_florestal.manejo.quality_selection import ArvoreQualitativa


@dataclass(frozen=True)
class WeibullResidualParameters:
    shape_c: float
    scale_b: float
    location_a: float
    dap_medio: float
    dap_minimo: float
    dap_maximo: float
    n: int


class ErroWeibullResidual(Exception):
    pass



def estimar_weibull_momentos(
    daps: list[float],
) -> WeibullResidualParameters:
    """
    Primeira aproximação Weibull residual.

    Implementação inicial simplificada via momentos.

    Futuramente:
    - MLE iterativo completo;
    - PRM;
    - PPM;
    - KS;
    - Anderson-Darling.
    """

    if len(daps) < 3:
        raise ErroWeibullResidual(
            "Necessário mínimo de 3 DAPs para Weibull residual."
        )

    dmin = min(daps)
    dmax = max(daps)
    dmed = mean(daps)

    # aproximação inicial conservadora
    shape_c = 3.0

    scale_b = dmed / gamma(1 + (1 / shape_c))

    return WeibullResidualParameters(
        shape_c=float(shape_c),
        scale_b=float(scale_b),
        location_a=float(dmin),
        dap_medio=float(dmed),
        dap_minimo=float(dmin),
        dap_maximo=float(dmax),
        n=len(daps),
    )



def recalibrar_weibull_residual(
    arvores_remanescentes: list[ArvoreQualitativa],
) -> WeibullResidualParameters:
    """
    Recalibra Weibull residual pós-desbaste.
    """

    daps = [
        arvore.dap
        for arvore in arvores_remanescentes
    ]

    return estimar_weibull_momentos(daps)
