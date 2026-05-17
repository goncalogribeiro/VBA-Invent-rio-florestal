from __future__ import annotations

from dataclasses import asdict, dataclass
import json


@dataclass(frozen=True)
class GeoFeature:
    identificador: str
    latitude: float
    longitude: float
    propriedades: dict


class ErroGeoJSON(Exception):
    pass



def feature_para_geojson(
    feature: GeoFeature,
) -> dict:
    """
    Converte feature simplificada para GeoJSON.
    """

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                feature.longitude,
                feature.latitude,
            ],
        },
        "properties": {
            "identificador": feature.identificador,
            **feature.propriedades,
        },
    }



def exportar_geojson(
    features: list[GeoFeature],
    caminho_saida: str,
) -> None:
    """
    Exporta coleção GeoJSON.

    Futuramente:
    - polígonos;
    - linhas;
    - CRS;
    - PostGIS;
    - shapefile.
    """

    collection = {
        "type": "FeatureCollection",
        "features": [
            feature_para_geojson(f)
            for f in features
        ],
    }

    with open(caminho_saida, "w", encoding="utf-8") as arquivo:
        json.dump(collection, arquivo, indent=2)
