from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EventoFluxoCaixa:
    ano: int
    descricao: str
    valor: float


@dataclass(frozen=True)
class ResultadoFluxoCaixa:
    fluxo_total: float
    receita_total: float
    custo_total: float
    eventos: list[EventoFluxoCaixa]


class ErroFluxoCaixa(Exception):
    pass



def calcular_fluxo_caixa(
    receitas: list[EventoFluxoCaixa],
    custos: list[EventoFluxoCaixa],
) -> ResultadoFluxoCaixa:
    """
    Primeira camada de fluxo econômico temporal.

    Futuramente:
    - inflação;
    - juros variáveis;
    - risco;
    - Monte Carlo;
    - carbono.
    """

    eventos = [*receitas, *custos]

    receita_total = sum(
        evento.valor
        for evento in receitas
    )

    custo_total = sum(
        evento.valor
        for evento in custos
    )

    fluxo_total = receita_total - custo_total

    return ResultadoFluxoCaixa(
        fluxo_total=float(fluxo_total),
        receita_total=float(receita_total),
        custo_total=float(custo_total),
        eventos=sorted(eventos, key=lambda e: e.ano),
    )



def criar_evento_receita(
    ano: int,
    descricao: str,
    valor: float,
) -> EventoFluxoCaixa:
    return EventoFluxoCaixa(
        ano=ano,
        descricao=descricao,
        valor=abs(valor),
    )



def criar_evento_custo(
    ano: int,
    descricao: str,
    valor: float,
) -> EventoFluxoCaixa:
    return EventoFluxoCaixa(
        ano=ano,
        descricao=descricao,
        valor=-abs(valor),
    )
