"""Motor inicial de regressao nao linear.

A regressao nao linear exige maior controle numerico que OLS/WLS. Por isso,
a primeira versao deste modulo exige uma funcao Python explicita, chutes
iniciais e, opcionalmente, limites para os parametros.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
from scipy.optimize import curve_fit

from inventario_florestal.ranking.metrics import (
    bias,
    mae,
    r2,
    r2_ajustado,
    rmse,
    syx,
    syx_percentual,
)
from inventario_florestal.ranking.residual_analysis import diagnosticar_residuos


FuncaoNaoLinear = Callable[..., np.ndarray]


@dataclass(frozen=True)
class ResultadoRegressaoNaoLinear:
    """Resultado padronizado de regressao nao linear."""

    parametros: dict[str, float]
    matriz_covariancia: np.ndarray | None
    estimado: np.ndarray
    observado: np.ndarray
    residuos: np.ndarray
    metricas: dict[str, float]
    diagnostico_residual: object
    convergiu: bool
    mensagem: str | None
    n: int
    n_parametros: int


class ErroRegressaoNaoLinear(Exception):
    """Erro relacionado ao ajuste nao linear."""



def ajustar_nls(
    funcao: FuncaoNaoLinear,
    x: np.ndarray,
    y: np.ndarray,
    nomes_parametros: list[str],
    chute_inicial: list[float],
    limites: tuple[list[float], list[float]] | None = None,
    max_iteracoes: int = 10000,
) -> ResultadoRegressaoNaoLinear:
    """Ajusta regressao nao linear por minimos quadrados.

    Parameters
    ----------
    funcao:
        Funcao no formato `f(x, *params)`.
    x:
        Matriz ou vetor de variaveis independentes.
    y:
        Vetor observado.
    nomes_parametros:
        Nomes dos parametros ajustados.
    chute_inicial:
        Valores iniciais dos parametros.
    limites:
        Tupla com limites inferiores e superiores.
    max_iteracoes:
        Numero maximo de avaliacoes da funcao.
    """

    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)

    if len(nomes_parametros) != len(chute_inicial):
        raise ErroRegressaoNaoLinear(
            "nomes_parametros e chute_inicial devem ter o mesmo tamanho."
        )

    try:
        if limites is None:
            parametros, cov = curve_fit(
                funcao,
                x_arr,
                y_arr,
                p0=chute_inicial,
                maxfev=max_iteracoes,
            )
        else:
            parametros, cov = curve_fit(
                funcao,
                x_arr,
                y_arr,
                p0=chute_inicial,
                bounds=limites,
                maxfev=max_iteracoes,
            )

        convergiu = True
        mensagem = None

    except Exception as exc:
        raise ErroRegressaoNaoLinear(str(exc)) from exc

    estimado = np.asarray(funcao(x_arr, *parametros), dtype=float)
    residuos = y_arr - estimado
    n_parametros = len(parametros)

    metricas = {
        "r2": r2(y_arr, estimado),
        "r2_ajustado": r2_ajustado(y_arr, estimado, n_parametros),
        "syx": syx(y_arr, estimado, n_parametros),
        "syx_percentual": syx_percentual(y_arr, estimado, n_parametros),
        "rmse": rmse(y_arr, estimado),
        "mae": mae(y_arr, estimado),
        "bias": bias(y_arr, estimado),
    }

    diagnostico = diagnosticar_residuos(
        observado=y_arr,
        estimado=estimado,
        matriz_x=None,
    )

    return ResultadoRegressaoNaoLinear(
        parametros={
            nome: float(valor)
            for nome, valor in zip(nomes_parametros, parametros, strict=True)
        },
        matriz_covariancia=cov,
        estimado=estimado,
        observado=y_arr,
        residuos=residuos,
        metricas=metricas,
        diagnostico_residual=diagnostico,
        convergiu=convergiu,
        mensagem=mensagem,
        n=int(len(y_arr)),
        n_parametros=n_parametros,
    )
