from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EstruturaFoliar:
    identificador: str
    area_foliar_m2: float
    area_solo_m2: float
    radiacao_interceptada: float


class ErroLAI(Exception):
    pass



def calcular_lai(
    area_foliar_m2: float,
    area_solo_m2: float,
) -> float:
    """
    Calcula índice de área foliar.
    """

    if area_solo_m2 <= 0:
        raise ErroLAI(
            "Área de solo inválida."
        )

    return area_foliar_m2 / area_solo_m2



def assimilacao_carbono(
    lai: float,
    radiacao_interceptada: float,
) -> float:
    """
    Assimilação simplificada de carbono.
    """

    return lai * radiacao_interceptada * 0.02



def analisar_estrutura_foliar(
    estrutura: EstruturaFoliar,
) -> dict[str, float]:
    """
    Primeira camada ecofisiológica avançada.

    Futuramente:
    - fotossíntese espacial;
    - assimilação líquida;
    - respiração;
    - IA ecofisiológica.
    """

    lai = calcular_lai(
        estrutura.area_foliar_m2,
        estrutura.area_solo_m2,
    )

    carbono = assimilacao_carbono(
        lai,
        estrutura.radiacao_interceptada,
    )

    return {
        "lai": float(lai),
        "carbono_assimilado": float(carbono),
    }
