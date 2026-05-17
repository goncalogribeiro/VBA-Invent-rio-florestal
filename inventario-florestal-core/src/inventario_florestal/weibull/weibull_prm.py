"""Parameter Recovery Method (PRM) para Weibull 3P.

Implementacao inicial baseada em recuperacao de parametros a partir de
atributos diametricos do povoamento.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq
from scipy.special import gamma


EPSILON = 1e-9


@dataclass(frozen=True)
class ResultadoWeibullPRM:
    """Resultado da recuperacao de parametros Weibull."""

    parametro_a: float
    parametro_b: float
    parametro_c: float
    diametro_medio_estimado: float
    variancia_estimada: float
    convergiu: bool
    metodo: str


class ErroWeibullPRM(Exception):
    """Erro na recuperacao Weibull PRM."""



def _equacao_shape(
    c: float,
    media: float,
    variancia: float,
) -> float:
    """Equacao implicita para recuperacao do shape Weibull."""

    gamma1 = gamma(1 + 1 / c)
    gamma2 = gamma(1 + 2 / c)

    lhs = variancia / (media**2)
    rhs = (gamma2 / (gamma1**2)) - 1

    return rhs - lhs



def ajustar_weibull_prm(
    diametro_medio: float,
    variancia_diametrica: float,
    diametro_minimo: float = 0.0,
) -> ResultadoWeibullPRM:
    """Recupera parametros Weibull 3P por PRM.

    Parameters
    ----------
    diametro_medio:
        DAP medio do povoamento.
    variancia_diametrica:
        Variancia dos diametros.
    diametro_minimo:
        Parametro de deslocamento inicial.
    """

    media = float(diametro_medio)
    variancia = float(variancia_diametrica)
    a = float(diametro_minimo)

    if media <= 0:
        raise ErroWeibullPRM("Diametro medio deve ser positivo.")

    if variancia <= 0:
        raise ErroWeibullPRM("Variancia diametrica deve ser positiva.")

    media_ajustada = media - a

    if media_ajustada <= 0:
        raise ErroWeibullPRM(
            "Diametro medio ajustado pelo parametro a deve ser positivo."
        )

    try:
        c = brentq(
            _equacao_shape,
            a=0.1,
            b=20.0,
            args=(media_ajustada, variancia),
            maxiter=1000,
        )

    except ValueError as exc:
        raise ErroWeibullPRM(
            "Falha na convergencia do parametro shape Weibull."
        ) from exc

    gamma1 = gamma(1 + 1 / c)

    b = media_ajustada / gamma1

    media_estim = a + b * gamma1

    gamma2 = gamma(1 + 2 / c)
    variancia_estim = (b**2) * (gamma2 - gamma1**2)

    return ResultadoWeibullPRM(
        parametro_a=float(a),
        parametro_b=float(b),
        parametro_c=float(c),
        diametro_medio_estimado=float(media_estim),
        variancia_estimada=float(variancia_estim),
        convergiu=True,
        metodo="PRM",
    )
