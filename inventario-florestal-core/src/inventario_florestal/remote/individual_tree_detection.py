from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArvoreIndividual:
    identificador: str
    altura_m: float
    diametro_copa_m: float
    biomassa_kg: float


@dataclass(frozen=True)
class Voxel:
    x: int
    y: int
    z: int
    densidade: float


class ErroITD(Exception):
    pass



def estimar_carbono(
    biomassa_kg: float,
) -> float:
    """
    Estimativa simplificada de carbono.
    """

    return biomassa_kg * 0.5



def calcular_volume_voxelizado(
    voxels: list[Voxel],
) -> float:
    """
    Volume simplificado baseado em voxels.
    """

    return sum(v.densidade for v in voxels)



def analisar_arvore_individual(
    arvore: ArvoreIndividual,
) -> dict[str, float]:
    """
    Primeira camada de ITD.

    Futuramente:
    - deep learning;
    - visão computacional;
    - segmentação automática;
    - competição espacial.
    """

    carbono = estimar_carbono(
        arvore.biomassa_kg
    )

    return {
        "altura_m": float(arvore.altura_m),
        "diametro_copa_m": float(arvore.diametro_copa_m),
        "biomassa_kg": float(arvore.biomassa_kg),
        "carbono_kg": float(carbono),
    }
