from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from statistics import variance

from inventario_florestal.manejo.quality_selection import (
    ArvoreQualitativa,
)


@dataclass(frozen=True)
class EstatisticasDiametricas:
    dap_medio: float
    dap_minimo: float
    dap_maximo: float
    variancia: float
    n: int


class ErroWeibullPosDesbaste(Exception):
    pass



def calcular_estatisticas_diametricas(
    arvores_remanescentes: list[ArvoreQualitativa],
) -> EstatisticasDiametricas:
    """
    Calcula estatísticas básicas da estrutura residual.
    """

    if not arvores_remanescentes:
        raise ErroWeibullPosDesbaste(
            "Nenhuma árvore remanescente disponível."
        )

    daps = [
        arv.dap
        for arv in arvores_remanescentes
    ]

    if len(daps) < 2:
        raise ErroWeibullPosDesbaste(
            "Quantidade insuficiente de árvores para Weibull residual."
        )

    return EstatisticasDiametricas(
        dap_medio=float(mean(daps)),
        dap_minimo=float(min(daps)),
        dap_maximo=float(max(daps)),
        variancia=float(variance(daps)),
        n=len(daps),
    )
