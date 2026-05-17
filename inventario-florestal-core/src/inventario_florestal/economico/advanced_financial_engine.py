from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.economico.financial_engine import (
    FluxoCaixaAno,
)


@dataclass(frozen=True)
class ResultadoFinanceiroAvancado:
    tir: float
    vet: float


class ErroFinanceiroAvancado(Exception):
    pass



def calcular_tir(
    fluxo_caixa: list[FluxoCaixaAno],
    taxa_inicial: float = 0.08,
    tolerancia: float = 1e-7,
    max_iteracoes: int = 500,
) -> float:
    """Calcula Taxa Interna de Retorno usando Newton-Raphson."""

    taxa = taxa_inicial

    for _ in range(max_iteracoes):
        vpl = 0.0
        derivada = 0.0

        for item in fluxo_caixa:
            fator = (1 + taxa) ** item.ano

            vpl += item.saldo / fator

            derivada -= (
                item.ano * item.saldo
            ) / ((1 + taxa) ** (item.ano + 1))

        if abs(derivada) < tolerancia:
            raise ErroFinanceiroAvancado(
                "Derivada muito pequena para TIR."
            )

        nova_taxa = taxa - (vpl / derivada)

        if abs(nova_taxa - taxa) < tolerancia:
            return float(nova_taxa)

        taxa = nova_taxa

    raise ErroFinanceiroAvancado(
        "TIR nao convergiu."
    )



def calcular_vet(
    vul: float,
    taxa_juros: float,
) -> float:
    """Calcula Valor Esperado da Terra (Faustmann)."""

    if taxa_juros <= 0:
        raise ErroFinanceiroAvancado(
            "Taxa de juros invalida para VET."
        )

    return float(vul / taxa_juros)
