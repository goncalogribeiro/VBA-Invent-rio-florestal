from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PerfilSilvicultural:
    nome: str
    incremento_dap_esperado_cm_ano: float
    incremento_dap_maximo_cm_ano: float
    mortalidade_anual_esperada: float
    mortalidade_anual_maxima: float
    resposta_competicao: float
    resposta_desbaste: float
    confianca: float


PERFIS_SILVICULTURAIS = {
    "conservador": PerfilSilvicultural(
        nome="conservador",
        incremento_dap_esperado_cm_ano=1.2,
        incremento_dap_maximo_cm_ano=2.5,
        mortalidade_anual_esperada=0.03,
        mortalidade_anual_maxima=0.10,
        resposta_competicao=1.0,
        resposta_desbaste=0.8,
        confianca=0.7,
    ),
    "operacional": PerfilSilvicultural(
        nome="operacional",
        incremento_dap_esperado_cm_ano=2.0,
        incremento_dap_maximo_cm_ano=3.5,
        mortalidade_anual_esperada=0.02,
        mortalidade_anual_maxima=0.08,
        resposta_competicao=1.1,
        resposta_desbaste=1.0,
        confianca=0.8,
    ),
    "elite_genetica": PerfilSilvicultural(
        nome="elite_genetica",
        incremento_dap_esperado_cm_ano=3.0,
        incremento_dap_maximo_cm_ano=5.0,
        mortalidade_anual_esperada=0.015,
        mortalidade_anual_maxima=0.06,
        resposta_competicao=1.2,
        resposta_desbaste=1.2,
        confianca=0.6,
    ),
}



def obter_perfil_silvicultural(
    nome_perfil: str,
) -> PerfilSilvicultural:
    """
    Obtém perfil silvicultural.
    """

    if nome_perfil not in PERFIS_SILVICULTURAIS:
        raise ValueError(
            f"Perfil silvicultural inválido: {nome_perfil}"
        )

    return PERFIS_SILVICULTURAIS[
        nome_perfil
    ]
