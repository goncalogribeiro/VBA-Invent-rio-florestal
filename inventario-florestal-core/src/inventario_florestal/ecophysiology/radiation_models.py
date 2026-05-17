from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CopaFlorestal:
    identificador: str
    area_copa_m2: float
    transmissividade: float
    altura_m: float


class ErroRadiacao(Exception):
    pass



def radiacao_interceptada(
    radiacao_incidente: float,
    transmissividade: float,
) -> float:
    """
    Interceptação simplificada de radiação.
    """

    return radiacao_incidente * (1 - transmissividade)



def vigor_ecofisiologico(
    radiacao_absorvida: float,
    area_copa_m2: float,
) -> float:
    """
    Índice simplificado de vigor.
    """

    if area_copa_m2 <= 0:
        raise ErroRadiacao(
            "Área de copa inválida."
        )

    return radiacao_absorvida / area_copa_m2



def analisar_radiacao_florestal(
    copa: CopaFlorestal,
    radiacao_incidente: float,
) -> dict[str, float]:
    """
    Primeira camada ecofisiológica.

    Futuramente:
    - ray tracing real;
    - aprendizado adaptativo;
    - IA ecológica;
    - fotossíntese espacial.
    """

    radiacao = radiacao_interceptada(
        radiacao_incidente,
        copa.transmissividade,
    )

    vigor = vigor_ecofisiologico(
        radiacao,
        copa.area_copa_m2,
    )

    return {
        "radiacao_interceptada": float(radiacao),
        "vigor_ecofisiologico": float(vigor),
    }
