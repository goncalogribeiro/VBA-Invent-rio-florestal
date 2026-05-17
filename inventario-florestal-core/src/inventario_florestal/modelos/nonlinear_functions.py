"""Funcoes biometricas nao lineares conhecidas.

Esta biblioteca evita interpretar livremente expressoes nao lineares em texto,
reduzindo risco numerico e aumentando auditabilidade. Cada funcao deve ser
explicitamente implementada, testada e documentada antes de entrar no torneio.
"""

from __future__ import annotations

import numpy as np


EPSILON = 1e-12



def chapman_richards_diametrico(
    d: np.ndarray,
    beta0: float,
    beta1: float,
    beta2: float,
) -> np.ndarray:
    """Modelo Chapman-Richards em funcao do DAP.

    Forma:

    h = 1.3 + beta0 * (1 - exp(-beta1 * d)) ** beta2

    Uso previsto:
    - hipsometria nao linear;
    - curva assintotica altura-DAP.
    """

    d = np.asarray(d, dtype=float)

    base = 1 - np.exp(-beta1 * d)
    base = np.clip(base, EPSILON, None)

    return 1.3 + beta0 * (base**beta2)



def naslund_hipsometrico(
    d: np.ndarray,
    beta0: float,
    beta1: float,
    beta2: float,
) -> np.ndarray:
    """Modelo hipsometrico de Naslund.

    Forma:

    h = 1.3 + d^2 / (beta0 + beta1*d + beta2*d^2)

    Uso previsto:
    - hipsometria nao linear;
    - comparacao com modelos lineares e linearizados.
    """

    d = np.asarray(d, dtype=float)

    denominador = beta0 + beta1 * d + beta2 * d**2
    denominador = np.where(
        np.abs(denominador) < EPSILON,
        np.sign(denominador) * EPSILON + EPSILON,
        denominador,
    )

    return 1.3 + (d**2 / denominador)



def silva_bailey_sitio(
    idade: np.ndarray,
    beta0: float,
    beta1: float,
    beta2: float,
) -> np.ndarray:
    """Modelo Silva-Bailey / Chapman-Richards para altura dominante.

    Forma:

    hdom = beta0 * (1 - exp(-beta1 * I)) ** beta2

    Uso previsto:
    - indice de sitio;
    - curvas anamórficas de altura dominante.
    """

    idade = np.asarray(idade, dtype=float)

    base = 1 - np.exp(-beta1 * idade)
    base = np.clip(base, EPSILON, None)

    return beta0 * (base**beta2)


FUNCOES_NAO_LINEARES = {
    "chapman_richards_diametrico": chapman_richards_diametrico,
    "naslund_hipsometrico": naslund_hipsometrico,
    "silva_bailey_sitio": silva_bailey_sitio,
}



def obter_funcao_nao_linear(nome: str):
    """Retorna uma funcao nao linear registrada pelo nome."""

    try:
        return FUNCOES_NAO_LINEARES[nome]
    except KeyError as exc:
        raise KeyError(f"Funcao nao linear nao registrada: {nome}") from exc
