from __future__ import annotations

from dataclasses import dataclass
from random import gauss
from statistics import mean, pstdev


@dataclass(frozen=True)
class ResultadoMonteCarlo:
    media: float
    desvio_padrao: float
    minimo: float
    maximo: float
    simulacoes: int


class ErroMonteCarlo(Exception):
    pass



def simular_preco(
    preco_base: float,
    volatilidade_percentual: float,
) -> float:
    """
    Simula preço com distribuição normal simplificada.
    """

    sigma = preco_base * (volatilidade_percentual / 100)

    return gauss(preco_base, sigma)



def executar_monte_carlo(
    preco_base: float,
    volatilidade_percentual: float,
    n_simulacoes: int = 1000,
) -> ResultadoMonteCarlo:
    """
    Primeira camada Monte Carlo.

    Futuramente:
    - múltiplas variáveis;
    - correlação;
    - clima;
    - crescimento;
    - mortalidade;
    - carbono.
    """

    if n_simulacoes <= 0:
        raise ErroMonteCarlo(
            "Número de simulações inválido."
        )

    resultados = [
        simular_preco(
            preco_base=preco_base,
            volatilidade_percentual=volatilidade_percentual,
        )
        for _ in range(n_simulacoes)
    ]

    return ResultadoMonteCarlo(
        media=float(mean(resultados)),
        desvio_padrao=float(pstdev(resultados)),
        minimo=float(min(resultados)),
        maximo=float(max(resultados)),
        simulacoes=n_simulacoes,
    )
