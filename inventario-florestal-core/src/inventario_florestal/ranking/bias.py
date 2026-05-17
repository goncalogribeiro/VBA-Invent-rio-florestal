"""Correcoes de vies para modelos biometricos transformados.

Modelos ajustados em escala logaritmica precisam de cuidado na
retransformacao para a escala original. Este modulo concentra os fatores de
correcao para evitar que cada motor implemente sua propria regra.
"""

from __future__ import annotations

import numpy as np



def fator_meyer(residuos_log: np.ndarray, n_parametros: int | None = None) -> float:
    """Calcula o Fator de Meyer para retransformacao logaritmica.

    A forma operacional utilizada e:

    FM = exp(0.5 * QM_res)

    onde QM_res e o quadrado medio dos residuos na escala logaritmica.

    Parameters
    ----------
    residuos_log:
        Residuos na escala logaritmica.
    n_parametros:
        Numero de parametros ajustados. Quando informado, utiliza n - p no
        denominador. Caso contrario, utiliza n.
    """

    residuos = np.asarray(residuos_log, dtype=float)

    if residuos.size == 0:
        raise ValueError("Nao ha residuos para calcular o Fator de Meyer.")

    denominador = residuos.size

    if n_parametros is not None:
        denominador = max(residuos.size - n_parametros, 1)

    qm_res = float(np.sum(residuos**2) / denominador)

    return float(np.exp(0.5 * qm_res))



def aplicar_fator_retransformacao(
    estimado_transformado: np.ndarray,
    fator_correcao: float,
    base_logaritmo: str = "ln",
) -> np.ndarray:
    """Retransforma estimativas logaritmicas para a escala original.

    Parameters
    ----------
    estimado_transformado:
        Estimativas na escala logaritmica.
    fator_correcao:
        Fator multiplicativo de correcao de vies.
    base_logaritmo:
        `ln` para logaritmo natural ou `log10` para logaritmo decimal.
    """

    valores = np.asarray(estimado_transformado, dtype=float)

    if base_logaritmo == "ln":
        return np.exp(valores) * fator_correcao

    if base_logaritmo == "log10":
        return (10**valores) * fator_correcao

    raise ValueError(f"Base logaritmica nao suportada: {base_logaritmo}")
