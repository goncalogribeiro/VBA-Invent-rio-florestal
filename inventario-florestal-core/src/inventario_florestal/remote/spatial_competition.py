from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class ArvoreEspacial:
    identificador: str
    x: float
    y: float
    dap_cm: float


class ErroCompeticao(Exception):
    pass



def calcular_distancia(
    a: ArvoreEspacial,
    b: ArvoreEspacial,
) -> float:
    dx = a.x - b.x
    dy = a.y - b.y

    return sqrt((dx ** 2) + (dy ** 2))



def indice_competicao_local(
    arvore: ArvoreEspacial,
    vizinhas: list[ArvoreEspacial],
    raio_m: float = 5.0,
) -> float:
    """
    Primeira camada de competição espacial.
    """

    competencia = 0.0

    for vizinha in vizinhas:
        distancia = calcular_distancia(
            arvore,
            vizinha,
        )

        if distancia == 0:
            continue

        if distancia <= raio_m:
            competencia += (
                vizinha.dap_cm / distancia
            )

    return competencia
