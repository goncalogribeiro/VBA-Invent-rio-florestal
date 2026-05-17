"""Geracao de distribuicao diametrica a partir da Weibull 3P.

Este modulo converte parametros Weibull em frequencias por classes
diametricas, permitindo uso posterior em prognose, sortimento e simulacao de
producao.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.stats import weibull_min


@dataclass(frozen=True)
class ClasseDiametricaWeibull:
    """Classe diametrica estimada pela distribuicao Weibull."""

    limite_inferior: float
    limite_superior: float
    centro_classe: float
    probabilidade: float
    arvores_por_ha: float


@dataclass(frozen=True)
class DistribuicaoDiametricaWeibull:
    """Distribuicao diametrica completa."""

    classes: list[ClasseDiametricaWeibull]
    total_arvores_ha: float
    soma_probabilidades: float
    parametro_a: float
    parametro_b: float
    parametro_c: float


class ErroDistribuicaoWeibull(Exception):
    """Erro ao gerar distribuicao diametrica Weibull."""



def gerar_classes_diametricas(
    dap_min: float,
    dap_max: float,
    amplitude: float,
) -> list[tuple[float, float]]:
    """Gera intervalos de classes diametricas."""

    if dap_min < 0:
        raise ErroDistribuicaoWeibull("DAP minimo nao pode ser negativo.")

    if dap_max <= dap_min:
        raise ErroDistribuicaoWeibull("DAP maximo deve ser maior que DAP minimo.")

    if amplitude <= 0:
        raise ErroDistribuicaoWeibull("Amplitude deve ser positiva.")

    limites = []
    atual = dap_min

    while atual < dap_max:
        superior = min(atual + amplitude, dap_max)
        limites.append((float(atual), float(superior)))
        atual = superior

    return limites



def gerar_distribuicao_weibull(
    parametro_a: float,
    parametro_b: float,
    parametro_c: float,
    arvores_ha: float,
    dap_min: float,
    dap_max: float,
    amplitude: float = 2.0,
) -> DistribuicaoDiametricaWeibull:
    """Gera distribuicao diametrica por classes a partir da Weibull 3P.

    Parameters
    ----------
    parametro_a:
        Parametro de locacao/deslocamento.
    parametro_b:
        Parametro de escala.
    parametro_c:
        Parametro de forma.
    arvores_ha:
        Numero total de arvores por hectare.
    dap_min:
        Limite inferior das classes.
    dap_max:
        Limite superior das classes.
    amplitude:
        Amplitude das classes diametricas.
    """

    if parametro_b <= 0 or parametro_c <= 0:
        raise ErroDistribuicaoWeibull(
            "Parametros b e c da Weibull devem ser positivos."
        )

    if arvores_ha < 0:
        raise ErroDistribuicaoWeibull(
            "Numero de arvores por hectare nao pode ser negativo."
        )

    classes_limites = gerar_classes_diametricas(
        dap_min=dap_min,
        dap_max=dap_max,
        amplitude=amplitude,
    )

    classes: list[ClasseDiametricaWeibull] = []
    soma_prob = 0.0

    for inferior, superior in classes_limites:
        x_inf = max(inferior - parametro_a, 0.0)
        x_sup = max(superior - parametro_a, 0.0)

        prob = float(
            weibull_min.cdf(x_sup, c=parametro_c, scale=parametro_b)
            - weibull_min.cdf(x_inf, c=parametro_c, scale=parametro_b)
        )

        prob = max(prob, 0.0)
        soma_prob += prob

        centro = (inferior + superior) / 2

        classes.append(
            ClasseDiametricaWeibull(
                limite_inferior=inferior,
                limite_superior=superior,
                centro_classe=float(centro),
                probabilidade=prob,
                arvores_por_ha=float(prob * arvores_ha),
            )
        )

    return DistribuicaoDiametricaWeibull(
        classes=classes,
        total_arvores_ha=float(sum(c.arvores_por_ha for c in classes)),
        soma_probabilidades=float(soma_prob),
        parametro_a=float(parametro_a),
        parametro_b=float(parametro_b),
        parametro_c=float(parametro_c),
    )
