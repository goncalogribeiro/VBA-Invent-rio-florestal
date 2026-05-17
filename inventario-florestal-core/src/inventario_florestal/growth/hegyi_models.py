from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class ArvoreCompeticao:
    identificador: str
    x: float
    y: float
    dap_cm: float
    altura_m: float
    area_basal_m2: float


class ErroHegyi(Exception):
    pass



def distancia(
    a: ArvoreCompeticao,
    b: ArvoreCompeticao,
) -> float:
    dx = a.x - b.x
    dy = a.y - b.y

    return sqrt((dx ** 2) + (dy ** 2))



def indice_hegyi(
    arvore: ArvoreCompeticao,
    vizinhas: list[ArvoreCompeticao],
    raio_m: float = 8.0,
) -> float:
    """
    Índice de competição de Hegyi simplificado.
    """

    indice = 0.0

    for vizinha in vizinhas:
        d = distancia(arvore, vizinha)

        if d == 0:
            continue

        if d <= raio_m:
            indice += (
                vizinha.dap_cm / arvore.dap_cm
            ) / d

    return indice



def calcular_bal(
    arvore: ArvoreCompeticao,
    vizinhas: list[ArvoreCompeticao],
) -> float:
    """
    Basal Area in Larger Trees simplificado.
    """

    return sum(
        v.area_basal_m2
        for v in vizinhas
        if v.dap_cm > arvore.dap_cm
    )



def competicao_copa(
    arvore: ArvoreCompeticao,
    vizinhas: list[ArvoreCompeticao],
) -> float:
    """
    Competição de copa simplificada.
    """

    competencia = 0.0

    for vizinha in vizinhas:
        if vizinha.altura_m > arvore.altura_m:
            competencia += 1.0

    return competencia



def analisar_competicao_avancada(
    arvore: ArvoreCompeticao,
    vizinhas: list[ArvoreCompeticao],
) -> dict[str, float]:
    """
    Primeira camada ecológica avançada.

    Futuramente:
    - competição luminosa real;
    - sucessão espacial;
    - machine learning ecológico;
    - crescimento adaptativo.
    """

    hegyi = indice_hegyi(
        arvore,
        vizinhas,
    )

    bal = calcular_bal(
        arvore,
        vizinhas,
    )

    copa = competicao_copa(
        arvore,
        vizinhas,
    )

    return {
        "indice_hegyi": float(hegyi),
        "bal": float(bal),
        "competicao_copa": float(copa),
    }
