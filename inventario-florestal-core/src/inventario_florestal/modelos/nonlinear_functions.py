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



def granemann_hipsometrico(
    x: np.ndarray,
    beta0: float,
    beta1: float,
) -> np.ndarray:
    """Modelo hipsometrico experimental Granemann.

    Forma:

    h = 1.3 + (hdom - 1.3) *
        [1 - exp(-beta0 * (d / d_med)^beta1 * sqrt(G / 100))]

    Variaveis esperadas em `x`:

    - x[0]: d, DAP individual em cm;
    - x[1]: hdom, altura dominante em m;
    - x[2]: d_med, DAP medio do povoamento em cm;
    - x[3]: G, area basal em m²/ha.

    Status cientifico:
    - modelo experimental;
    - requer validacao com dados reais;
    - nao deve ser tratado como modelo consolidado de literatura.
    """

    matriz = np.asarray(x, dtype=float)

    if matriz.shape[0] != 4:
        raise ValueError(
            "O modelo Granemann requer x com quatro linhas: d, hdom, d_med e G."
        )

    d = matriz[0]
    hdom = matriz[1]
    d_med = np.clip(matriz[2], EPSILON, None)
    g = np.clip(matriz[3], EPSILON, None)

    razao_diametrica = np.clip(d / d_med, EPSILON, None)
    competencia = np.sqrt(g / 100)

    expoente = -beta0 * (razao_diametrica**beta1) * competencia

    return 1.3 + (hdom - 1.3) * (1 - np.exp(expoente))



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
    "granemann_hipsometrico": granemann_hipsometrico,
    "naslund_hipsometrico": naslund_hipsometrico,
    "silva_bailey_sitio": silva_bailey_sitio,
}



def obter_funcao_nao_linear(nome: str):
    """Retorna uma funcao nao linear registrada pelo nome."""

    try:
        return FUNCOES_NAO_LINEARES[nome]
    except KeyError as exc:
        raise KeyError(f"Funcao nao linear nao registrada: {nome}") from exc
