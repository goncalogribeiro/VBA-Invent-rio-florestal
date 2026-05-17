"""Metricas estatisticas para avaliacao de modelos biometricos."""

from __future__ import annotations

import numpy as np


EPSILON = 1e-12



def residuo(observado: np.ndarray, estimado: np.ndarray) -> np.ndarray:
    """Calcula residuos simples."""
    return observado - estimado



def bias(observado: np.ndarray, estimado: np.ndarray) -> float:
    """Calcula o vies medio."""
    return float(np.mean(residuo(observado, estimado)))



def mae(observado: np.ndarray, estimado: np.ndarray) -> float:
    """Erro medio absoluto."""
    return float(np.mean(np.abs(residuo(observado, estimado))))



def rmse(observado: np.ndarray, estimado: np.ndarray) -> float:
    """Raiz do erro quadratico medio."""
    return float(np.sqrt(np.mean((observado - estimado) ** 2)))



def syx(
    observado: np.ndarray,
    estimado: np.ndarray,
    n_parametros: int,
) -> float:
    """Erro padrao da estimativa."""

    n = len(observado)

    soma_quadrados = np.sum((observado - estimado) ** 2)

    return float(np.sqrt(soma_quadrados / max(n - n_parametros, 1)))



def syx_percentual(
    observado: np.ndarray,
    estimado: np.ndarray,
    n_parametros: int,
) -> float:
    """Erro padrao percentual."""

    media_obs = np.mean(observado)

    return float(
        (syx(observado, estimado, n_parametros) / (media_obs + EPSILON))
        * 100
    )



def r2(observado: np.ndarray, estimado: np.ndarray) -> float:
    """Coeficiente de determinacao."""

    sq_res = np.sum((observado - estimado) ** 2)
    sq_tot = np.sum((observado - np.mean(observado)) ** 2)

    return float(1 - (sq_res / (sq_tot + EPSILON)))



def r2_ajustado(
    observado: np.ndarray,
    estimado: np.ndarray,
    n_parametros: int,
) -> float:
    """Coeficiente de determinacao ajustado."""

    n = len(observado)
    r2_valor = r2(observado, estimado)

    return float(
        1 - ((1 - r2_valor) * (n - 1) / max((n - n_parametros - 1), 1))
    )
