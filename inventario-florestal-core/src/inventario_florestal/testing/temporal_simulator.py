from __future__ import annotations

from dataclasses import replace
from random import random

from inventario_florestal.core.biological_constraints import (
    validar_crescimento_dap,
    validar_mortalidade,
)
from inventario_florestal.silviculture.silvicultural_profiles import (
    obter_perfil_silvicultural,
)
from inventario_florestal.testing.synthetic_dataset_generator import (
    ArvoreSintetica,
)



def simular_crescimento_anual(
    arvore: ArvoreSintetica,
    incremento_dap_cm: float,
    incremento_altura_m: float,
) -> ArvoreSintetica:
    """
    Simula crescimento anual simplificado.
    """

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
    """
    Retorna True se árvore morreu.
    """

    mortalidade_anual = validar_mortalidade(
        mortalidade_anual
    )

    return random() < mortalidade_anual



def simular_ano(
    arvores: list[ArvoreSintetica],
    perfil_nome: str = "operacional",
) -> list[ArvoreSintetica]:
    """
    Simula um ciclo anual sintético.
    """

    perfil = obter_perfil_silvicultural(
        perfil_nome
    )

    sobreviventes = []

    for arvore in arvores:
        if simular_mortalidade(
            perfil.mortalidade_anual_esperada
        ):
            continue

        arvore_atualizada = simular_crescimento_anual(
            arvore,
            incremento_dap_cm=perfil.incremento_dap_esperado_cm_ano,
            incremento_altura_m=0.8,
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
    """
    Simula múltiplos ciclos anuais.
    """

    estado = arvores

    for _ in range(anos):
        estado = simular_ano(
            estado,
            perfil_nome=perfil_nome,
        )

    return estado
