from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RasterClimatico:
    identificador: str
    resolucao_m: float
    variavel: str


@dataclass(frozen=True)
class CamadaNDVI:
    identificador: str
    media_ndvi: float


@dataclass(frozen=True)
class VooDrone:
    identificador: str
    altitude_m: float
    area_ha: float


class ErroSensoriamento(Exception):
    pass



def classificar_ndvi(
    valor_ndvi: float,
) -> str:
    """
    Classificação simplificada de vigor.
    """

    if valor_ndvi < 0.2:
        return "baixo"

    if valor_ndvi < 0.5:
        return "medio"

    return "alto"



def estimar_vigor_florestal(
    camada: CamadaNDVI,
) -> dict[str, str | float]:
    """
    Primeira camada de analytics remoto.

    Futuramente:
    - LiDAR;
    - satelite;
    - biometria remota;
    - carbono espacial.
    """

    classe = classificar_ndvi(
        camada.media_ndvi
    )

    return {
        "identificador": camada.identificador,
        "ndvi": camada.media_ndvi,
        "classe_vigor": classe,
    }
