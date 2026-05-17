from __future__ import annotations


FATOR_SUAVIZACAO = 0.25
LIMITE_AJUSTE_ADAPTATIVO = 0.10



def suavizacao_temporal(
    valor_anterior: float,
    valor_novo: float,
    fator_suavizacao: float = FATOR_SUAVIZACAO,
) -> float:
    """
    Suavização temporal simples.
    """

    return (
        valor_anterior
        + (
            valor_novo - valor_anterior
        ) * fator_suavizacao
    )



def limitar_ajuste_adaptativo(
    valor_anterior: float,
    valor_recalibrado: float,
    limite: float = LIMITE_AJUSTE_ADAPTATIVO,
) -> float:
    """
    Limita drift adaptativo.
    """

    diferenca = (
        valor_recalibrado - valor_anterior
    )

    ajuste_maximo = (
        abs(valor_anterior) * limite
    )

    if diferenca > ajuste_maximo:
        return valor_anterior + ajuste_maximo

    if diferenca < -ajuste_maximo:
        return valor_anterior - ajuste_maximo

    return valor_recalibrado



def aplicar_inercia_ecologica(
    valor_anterior: float,
    valor_novo: float,
) -> float:
    """
    Aplica memória ecológica temporal.
    """

    return suavizacao_temporal(
        valor_anterior,
        valor_novo,
    )
