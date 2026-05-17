from __future__ import annotations

from dataclasses import dataclass
from random import gauss


@dataclass(frozen=True)
class VariavelCorrelacionada:
    nome: str
    valor_base: float
    volatilidade_percentual: float
    correlacao: float


@dataclass(frozen=True)
class ResultadoCenarioCorrelacionado:
    crescimento: float
    mortalidade: float
    preco: float
    produtividade: float


class ErroCorrelacao(Exception):
    pass



def aplicar_choque_correlacionado(
    valor_base: float,
    volatilidade_percentual: float,
    choque_base: float,
    correlacao: float,
) -> float:
    """
    Primeira aproximação de variável correlacionada.

    Implementação simplificada.
    """

    ruido_independente = gauss(0, 1)

    choque = (
        correlacao * choque_base
        + (1 - abs(correlacao)) * ruido_independente
    )

    fator = 1 + (
        choque * volatilidade_percentual / 100
    )

    return valor_base * fator



def gerar_cenario_correlacionado(
    crescimento_base: float,
    mortalidade_base: float,
    preco_base: float,
    produtividade_base: float,
) -> ResultadoCenarioCorrelacionado:
    """
    Primeira camada de cenário multivariado correlacionado.

    Futuramente:
    - matrizes de covariância;
    - Cholesky;
    - séries históricas;
    - clima;
    - IA.
    """

    choque_global = gauss(0, 1)

    crescimento = aplicar_choque_correlacionado(
        valor_base=crescimento_base,
        volatilidade_percentual=10,
        choque_base=choque_global,
        correlacao=0.75,
    )

    mortalidade = aplicar_choque_correlacionado(
        valor_base=mortalidade_base,
        volatilidade_percentual=15,
        choque_base=choque_global,
        correlacao=-0.65,
    )

    preco = aplicar_choque_correlacionado(
        valor_base=preco_base,
        volatilidade_percentual=20,
        choque_base=choque_global,
        correlacao=0.40,
    )

    produtividade = aplicar_choque_correlacionado(
        valor_base=produtividade_base,
        volatilidade_percentual=12,
        choque_base=choque_global,
        correlacao=0.80,
    )

    return ResultadoCenarioCorrelacionado(
        crescimento=float(crescimento),
        mortalidade=float(mortalidade),
        preco=float(preco),
        produtividade=float(produtividade),
    )
