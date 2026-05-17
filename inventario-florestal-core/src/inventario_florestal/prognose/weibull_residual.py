from __future__ import annotations

from dataclasses import dataclass
from statistics import mean

from inventario_florestal.manejo.quality_selection import ArvoreQualitativa


@dataclass(frozen=True)
class EstruturaResidual:
    n: int
    dap_medio: float
    dap_minimo: float
    dap_maximo: float
    area_basal_total: float
    volume_total: float



def calcular_estrutura_residual(
    arvores: list[ArvoreQualitativa],
) -> EstruturaResidual:
    """
    Calcula estrutura residual pós-desbaste.

    Esta camada será utilizada futuramente para:

    - recalibração Weibull;
    - prognose diamétrica;
    - ICA;
    - mortalidade;
    - crescimento compensatório.
    """

    if not arvores:
        return EstruturaResidual(
            n=0,
            dap_medio=0.0,
            dap_minimo=0.0,
            dap_maximo=0.0,
            area_basal_total=0.0,
            volume_total=0.0,
        )

    daps = [arv.dap for arv in arvores]

    return EstruturaResidual(
        n=len(arvores),
        dap_medio=float(mean(daps)),
        dap_minimo=float(min(daps)),
        dap_maximo=float(max(daps)),
        area_basal_total=float(
            sum(arv.area_basal for arv in arvores)
        ),
        volume_total=float(
            sum(arv.volume for arv in arvores)
        ),
    )
