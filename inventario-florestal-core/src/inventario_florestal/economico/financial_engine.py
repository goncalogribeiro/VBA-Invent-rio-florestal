from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FluxoCaixaAno:
    ano: int
    receita: float
    custo: float
    saldo: float


@dataclass(frozen=True)
class ResultadoFinanceiro:
    vpl: float
    relacao_bc: float
    receita_total: float
    custo_total: float
    fluxo_caixa: list[FluxoCaixaAno]


class ErroFinanceiro(Exception):
    pass



def calcular_vpl(
    fluxo_caixa: list[FluxoCaixaAno],
    taxa_juros: float,
) -> float:
    """Calcula Valor Presente Liquido."""

    vpl = 0.0

    for item in fluxo_caixa:
        vpl += item.saldo / ((1 + taxa_juros) ** item.ano)

    return float(vpl)



def calcular_relacao_bc(
    fluxo_caixa: list[FluxoCaixaAno],
    taxa_juros: float,
) -> float:
    """Calcula relacao beneficio custo."""

    beneficios = 0.0
    custos = 0.0

    for item in fluxo_caixa:
        beneficios += (
            item.receita / ((1 + taxa_juros) ** item.ano)
        )

        custos += (
            item.custo / ((1 + taxa_juros) ** item.ano)
        )

    if custos <= 0:
        raise ErroFinanceiro(
            "Custos invalidos para relacao B/C."
        )

    return float(beneficios / custos)



def consolidar_resultado_financeiro(
    fluxo_caixa: list[FluxoCaixaAno],
    taxa_juros: float,
) -> ResultadoFinanceiro:
    receita_total = sum(x.receita for x in fluxo_caixa)
    custo_total = sum(x.custo for x in fluxo_caixa)

    vpl = calcular_vpl(
        fluxo_caixa=fluxo_caixa,
        taxa_juros=taxa_juros,
    )

    relacao_bc = calcular_relacao_bc(
        fluxo_caixa=fluxo_caixa,
        taxa_juros=taxa_juros,
    )

    return ResultadoFinanceiro(
        vpl=float(vpl),
        relacao_bc=float(relacao_bc),
        receita_total=float(receita_total),
        custo_total=float(custo_total),
        fluxo_caixa=fluxo_caixa,
    )
