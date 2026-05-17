from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev


@dataclass(frozen=True)
class ResultadoRisco:
    media: float
    desvio_padrao: float
    valor_minimo: float
    valor_maximo: float
    amplitude: float
    n_simulacoes: int


class ErroRisco(Exception):
    pass



def analisar_resultados(
    resultados: list[float],
) -> ResultadoRisco:
    """
    Primeira camada de análise de risco.

    Futuramente:
    - Monte Carlo completo;
    - percentis;
    - VaR;
    - CVaR;
    - distribuições probabilísticas.
    """

    if not resultados:
        raise ErroRisco(
            "Lista de resultados vazia."
        )

    media = mean(resultados)

    desvio = (
        pstdev(resultados)
        if len(resultados) > 1
        else 0.0
    )

    minimo = min(resultados)
    maximo = max(resultados)

    return ResultadoRisco(
        media=float(media),
        desvio_padrao=float(desvio),
        valor_minimo=float(minimo),
        valor_maximo=float(maximo),
        amplitude=float(maximo - minimo),
        n_simulacoes=len(resultados),
    )
