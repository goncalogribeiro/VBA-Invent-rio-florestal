"""Estimacao Weibull 3P por maxima verossimilhanca.

Implementacao inicial focada em distribuicao diametrica para prognose
florestal.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize
from scipy.stats import weibull_min


EPSILON = 1e-9


@dataclass(frozen=True)
class ResultadoWeibullMLE:
    """Resultado da estimacao Weibull 3P."""

    parametro_a: float
    parametro_b: float
    parametro_c: float
    log_likelihood: float
    convergiu: bool
    mensagem: str
    n: int


class ErroWeibullMLE(Exception):
    """Erro na estimacao Weibull."""



def _negative_log_likelihood(
    params: np.ndarray,
    dados: np.ndarray,
) -> float:
    """Negative log-likelihood Weibull 3P."""

    a, b, c = params

    if b <= EPSILON or c <= EPSILON:
        return 1e30

    ajustado = dados - a

    if np.any(ajustado <= 0):
        return 1e30

    log_pdf = weibull_min.logpdf(ajustado, c=c, scale=b)

    return -float(np.sum(log_pdf))



def ajustar_weibull_mle(
    diametros: np.ndarray,
    chute_inicial: tuple[float, float, float] | None = None,
) -> ResultadoWeibullMLE:
    """Ajusta Weibull 3P via máxima verossimilhança."""

    dados = np.asarray(diametros, dtype=float)
    dados = dados[np.isfinite(dados)]

    if len(dados) < 10:
        raise ErroWeibullMLE(
            "Weibull requer pelo menos 10 observacoes validas."
        )

    if np.any(dados <= 0):
        raise ErroWeibullMLE(
            "Diametros devem ser positivos."
        )

    if chute_inicial is None:
        a0 = max(0.0, float(np.min(dados) * 0.5))
        b0 = float(np.std(dados))
        c0 = 2.0
    else:
        a0, b0, c0 = chute_inicial

    resultado = minimize(
        _negative_log_likelihood,
        x0=np.array([a0, b0, c0], dtype=float),
        args=(dados,),
        method="L-BFGS-B",
        bounds=[
            (0.0, float(np.min(dados) - EPSILON)),
            (EPSILON, None),
            (EPSILON, None),
        ],
    )

    if not resultado.success:
        raise ErroWeibullMLE(resultado.message)

    a, b, c = resultado.x

    return ResultadoWeibullMLE(
        parametro_a=float(a),
        parametro_b=float(b),
        parametro_c=float(c),
        log_likelihood=-float(resultado.fun),
        convergiu=bool(resultado.success),
        mensagem=str(resultado.message),
        n=int(len(dados)),
    )
