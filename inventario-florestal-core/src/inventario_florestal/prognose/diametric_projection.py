from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.prognose.stand_projection import (
    EstadoPovoamento,
)
from inventario_florestal.weibull.weibull_distribution import (
    DistribuicaoDiametricaWeibull,
    gerar_distribuicao_weibull,
)
from inventario_florestal.weibull.weibull_prm import (
    ResultadoWeibullPRM,
    ajustar_weibull_prm,
)


@dataclass(frozen=True)
class ResultadoPrognoseDiametrica:
    estado_futuro: EstadoPovoamento
    weibull: ResultadoWeibullPRM
    distribuicao: DistribuicaoDiametricaWeibull


class ErroPrognoseDiametrica(Exception):
    pass



def prognose_diametrica_prm(
    estado_futuro: EstadoPovoamento,
    variancia_diametrica: float,
    diametro_minimo: float,
    dap_maximo_estimado: float,
    amplitude_classe: float = 2.0,
) -> ResultadoPrognoseDiametrica:
    """Executa prognose diametrica baseada em PRM Weibull."""

    weibull = ajustar_weibull_prm(
        diametro_medio=estado_futuro.dap_medio,
        variancia_diametrica=variancia_diametrica,
        diametro_minimo=diametro_minimo,
    )

    distribuicao = gerar_distribuicao_weibull(
        parametro_a=weibull.parametro_a,
        parametro_b=weibull.parametro_b,
        parametro_c=weibull.parametro_c,
        arvores_ha=estado_futuro.n_arvores_ha,
        dap_min=diametro_minimo,
        dap_max=dap_maximo_estimado,
        amplitude=amplitude_classe,
    )

    return ResultadoPrognoseDiametrica(
        estado_futuro=estado_futuro,
        weibull=weibull,
        distribuicao=distribuicao,
    )
