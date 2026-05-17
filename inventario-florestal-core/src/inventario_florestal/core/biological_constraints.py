from __future__ import annotations


class ErroBiologico(Exception):
    pass


LIMITES_BIOLOGICOS = {
    "crescimento_dap_anual_min": 0.0,
    "crescimento_dap_anual_max": 5.0,
    "mortalidade_min": 0.0,
    "mortalidade_max": 1.0,
    "lai_min": 0.0,
    "lai_max": 12.0,
    "gpp_min": 0.0,
    "npp_min": 0.0,
    "volume_min": 0.0,
    "area_basal_min": 0.0,
}



def limitar_intervalo(
    valor: float,
    minimo: float,
    maximo: float,
) -> float:
    return max(minimo, min(valor, maximo))



def validar_crescimento_dap(
    crescimento_cm_ano: float,
) -> float:
    """
    Controla crescimento biologicamente plausível.
    """

    return limitar_intervalo(
        crescimento_cm_ano,
        LIMITES_BIOLOGICOS[
            "crescimento_dap_anual_min"
        ],
        LIMITES_BIOLOGICOS[
            "crescimento_dap_anual_max"
        ],
    )



def validar_mortalidade(
    mortalidade: float,
) -> float:
    """
    Garante mortalidade entre 0 e 1.
    """

    return limitar_intervalo(
        mortalidade,
        LIMITES_BIOLOGICOS[
            "mortalidade_min"
        ],
        LIMITES_BIOLOGICOS[
            "mortalidade_max"
        ],
    )



def validar_lai(
    lai: float,
) -> float:
    """
    Controla LAI plausível.
    """

    return limitar_intervalo(
        lai,
        LIMITES_BIOLOGICOS[
            "lai_min"
        ],
        LIMITES_BIOLOGICOS[
            "lai_max"
        ],
    )



def validar_variavel_nao_negativa(
    valor: float,
) -> float:
    """
    Impede valores negativos.
    """

    return max(0.0, valor)
