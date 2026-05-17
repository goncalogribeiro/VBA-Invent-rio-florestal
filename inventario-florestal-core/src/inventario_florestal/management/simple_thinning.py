from __future__ import annotations

from math import pi

from inventario_florestal.ecology.dynamic_dominance import (
    CODOMINANTE,
    DOMINADA,
    DOMINANTE,
    SUPRIMIDA,
    classificar_posicao_sociologica,
    dap_medio,
    altura_media,
)
from inventario_florestal.testing.synthetic_dataset_generator import (
    ArvoreSintetica,
)


PRIORIDADE_REMOCAO = {
    SUPRIMIDA: 0,
    DOMINADA: 1,
    CODOMINANTE: 2,
    DOMINANTE: 3,
}



def calcular_g_individual(
    dap_cm: float,
) -> float:
    """
    Área basal individual.
    """

    return (
        pi * (dap_cm ** 2)
    ) / 40000.0



def _classificar_para_remocao(
    arvores: list[ArvoreSintetica],
):
    dap_med = dap_medio(arvores)
    alt_med = altura_media(arvores)

    classificadas = []

    for arvore in arvores:
        classe = classificar_posicao_sociologica(
            arvore,
            dap_med,
            alt_med,
        )

        classificadas.append(
            (
                PRIORIDADE_REMOCAO[classe],
                calcular_g_individual(
                    arvore.dap_cm
                ),
                arvore,
            )
        )

    classificadas.sort(
        key=lambda item: (
            item[0],
            item[1],
        )
    )

    return classificadas



def desbaste_seletivo_por_arvores(
    arvores: list[ArvoreSintetica],
    percentual_remocao: float,
) -> list[ArvoreSintetica]:
    """
    Desbaste seletivo por número de árvores.
    """

    if percentual_remocao <= 0:
        return arvores

    classificadas = _classificar_para_remocao(
        arvores
    )

    quantidade_remover = int(
        len(arvores)
        * percentual_remocao
    )

    remanescentes = [
        item[2]
        for item in classificadas[
            quantidade_remover:
        ]
    ]

    return remanescentes



def desbaste_seletivo_por_g(
    arvores: list[ArvoreSintetica],
    percentual_g_remover: float,
) -> list[ArvoreSintetica]:
    """
    Desbaste seletivo por área basal.
    """

    if percentual_g_remover <= 0:
        return arvores

    classificadas = _classificar_para_remocao(
        arvores
    )

    g_total = sum(
        item[1]
        for item in classificadas
    )

    g_alvo = (
        g_total
        * percentual_g_remover
    )

    g_removido = 0.0

    remanescentes = []

    for prioridade, gi, arvore in classificadas:
        if g_removido < g_alvo:
            g_removido += gi
            continue

        remanescentes.append(
            arvore
        )

    return remanescentes
