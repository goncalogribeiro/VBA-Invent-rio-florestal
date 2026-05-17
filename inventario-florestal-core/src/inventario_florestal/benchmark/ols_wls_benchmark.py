"""Benchmark comparativo OLS vs WLS.

Este modulo compara ajustes OLS e WLS com base em metricas biometricas,
diagnostico residual e estabilidade estatistica.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from inventario_florestal.ajuste.auto_wls import ResultadoAutoWLS, executar_auto_wls


@dataclass(frozen=True)
class ComparacaoOLSWLS:
    """Resumo comparativo entre OLS e WLS."""

    modelo_recomendado: str
    heterocedasticidade_detectada: bool
    estrategia_pesos: str | None
    r2_ajustado_ols: float
    syx_percentual_ols: float
    press_rmse_ols: float
    r2_ajustado_wls: float | None
    syx_percentual_wls: float | None
    press_rmse_wls: float | None
    justificativa: str
    resultado_auto_wls: ResultadoAutoWLS



def comparar_ols_wls(
    dados: pd.DataFrame,
    variavel_dependente: str,
    variaveis_independentes: list[str],
    estrategia_pesos: str = "inverso_estimado_quadrado",
    intercepto: bool = True,
) -> ComparacaoOLSWLS:
    """Executa benchmark entre OLS e WLS.

    O WLS so e executado quando o diagnostico OLS indica
    heterocedasticidade.
    """

    resultado = executar_auto_wls(
        dados=dados,
        variavel_dependente=variavel_dependente,
        variaveis_independentes=variaveis_independentes,
        estrategia_pesos=estrategia_pesos,
        intercepto=intercepto,
    )

    r2_aj_ols = resultado.ols.metricas["r2_ajustado"]
    syx_ols = resultado.ols.metricas["syx_percentual"]
    press_ols = resultado.diagnostico_ols.press_rmse

    r2_aj_wls = None
    syx_wls = None
    press_wls = None

    if resultado.wls is None or resultado.diagnostico_wls is None:
        justificativa = (
            "OLS recomendado: heterocedasticidade nao detectada pelos testes "
            "residuais implementados."
        )
    else:
        r2_aj_wls = resultado.wls.metricas["r2_ajustado"]
        syx_wls = resultado.wls.metricas["syx_percentual"]
        press_wls = resultado.diagnostico_wls.press_rmse

        if resultado.modelo_recomendado == "WLS":
            justificativa = (
                "WLS recomendado: houve heterocedasticidade detectada e o "
                "ajuste ponderado reduziu o Syx%."
            )
        else:
            justificativa = (
                "OLS mantido: embora tenha havido heterocedasticidade, o WLS "
                "nao reduziu o Syx% em relacao ao OLS."
            )

    return ComparacaoOLSWLS(
        modelo_recomendado=resultado.modelo_recomendado,
        heterocedasticidade_detectada=resultado.heterocedasticidade_detectada,
        estrategia_pesos=resultado.estrategia_pesos,
        r2_ajustado_ols=r2_aj_ols,
        syx_percentual_ols=syx_ols,
        press_rmse_ols=press_ols,
        r2_ajustado_wls=r2_aj_wls,
        syx_percentual_wls=syx_wls,
        press_rmse_wls=press_wls,
        justificativa=justificativa,
        resultado_auto_wls=resultado,
    )
