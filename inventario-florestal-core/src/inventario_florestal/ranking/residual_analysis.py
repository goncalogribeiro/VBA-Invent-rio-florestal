"""Analise residual para modelos biometricos.

A avaliacao residual e uma etapa obrigatoria em biometria florestal, pois
modelos com bom R² ajustado podem apresentar vies sistematico,
heterocedasticidade ou comportamento inadequado em faixas especificas de DAP,
altura ou volume.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


EPSILON = 1e-12


@dataclass(frozen=True)
class DiagnosticoResidual:
    """Resumo da analise residual."""

    residuos: np.ndarray
    residuos_percentuais: np.ndarray
    residuos_padronizados: np.ndarray
    press: float
    press_rmse: float
    media_residuos: float
    media_abs_residuos_percentuais: float
    max_abs_residuo_percentual: float
    leverage: np.ndarray | None = None
    max_leverage: float | None = None
    press_real: bool = False
    cook_distance: np.ndarray | None = None
    max_cook_distance: float | None = None
    n_observacoes_influentes: int | None = None



def residuos_percentuais(
    observado: np.ndarray,
    estimado: np.ndarray,
) -> np.ndarray:
    """Calcula residuos percentuais.

    A forma utilizada e:

    100 * (observado - estimado) / observado
    """

    observado = np.asarray(observado, dtype=float)
    estimado = np.asarray(estimado, dtype=float)

    return 100 * (observado - estimado) / (observado + EPSILON)



def residuos_padronizados(
    observado: np.ndarray,
    estimado: np.ndarray,
) -> np.ndarray:
    """Calcula residuos padronizados por desvio padrao amostral."""

    residuos = np.asarray(observado, dtype=float) - np.asarray(estimado, dtype=float)

    desvio = np.std(residuos, ddof=1)

    if desvio <= EPSILON:
        return np.zeros_like(residuos)

    return residuos / desvio



def calcular_leverage(matriz_x: np.ndarray) -> np.ndarray:
    """Calcula os valores de leverage da matriz de projeto.

    A diagonal da matriz hat e calculada por:

    H = X (X'X)^-1 X'

    Para estabilidade numerica, usa-se pseudo-inversa.
    """

    x = np.asarray(matriz_x, dtype=float)

    if x.ndim != 2:
        raise ValueError("A matriz X deve ser bidimensional.")

    hat = x @ np.linalg.pinv(x.T @ x) @ x.T

    return np.clip(np.diag(hat), 0.0, 1.0)



def press_com_leverage(
    observado: np.ndarray,
    estimado: np.ndarray,
    leverage: np.ndarray,
) -> float:
    """Calcula PRESS usando leverage."""

    observado = np.asarray(observado, dtype=float)
    estimado = np.asarray(estimado, dtype=float)
    leverage = np.asarray(leverage, dtype=float)

    residuos = observado - estimado

    denom = np.clip(1 - leverage, EPSILON, None)

    return float(np.sum((residuos / denom) ** 2))



def cook_distance(
    observado: np.ndarray,
    estimado: np.ndarray,
    leverage: np.ndarray,
    n_parametros: int,
) -> np.ndarray:
    """Calcula Cook Distance para cada observacao.

    Formula operacional:

    D_i = (e_i² / (p * MSE)) * [h_ii / (1 - h_ii)²]

    onde:
    - e_i = residuo da observacao i;
    - p = numero de parametros do modelo;
    - MSE = quadrado medio residual;
    - h_ii = leverage da observacao i.
    """

    observado = np.asarray(observado, dtype=float)
    estimado = np.asarray(estimado, dtype=float)
    leverage = np.asarray(leverage, dtype=float)

    residuos = observado - estimado
    n = len(residuos)
    p = max(int(n_parametros), 1)

    mse = np.sum(residuos**2) / max(n - p, 1)

    denom = p * max(mse, EPSILON)
    leverage_denom = np.clip((1 - leverage) ** 2, EPSILON, None)

    return (residuos**2 / denom) * (leverage / leverage_denom)



def press_aproximado(
    observado: np.ndarray,
    estimado: np.ndarray,
) -> float:
    """Calcula PRESS aproximado sem matriz de alavancagem."""

    residuos = np.asarray(observado, dtype=float) - np.asarray(estimado, dtype=float)

    return float(np.sum(residuos**2))



def diagnosticar_residuos(
    observado: np.ndarray,
    estimado: np.ndarray,
    matriz_x: np.ndarray | None = None,
) -> DiagnosticoResidual:
    """Gera diagnostico residual.

    Quando `matriz_x` e fornecida, calcula leverage, PRESS real e Cook
    Distance. Caso contrario, usa PRESS aproximado.
    """

    observado = np.asarray(observado, dtype=float)
    estimado = np.asarray(estimado, dtype=float)

    residuos = observado - estimado
    resid_perc = residuos_percentuais(observado, estimado)
    resid_pad = residuos_padronizados(observado, estimado)

    leverage = None
    max_leverage = None
    press_real = False
    cooks = None
    max_cook = None
    n_influentes = None

    if matriz_x is not None:
        leverage = calcular_leverage(matriz_x)
        press = press_com_leverage(observado, estimado, leverage)
        max_leverage = float(np.max(leverage))
        press_real = True

        n_parametros = matriz_x.shape[1]
        cooks = cook_distance(observado, estimado, leverage, n_parametros)
        max_cook = float(np.max(cooks))

        limite_cook = 4 / max(len(observado), 1)
        n_influentes = int(np.sum(cooks > limite_cook))
    else:
        press = press_aproximado(observado, estimado)

    return DiagnosticoResidual(
        residuos=residuos,
        residuos_percentuais=resid_perc,
        residuos_padronizados=resid_pad,
        press=press,
        press_rmse=float(np.sqrt(press / max(len(observado), 1))),
        media_residuos=float(np.mean(residuos)),
        media_abs_residuos_percentuais=float(np.mean(np.abs(resid_perc))),
        max_abs_residuo_percentual=float(np.max(np.abs(resid_perc))),
        leverage=leverage,
        max_leverage=max_leverage,
        press_real=press_real,
        cook_distance=cooks,
        max_cook_distance=max_cook,
        n_observacoes_influentes=n_influentes,
    )
