from __future__ import annotations

from statistics import mean

from inventario_florestal.testing.synthetic_dataset_generator import (
    ArvoreSintetica,
)


DOMINANTE = "dominante"
CODOMINANTE = "codominante"
DOMINADA = "dominada"
SUPRIMIDA = "suprimida"



def dap_medio(
    arvores: list[ArvoreSintetica],
) -> float:
    return mean(
        arvore.dap_cm
        for arvore in arvores
    )



def altura_media(
    arvores: list[ArvoreSintetica],
) -> float:
    return mean(
        arvore.altura_m
        for arvore in arvores
    )



def classificar_posicao_sociologica(
    arvore: ArvoreSintetica,
    dap_medio_povoamento: float,
    altura_media_povoamento: float,
) -> str:
    """
    Estratificação sociológica simplificada.
    """

    relacao_dap = (
        arvore.dap_cm
        / dap_medio_povoamento
    )

    relacao_altura = (
        arvore.altura_m
        / altura_media_povoamento
    )

    indice = (
        relacao_dap
        + relacao_altura
    ) / 2

    if indice >= 1.2:
        return DOMINANTE

    if indice >= 1.0:
        return CODOMINANTE

    if indice >= 0.8:
        return DOMINADA

    return SUPRIMIDA
