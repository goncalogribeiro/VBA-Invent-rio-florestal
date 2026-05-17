from __future__ import annotations

from dataclasses import dataclass
from random import gauss
from math import sqrt


@dataclass(frozen=True)
class ResultadoCholesky:
    crescimento: float
    mortalidade: float
    preco: float
    produtividade: float


class ErroCholesky(Exception):
    pass



def decomposicao_cholesky_2x2(
    a11: float,
    a12: float,
    a22: float,
) -> tuple[tuple[float, float], tuple[float, float]]:
    """
    Primeira implementação simplificada de Cholesky.
    """

    l11 = sqrt(a11)
    l21 = a12 / l11
    l22 = sqrt(a22 - (l21 ** 2))

    return (
        (l11, 0.0),
        (l21, l22),
    )



def gerar_choques_correlacionados(
    correlacao: float,
) -> tuple[float, float]:
    """
    Gera dois choques correlacionados.
    """

    matriz = decomposicao_cholesky_2x2(
        a11=1.0,
        a12=correlacao,
        a22=1.0,
    )

    z1 = gauss(0, 1)
    z2 = gauss(0, 1)

    x1 = matriz[0][0] * z1

    x2 = (
        matriz[1][0] * z1
        + matriz[1][1] * z2
    )

    return x1, x2



def gerar_cenario_cholesky(
    crescimento_base: float,
    mortalidade_base: float,
    correlacao: float = -0.65,
) -> ResultadoCholesky:
    """
    Primeira camada estatisticamente consistente.

    Futuramente:
    - NxN;
    - matrizes reais;
    - séries históricas;
    - clima;
    - preços.
    """

    choque_crescimento, choque_mortalidade = (
        gerar_choques_correlacionados(correlacao)
    )

    crescimento = crescimento_base * (1 + choque_crescimento * 0.10)

    mortalidade = mortalidade_base * (
        1 + choque_mortalidade * 0.15
    )

    preco = 1.0 + (choque_crescimento * 0.05)

    produtividade = crescimento * 0.9

    return ResultadoCholesky(
        crescimento=float(crescimento),
        mortalidade=float(mortalidade),
        preco=float(preco),
        produtividade=float(produtividade),
    )
