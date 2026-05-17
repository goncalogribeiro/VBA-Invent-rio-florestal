from __future__ import annotations

from dataclasses import dataclass
from math import exp, log


@dataclass(frozen=True)
class ResultadoMortalidade:
    n_inicial: float
    n_final: float
    mortalidade_percentual: float
    modelo_utilizado: str
    idade_inicial: int
    idade_final: int


class ErroMortalidade(Exception):
    pass



def modelo_lenhart(
    n1: float,
    idade1: int,
    idade2: int,
    beta1: float = -0.015,
    beta2: float = -0.08,
) -> float:
    """
    Modelo Lenhart simplificado.

    N2 = N1 * exp[beta1*(I2-I1) + beta2*ln(I2/I1)]
    """

    return n1 * exp(
        beta1 * (idade2 - idade1)
        + beta2 * log(idade2 / idade1)
    )



def projetar_mortalidade(
    n_atual: float,
    idade_atual: int,
    idade_futura: int,
    modelo: str = "lenhart",
) -> ResultadoMortalidade:
    """
    Primeira camada de mortalidade dinâmica.

    Futuramente:
    - torneio de sobrevivência;
    - competição;
    - sítio;
    - Reineke;
    - Hart-Becking;
    - mortalidade espacial.
    """

    if idade_futura <= idade_atual:
        raise ErroMortalidade(
            "Idade futura deve ser maior que idade atual."
        )

    if modelo != "lenhart":
        raise ErroMortalidade(
            f"Modelo não implementado: {modelo}"
        )

    n_final = modelo_lenhart(
        n1=n_atual,
        idade1=idade_atual,
        idade2=idade_futura,
    )

    mortalidade = max(0.0, 1 - (n_final / n_atual))

    return ResultadoMortalidade(
        n_inicial=float(n_atual),
        n_final=float(n_final),
        mortalidade_percentual=float(mortalidade * 100),
        modelo_utilizado=modelo,
        idade_inicial=idade_atual,
        idade_final=idade_futura,
    )
