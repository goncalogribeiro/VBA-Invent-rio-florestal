from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoProdutividade:
    ica: float
    ima: float
    idade: int
    volume_total: float
    sitio_categoria: str


class ErroProdutividade(Exception):
    pass



def calcular_ica(
    volume_atual: float,
    volume_anterior: float,
) -> float:
    """
    Incremento Corrente Anual.
    """

    return volume_atual - volume_anterior



def calcular_ima(
    volume_total: float,
    idade: int,
) -> float:
    """
    Incremento Médio Anual.
    """

    if idade <= 0:
        raise ErroProdutividade(
            "Idade deve ser maior que zero."
        )

    return volume_total / idade



def classificar_sitio(
    altura_dominante: float,
) -> str:
    """
    Primeira classificação simplificada de sítio.

    Futuramente:
    - curvas anamórficas;
    - ADA;
    - GADA;
    - polimórficas.
    """

    if altura_dominante >= 28:
        return "sitio_alto"

    if altura_dominante >= 22:
        return "sitio_medio"

    return "sitio_baixo"



def calcular_produtividade(
    volume_atual: float,
    volume_anterior: float,
    idade: int,
    altura_dominante: float,
) -> ResultadoProdutividade:
    """
    Calcula métricas dinâmicas de produtividade.
    """

    ica = calcular_ica(
        volume_atual=volume_atual,
        volume_anterior=volume_anterior,
    )

    ima = calcular_ima(
        volume_total=volume_atual,
        idade=idade,
    )

    sitio = classificar_sitio(altura_dominante)

    return ResultadoProdutividade(
        ica=float(ica),
        ima=float(ima),
        idade=idade,
        volume_total=float(volume_atual),
        sitio_categoria=sitio,
    )
