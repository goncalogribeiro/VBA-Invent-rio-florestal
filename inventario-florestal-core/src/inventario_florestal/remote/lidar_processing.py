from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PontoLiDAR:
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class RasterClimatico:
    identificador: str
    resolucao_m: float
    variavel: str


class ErroLiDAR(Exception):
    pass



def calcular_altura_media(
    pontos: list[PontoLiDAR],
) -> float:
    """
    Calcula altura média simplificada.
    """

    if not pontos:
        raise ErroLiDAR(
            "Nuvem de pontos vazia."
        )

    return sum(p.z for p in pontos) / len(pontos)



def classificar_estrutura_vertical(
    altura_media: float,
) -> str:
    """
    Classificação estrutural simplificada.
    """

    if altura_media < 10:
        return "baixo"

    if altura_media < 20:
        return "medio"

    return "alto"



def analisar_nuvem_pontos(
    pontos: list[PontoLiDAR],
) -> dict[str, float | str]:
    """
    Primeira camada LiDAR.

    Futuramente:
    - segmentação individual;
    - carbono;
    - biomassa;
    - machine vision;
    - IA.
    """

    altura_media = calcular_altura_media(pontos)

    estrutura = classificar_estrutura_vertical(
        altura_media
    )

    return {
        "altura_media": float(altura_media),
        "estrutura_vertical": estrutura,
    }
