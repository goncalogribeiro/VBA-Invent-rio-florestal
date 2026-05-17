from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.manejo.quality_selection import ArvoreQualitativa


@dataclass(frozen=True)
class ResultadoCrescimento:
    idade_inicial: int
    idade_final: int
    incremento_dap_medio_cm: float
    incremento_altura_medio_m: float
    fator_compensacao_desbaste: float
    n_arvores: int


class ErroPrognoseCrescimento(Exception):
    pass



def calcular_fator_compensacao(
    intensidade_g_real: float,
) -> float:
    """
    Calcula fator simplificado de crescimento compensatório.

    Primeira aproximação conservadora.
    """

    if intensidade_g_real <= 0:
        return 1.0

    if intensidade_g_real <= 0.20:
        return 1.03

    if intensidade_g_real <= 0.35:
        return 1.08

    if intensidade_g_real <= 0.50:
        return 1.15

    return 1.20



def projetar_crescimento_um_ciclo(
    arvores: list[ArvoreQualitativa],
    idade_atual: int,
    anos_projetados: int,
    incremento_dap_base_cm_ano: float,
    incremento_altura_base_m_ano: float,
    intensidade_g_real: float,
) -> ResultadoCrescimento:
    """
    Primeira camada de crescimento temporal.

    Futuramente:
    - competição;
    - ICA;
    - mortalidade;
    - sítio;
    - crescimento individual.
    """

    if anos_projetados <= 0:
        raise ErroPrognoseCrescimento(
            "Anos projetados deve ser maior que zero."
        )

    fator = calcular_fator_compensacao(intensidade_g_real)

    incremento_dap = (
        incremento_dap_base_cm_ano
        * fator
        * anos_projetados
    )

    incremento_h = (
        incremento_altura_base_m_ano
        * fator
        * anos_projetados
    )

    return ResultadoCrescimento(
        idade_inicial=idade_atual,
        idade_final=idade_atual + anos_projetados,
        incremento_dap_medio_cm=float(incremento_dap),
        incremento_altura_medio_m=float(incremento_h),
        fator_compensacao_desbaste=float(fator),
        n_arvores=len(arvores),
    )
