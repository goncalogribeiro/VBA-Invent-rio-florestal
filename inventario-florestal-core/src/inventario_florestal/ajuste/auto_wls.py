"""Pipeline automatico OLS -> diagnostico -> WLS.

Este modulo implementa uma primeira camada de Auto-WLS para modelos
biometricos lineares.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from inventario_florestal.ajuste.linear_regression import ajustar_ols
from inventario_florestal.ajuste.weighted_regression import ajustar_wls
from inventario_florestal.ajuste.weights import gerar_pesos_wls
from inventario_florestal.ranking.residual_analysis import diagnosticar_residuos


@dataclass(frozen=True)
class ResultadoAutoWLS:
    """Resultado comparativo entre OLS e WLS."""

    ols: object
    diagnostico_ols: object
    pesos_wls: object | None
    wls: object | None
    diagnostico_wls: object | None
    heterocedasticidade_detectada: bool
    estrategia_pesos: str | None
    modelo_recomendado: str



def executar_auto_wls(
    dados: pd.DataFrame,
    variavel_dependente: str,
    variaveis_independentes: list[str],
    estrategia_pesos: str = "inverso_estimado_quadrado",
    intercepto: bool = True,
) -> ResultadoAutoWLS:
    """Executa pipeline automatico de comparacao OLS x WLS.

    Fluxo:

    1. ajusta OLS;
    2. executa diagnostico residual;
    3. detecta heterocedasticidade;
    4. gera pesos automaticamente;
    5. executa WLS;
    6. compara OLS e WLS.
    """

    resultado_ols = ajustar_ols(
        dados=dados,
        variavel_dependente=variavel_dependente,
        variaveis_independentes=variaveis_independentes,
        intercepto=intercepto,
    )

    diagnostico_ols = diagnosticar_residuos(
        observado=resultado_ols.observado,
        estimado=resultado_ols.estimado,
        matriz_x=resultado_ols.matriz_x,
    )

    hetero = bool(diagnostico_ols.heterocedasticidade_detectada)

    if not hetero:
        return ResultadoAutoWLS(
            ols=resultado_ols,
            diagnostico_ols=diagnostico_ols,
            pesos_wls=None,
            wls=None,
            diagnostico_wls=None,
            heterocedasticidade_detectada=False,
            estrategia_pesos=None,
            modelo_recomendado="OLS",
        )

    pesos = gerar_pesos_wls(
        estrategia=estrategia_pesos,
        estimado=resultado_ols.estimado,
        residuos=resultado_ols.residuos,
    )

    resultado_wls = ajustar_wls(
        dados=dados,
        variavel_dependente=variavel_dependente,
        variaveis_independentes=variaveis_independentes,
        pesos=pesos,
        intercepto=intercepto,
    )

    diagnostico_wls = diagnosticar_residuos(
        observado=resultado_wls.observado,
        estimado=resultado_wls.estimado,
        matriz_x=resultado_wls.matriz_x,
    )

    syx_ols = resultado_ols.metricas["syx_percentual"]
    syx_wls = resultado_wls.metricas["syx_percentual"]

    if syx_wls < syx_ols:
        recomendado = "WLS"
    else:
        recomendado = "OLS"

    return ResultadoAutoWLS(
        ols=resultado_ols,
        diagnostico_ols=diagnostico_ols,
        pesos_wls=pesos,
        wls=resultado_wls,
        diagnostico_wls=diagnostico_wls,
        heterocedasticidade_detectada=True,
        estrategia_pesos=estrategia_pesos,
        modelo_recomendado=recomendado,
    )
