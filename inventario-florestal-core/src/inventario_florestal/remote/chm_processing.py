from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModeloTerreno:
    resolucao_m: float
    elevacao_media: float


@dataclass(frozen=True)
class ModeloSuperficie:
    resolucao_m: float
    altura_media: float


@dataclass(frozen=True)
class CopaSegmentada:
    identificador: str
    altura_m: float
    diametro_copa_m: float


class ErroCHM(Exception):
    pass



def calcular_chm(
    dsm: ModeloSuperficie,
    dtm: ModeloTerreno,
) -> float:
    return dsm.altura_media - dtm.elevacao_media



def estimar_biomassa(
    altura_m: float,
    diametro_copa_m: float,
) -> float:
    return altura_m * diametro_copa_m * 0.5



def analisar_copa(
    copa: CopaSegmentada,
) -> dict[str, float]:
    biomassa = estimar_biomassa(
        altura_m=copa.altura_m,
        diametro_copa_m=copa.diametro_copa_m,
    )

    return {
        "altura_m": float(copa.altura_m),
        "diametro_copa_m": float(copa.diametro_copa_m),
        "biomassa": float(biomassa),
    }
