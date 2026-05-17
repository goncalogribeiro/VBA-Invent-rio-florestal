"""Analise residual para modelos biometricos.

A avaliacao residual e uma etapa obrigatoria em biometria florestal, pois
modelos com bom R² podem apresentar vies sistematico, heterocedasticidade ou
comportamento inadequado em faixas especificas de DAP, altura ou volume.
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



def press_aproximado(
    observado: np.ndarray,
    estimado: np.ndarray,
) -> float:
    """Calcula PRESS aproximado sem matriz de alavancagem.

    Esta versao inicial usa a soma de quadrados dos residuos como aproximação.
    Futuramente sera substituida pela formula com leverage:

    PRESS = soma[(e_i / (1 - h_ii))²]
    """

    residuos = np.asarray(observado, dtype=float) - np.asarray(estimado, dtype=float)

    return float(np.sum(residuos**2))



def diagnosticar_residuos(
    observado: np.ndarray,
    estimado: np.ndarray,
) -> DiagnosticoResidual:
    """Gera diagnostico residual inicial."""

    observado = np.asarray(observado, dtype=float)
    estimado = np.asarray(estimado, dtype=float)

    residuos = observado - estimado
    resid_perc = residuos_percentuais(observado, estimado)
    resid_pad = residuos_padronizados(observado, estimado)
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
    )
