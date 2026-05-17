"""Motor inicial de regressao linear para modelos biometricos.

Este modulo implementa ajuste OLS com statsmodels, retornando uma estrutura
padronizada para uso posterior no motor universal de ranking.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm

from inventario_florestal.ranking.metrics import (
    bias,
    mae,
    r2,
    r2_ajustado,
    rmse,
    syx,
    syx_percentual,
)


@dataclass(frozen=True)
class ResultadoRegressaoLinear:
    """Resultado padronizado de uma regressao linear."""

    coeficientes: dict[str, float]
    estimado: np.ndarray
    observado: np.ndarray
    residuos: np.ndarray
    metricas: dict[str, float]
    aic: float
    bic: float
    n: int
    n_parametros: int


def ajustar_ols(
    dados: pd.DataFrame,
    variavel_dependente: str,
    variaveis_independentes: list[str],
    intercepto: bool = True,
) -> ResultadoRegressaoLinear:
    """Ajusta uma regressao linear por minimos quadrados ordinarios.

    Parameters
    ----------
    dados:
        DataFrame contendo a variavel dependente e as independentes.
    variavel_dependente:
        Nome da coluna da variavel resposta.
    variaveis_independentes:
        Lista de colunas explicativas.
    intercepto:
        Define se o modelo deve incluir intercepto.

    Returns
    -------
    ResultadoRegressaoLinear
        Resultado padronizado do ajuste.
    """

    colunas = [variavel_dependente, *variaveis_independentes]
    dados_validos = dados[colunas].dropna().copy()

    if dados_validos.empty:
        raise ValueError("Nao ha dados validos para ajuste OLS.")

    y = dados_validos[variavel_dependente].astype(float)
    x = dados_validos[variaveis_independentes].astype(float)

    if intercepto:
        x = sm.add_constant(x, has_constant="add")

    modelo = sm.OLS(y, x).fit()

    observado = y.to_numpy(dtype=float)
    estimado = modelo.predict(x).to_numpy(dtype=float)
    residuos = observado - estimado

    n_parametros = int(len(modelo.params))

    metricas = {
        "r2": r2(observado, estimado),
        "r2_ajustado": r2_ajustado(observado, estimado, n_parametros),
        "syx": syx(observado, estimado, n_parametros),
        "syx_percentual": syx_percentual(observado, estimado, n_parametros),
        "rmse": rmse(observado, estimado),
        "mae": mae(observado, estimado),
        "bias": bias(observado, estimado),
    }

    return ResultadoRegressaoLinear(
        coeficientes={str(k): float(v) for k, v in modelo.params.items()},
        estimado=estimado,
        observado=observado,
        residuos=residuos,
        metricas=metricas,
        aic=float(modelo.aic),
        bic=float(modelo.bic),
        n=int(len(observado)),
        n_parametros=n_parametros,
    )
