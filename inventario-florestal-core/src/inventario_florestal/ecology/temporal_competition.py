from __future__ import annotations

from math import sqrt

from inventario_florestal.testing.synthetic_dataset_generator import (
    ArvoreSintetica,
)


DISTANCIA_MINIMA = 0.01



def distancia(
    arvore_a: ArvoreSintetica,
    arvore_b: ArvoreSintetica,
) -> float:
    dx = arvore_a.x - arvore_b.x
    dy = arvore_a.y - arvore_b.y

    return max(
        sqrt(dx * dx + dy * dy),
        DISTANCIA_MINIMA,
    )



def indice_competicao_hegyi(
    arvore_alvo: ArvoreSintetica,
    vizinhas: list[ArvoreSintetica],
) -> float:
    """
    Índice simplificado de Hegyi.
    """

    indice = 0.0

    for vizinha in vizinhas:
        if vizinha.id_arvore == arvore_alvo.id_arvore:
            continue

        indice += (
            vizinha.dap_cm
            / arvore_alvo.dap_cm
        ) / distancia(
            arvore_alvo,
            vizinha,
        )

    return indice



def fator_reducao_crescimento(
    indice_competicao: float,
) -> float:
    """
    Reduz crescimento conforme competição.
    """

    return max(
        0.2,
        1.0 - (indice_competicao * 0.05),
    )



def fator_aumento_mortalidade(
    indice_competicao: float,
) -> float:
    """
    Aumenta mortalidade conforme competição.
    """

    return 1.0 + (
        indice_competicao * 0.03
    )
