from __future__ import annotations

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



def desbaste_seletivo_por_arvores(
    arvores: list[ArvoreSintetica],
    percentual_remocao: float,
) -> list[ArvoreSintetica]:
    """
    Desbaste seletivo simplificado para testes operacionais.
    """

    if percentual_remocao <= 0:
        return arvores

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
                arvore,
            )
        )

    classificadas.sort(
        key=lambda item: item[0]
    )

    quantidade_remover = int(
        len(arvores)
        * percentual_remocao
    )

    remanescentes = [
        item[1]
        for item in classificadas[
            quantidade_remover:
        ]
    ]

    return remanescentes
