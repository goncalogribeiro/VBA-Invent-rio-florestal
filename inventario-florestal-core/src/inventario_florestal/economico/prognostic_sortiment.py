from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.taper.prognostic_taper import (
    ResultadoTaperClasse,
)


@dataclass(frozen=True)
class ItemSortimentoProjetado:
    sortimento: str
    volume_m3: float
    massa_ton: float
    valor_total: float
    valor_medio_ton: float


@dataclass(frozen=True)
class ResultadoSortimentoProjetado:
    itens: list[ItemSortimentoProjetado]
    volume_total_m3: float
    massa_total_ton: float
    receita_total: float
    valor_medio_ponderado_ton: float


class ErroSortimentoProjetado(Exception):
    pass



def consolidar_sortimento_prognostico(
    resultados_taper: list[ResultadoTaperClasse],
    conversao_m3_ton: float,
    precos_ton: dict[str, float],
) -> ResultadoSortimentoProjetado:
    """Consolida volume, massa e receita por sortimento.

    O valor medio geral por tonelada e calculado por media ponderada:

    valor_medio_ponderado = receita_total / massa_total

    Isso evita media simples entre sortimentos com massas diferentes.
    """

    acumulado: dict[str, dict[str, float]] = {}

    for resultado in resultados_taper:
        for tora in resultado.toras:
            if tora.sortimento not in acumulado:
                acumulado[tora.sortimento] = {
                    "volume": 0.0,
                    "massa": 0.0,
                    "receita": 0.0,
                }

            volume_ha = tora.volume_m3 * resultado.arvores_ha
            massa = volume_ha * conversao_m3_ton
            preco = precos_ton.get(tora.sortimento, 0.0)
            receita = massa * preco

            acumulado[tora.sortimento]["volume"] += volume_ha
            acumulado[tora.sortimento]["massa"] += massa
            acumulado[tora.sortimento]["receita"] += receita

    itens: list[ItemSortimentoProjetado] = []

    volume_total = 0.0
    massa_total = 0.0
    receita_total = 0.0

    for sortimento, valores in acumulado.items():
        massa = valores["massa"]
        receita = valores["receita"]
        valor_medio = receita / massa if massa > 0 else 0.0

        item = ItemSortimentoProjetado(
            sortimento=sortimento,
            volume_m3=float(valores["volume"]),
            massa_ton=float(massa),
            valor_total=float(receita),
            valor_medio_ton=float(valor_medio),
        )

        itens.append(item)

        volume_total += valores["volume"]
        massa_total += massa
        receita_total += receita

    itens.sort(
        key=lambda x: x.valor_total,
        reverse=True,
    )

    valor_medio_ponderado = (
        receita_total / massa_total if massa_total > 0 else 0.0
    )

    return ResultadoSortimentoProjetado(
        itens=itens,
        volume_total_m3=float(volume_total),
        massa_total_ton=float(massa_total),
        receita_total=float(receita_total),
        valor_medio_ponderado_ton=float(valor_medio_ponderado),
    )
