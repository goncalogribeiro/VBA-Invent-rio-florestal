from __future__ import annotations

from dataclasses import replace
from random import random

from inventario_florestal.core.biological_constraints import (
    validar_crescimento_dap,
    validar_mortalidade,
)
from inventario_florestal.ecology.dynamic_dominance import (
    CODOMINANTE,
    DOMINADA,
    DOMINANTE,
    SUPRIMIDA,
    classificar_posicao_sociologica,
    dap_medio,
    altura_media,
)
from inventario_florestal.ecology.temporal_competition import (
    fator_aumento_mortalidade,
    fator_reducao_crescimento,
    indice_competicao_hegyi,
)
from inventario_florestal.silviculture.silvicultural_profiles import (
    obter_perfil_silvicultural,
)
from inventario_florestal.testing.synthetic_dataset_generator import (
    ArvoreSintetica,
)


DOMINANCIA_CRESCIMENTO = {
    DOMINANTE: 1.15,
    CODOMINANTE: 1.0,
    DOMINADA: 0.80,
    SUPRIMIDA: 0.55,
}


DOMINANCIA_MORTALIDADE = {
    DOMINANTE: 0.75,
    CODOMINANTE: 1.0,
    DOMINADA: 1.35,
    SUPRIMIDA: 1.80,
}



def simular_crescimento_anual(
    arvore: ArvoreSintetica,
    incremento_dap_cm: float,
    incremento_altura_m: float,
) -> ArvoreSintetica:
    incremento_dap_cm = validar_crescimento_dap(
        incremento_dap_cm
    )

    return replace(
        arvore,
        dap_cm=arvore.dap_cm + incremento_dap_cm,
        altura_m=arvore.altura_m + incremento_altura_m,
        idade=arvore.idade + 1,
    )



def simular_mortalidade(
    mortalidade_anual: float,
) -> bool:
    mortalidade_anual = validar_mortalidade(
        mortalidade_anual
    )

    return random() < mortalidade_anual



def simular_ano(
    arvores: list[ArvoreSintetica],
    perfil_nome: str = "operacional",
) -> list[ArvoreSintetica]:
    perfil = obter_perfil_silvicultural(
        perfil_nome
    )

    dap_medio_povoamento = dap_medio(
        arvores
    )

    altura_media_povoamento = altura_media(
        arvores
    )

    sobreviventes = []

    for arvore in arvores:
        classe_sociologica = classificar_posicao_sociologica(
            arvore,
            dap_medio_povoamento,
            altura_media_povoamento,
        )

        indice_competicao = indice_competicao_hegyi(
            arvore,
            arvores,
        )

        reducao = fator_reducao_crescimento(
            indice_competicao
        )

        aumento_mortalidade = fator_aumento_mortalidade(
            indice_competicao
        )

        fator_crescimento = DOMINANCIA_CRESCIMENTO[
            classe_sociologica
        ]

        fator_mortalidade = DOMINANCIA_MORTALIDADE[
            classe_sociologica
        ]

        mortalidade = (
            perfil.mortalidade_anual_esperada
            * aumento_mortalidade
            * fator_mortalidade
        )

        if simular_mortalidade(
            mortalidade
        ):
            continue

        incremento_dap = (
            perfil.incremento_dap_esperado_cm_ano
            * reducao
            * fator_crescimento
        )

        incremento_altura = (
            0.8
            * reducao
            * fator_crescimento
        )

        arvore_atualizada = simular_crescimento_anual(
            arvore,
            incremento_dap_cm=incremento_dap,
            incremento_altura_m=incremento_altura,
        )

        sobreviventes.append(
            arvore_atualizada
        )

    return sobreviventes



def simular_periodo(
    arvores: list[ArvoreSintetica],
    anos: int,
    perfil_nome: str = "operacional",
) -> list[ArvoreSintetica]:
    estado = arvores

    for _ in range(anos):
        estado = simular_ano(
            estado,
            perfil_nome=perfil_nome,
        )

    return estado
