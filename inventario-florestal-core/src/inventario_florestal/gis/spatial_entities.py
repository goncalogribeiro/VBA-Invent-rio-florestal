from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Coordenada:
    latitude: float
    longitude: float


@dataclass(frozen=True)
class ParcelaEspacial:
    codigo: str
    coordenada: Coordenada
    area_m2: float


@dataclass(frozen=True)
class TalhaoEspacial:
    codigo: str
    area_ha: float
    centroide: Coordenada


@dataclass(frozen=True)
class FazendaEspacial:
    nome: str
    area_total_ha: float
    centroide: Coordenada


class ErroGIS(Exception):
    pass



def calcular_distancia_aproximada(
    ponto_a: Coordenada,
    ponto_b: Coordenada,
) -> float:
    """
    Distância euclidiana simplificada.

    Futuramente:
    - geodésica;
    - projeções;
    - UTM;
    - PostGIS.
    """

    dx = ponto_a.latitude - ponto_b.latitude
    dy = ponto_a.longitude - ponto_b.longitude

    return ((dx ** 2) + (dy ** 2)) ** 0.5



def validar_coordenada(
    coordenada: Coordenada,
) -> bool:
    """
    Validação básica de coordenadas.
    """

    return (
        -90 <= coordenada.latitude <= 90
        and -180 <= coordenada.longitude <= 180
    )
