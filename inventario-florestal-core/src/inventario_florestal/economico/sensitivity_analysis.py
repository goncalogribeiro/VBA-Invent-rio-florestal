from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.economico.financial_engine import (
    FluxoCaixaAno,
    consolidar_resultado_financeiro,
)


@dataclass(frozen=True)
class ResultadoSensibilidade:
    nome_cenario: str
    fator_variacao: float
    vpl: float
    relacao_bc: float


class ErroSensibilidade(Exception):
    pass



def aplicar_variacao_receita(
    fluxo_caixa: list[FluxoCaixaAno],
    fator: float,
) -> list[FluxoCaixaAno]:
    fluxo_ajustado: list[FluxoCaixaAno] = []

    for item in fluxo_caixa:
        nova_receita = item.receita * fator

        fluxo_ajustado.append(
            FluxoCaixaAno(
                ano=item.ano,
                receita=float(nova_receita),
                custo=float(item.custo),
                saldo=float(nova_receita - item.custo),
            )
        )

    return fluxo_ajustado



def executar_analise_sensibilidade(
    fluxo_caixa_base: list[FluxoCaixaAno],
    taxa_juros: float,
    variacoes: list[tuple[str, float]],
) -> list[ResultadoSensibilidade]:
    """Executa análise de sensibilidade sobre receitas.

    Exemplo:
        variacoes = [
            ("-20%", 0.8),
            ("base", 1.0),
            ("+20%", 1.2),
        ]
    """

    resultados: list[ResultadoSensibilidade] = []

    for nome, fator in variacoes:
        fluxo_variado = aplicar_variacao_receita(
            fluxo_caixa=fluxo_caixa_base,
            fator=fator,
        )

        resultado = consolidar_resultado_financeiro(
            fluxo_caixa=fluxo_variado,
            taxa_juros=taxa_juros,
        )

        resultados.append(
            ResultadoSensibilidade(
                nome_cenario=nome,
                fator_variacao=float(fator),
                vpl=float(resultado.vpl),
                relacao_bc=float(resultado.relacao_bc),
            )
        )

    return resultados
