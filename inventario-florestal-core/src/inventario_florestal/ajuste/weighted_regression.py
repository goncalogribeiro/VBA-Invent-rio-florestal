"""Motor inicial de regressao ponderada WLS.

A regressao ponderada deve ser usada quando ha evidencias de
heterocedasticidade. A versao inicial aceita pesos explicitamente fornecidos
ou uma coluna de pesos no DataFrame.
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
class ResultadoRegressaoPonderada:
    """Resultado padronizado de regressao WLS."""

    coeficientes: dict[str, float]
    estimado: np.ndarray
    observado: np.ndarray
    residuos: np.ndarray
    pesos: np.ndarray
    metricas: dict[str, float]
    aic: float
    bic: float
    n: int
    n_parametros: int
    matriz_x: np.ndarray
    nomes_variaveis_x: list[str]


class ErroRegressaoPonderada(Exception):
    """Erro relacionado ao ajuste WLS."""



def ajustar_wls(
    dados: pd.DataFrame,
    variavel_dependente: str,
    variaveis_independentes: list[str],
    pesos: np.ndarray | None = None,
    coluna_pesos: str | None = None,
    intercepto: bool = True,
) -> ResultadoRegressaoPonderada:
    """Ajusta regressao por minimos quadrados ponderados.

    Parameters
    ----------
    dados:
        DataFrame com variavel dependente, independentes e opcionalmente pesos.
    variavel_dependente:
        Nome da variavel resposta.
    variaveis_independentes:
        Variaveis explicativas.
    pesos:
        Vetor externo de pesos.
    coluna_pesos:
        Nome da coluna com pesos.
    intercepto:
        Define se o modelo inclui intercepto.
    """

    if pesos is not None and coluna_pesos is not None:
        raise ErroRegressaoPonderada(
            "Informe pesos ou coluna_pesos, nao ambos."
        )

    colunas = [variavel_dependente, *variaveis_independentes]

    if coluna_pesos is not None:
        colunas.append(coluna_pesos)

    dados_validos = dados[colunas].dropna().copy()

    if dados_validos.empty:
        raise ErroRegressaoPonderada("Nao ha dados validos para ajuste WLS.")

    y = dados_validos[variavel_dependente].astype(float)
    x = dados_validos[variaveis_independentes].astype(float)

    if intercepto:
        x = sm.add_constant(x, has_constant="add")

    if coluna_pesos is not None:
        w = dados_validos[coluna_pesos].astype(float).to_numpy()
    elif pesos is not None:
        w = np.asarray(pesos, dtype=float)
        if len(w) != len(dados_validos):
            raise ErroRegressaoPonderada(
                "O vetor de pesos deve ter o mesmo tamanho dos dados validos."
            )
    else:
        raise ErroRegressaoPonderada(
            "WLS requer pesos explicitos ou coluna_pesos."
        )

    if np.any(w <= 0):
        raise ErroRegressaoPonderada("Todos os pesos WLS devem ser positivos.")

    modelo = sm.WLS(y, x, weights=w).fit()

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

    return ResultadoRegressaoPonderada(
        coeficientes={str(k): float(v) for k, v in modelo.params.items()},
        estimado=estimado,
        observado=observado,
        residuos=residuos,
        pesos=w,
        metricas=metricas,
        aic=float(modelo.aic),
        bic=float(modelo.bic),
        n=int(len(observado)),
        n_parametros=n_parametros,
        matriz_x=x.to_numpy(dtype=float),
        nomes_variaveis_x=[str(coluna) for coluna in x.columns],
    )
