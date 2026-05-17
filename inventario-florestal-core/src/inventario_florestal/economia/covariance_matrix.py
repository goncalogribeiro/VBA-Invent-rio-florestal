from __future__ import annotations

from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class ResultadoCovariancia:
    matriz_covariancia: list[list[float]]
    medias: list[float]
    variaveis: list[str]


class ErroCovariancia(Exception):
    pass



def calcular_covariancia(
    x: list[float],
    y: list[float],
) -> float:
    """
    Calcula covariância amostral.
    """

    if len(x) != len(y):
        raise ErroCovariancia(
            "Vetores incompatíveis."
        )

    if len(x) < 2:
        raise ErroCovariancia(
            "Número insuficiente de observações."
        )

    mx = mean(x)
    my = mean(y)

    soma = sum(
        (xi - mx) * (yi - my)
        for xi, yi in zip(x, y)
    )

    return soma / (len(x) - 1)



def construir_matriz_covariancia(
    dados: dict[str, list[float]],
) -> ResultadoCovariancia:
    """
    Primeira camada de matriz NxN.

    Futuramente:
    - matrizes históricas reais;
    - clima;
    - preços;
    - mortalidade;
    - séries temporais.
    """

    variaveis = list(dados.keys())

    matriz: list[list[float]] = []

    for var_i in variaveis:
        linha = []

        for var_j in variaveis:
            cov = calcular_covariancia(
                dados[var_i],
                dados[var_j],
            )

            linha.append(float(cov))

        matriz.append(linha)

    medias = [
        float(mean(dados[var]))
        for var in variaveis
    ]

    return ResultadoCovariancia(
        matriz_covariancia=matriz,
        medias=medias,
        variaveis=variaveis,
    )
