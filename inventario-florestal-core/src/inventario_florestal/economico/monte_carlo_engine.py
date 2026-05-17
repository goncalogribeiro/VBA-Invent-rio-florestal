from __future__ import annotations

from dataclasses import dataclass
import random
import statistics

from inventario_florestal.economico.financial_engine import (
    FluxoCaixaAno,
    consolidar_resultado_financeiro,
)


@dataclass(frozen=True)
class ResultadoMonteCarlo:
    vpl_medio: float
    vpl_minimo: float
    vpl_maximo: float
    desvio_padrao: float
    probabilidade_vpl_negativo: float
    simulacoes: int


class ErroMonteCarlo(Exception):
    pass



def gerar_fator_aleatorio(
    media: float = 1.0,
    desvio: float = 0.15,
) -> float:
    fator = random.normalvariate(media, desvio)

    return max(fator, 0.01)



def simular_fluxo_caixa(
    fluxo_base: list[FluxoCaixaAno],
    desvio_receita: float,
) -> list[FluxoCaixaAno]:
    fluxo_simulado: list[FluxoCaixaAno] = []

    for item in fluxo_base:
        fator = gerar_fator_aleatorio(
            media=1.0,
            desvio=desvio_receita,
        )

        nova_receita = item.receita * fator

        fluxo_simulado.append(
            FluxoCaixaAno(
                ano=item.ano,
                receita=float(nova_receita),
                custo=float(item.custo),
                saldo=float(nova_receita - item.custo),
            )
        )

    return fluxo_simulado



def executar_monte_carlo(
    fluxo_base: list[FluxoCaixaAno],
    taxa_juros: float,
    simulacoes: int = 1000,
    desvio_receita: float = 0.15,
) -> ResultadoMonteCarlo:
    """Executa simulação Monte Carlo sobre receitas futuras."""

    if simulacoes <= 0:
        raise ErroMonteCarlo(
            "Numero de simulacoes invalido."
        )

    vpls: list[float] = []

    for _ in range(simulacoes):
        fluxo_simulado = simular_fluxo_caixa(
            fluxo_base=fluxo_base,
            desvio_receita=desvio_receita,
        )

        resultado = consolidar_resultado_financeiro(
            fluxo_caixa=fluxo_simulado,
            taxa_juros=taxa_juros,
        )

        vpls.append(resultado.vpl)

    vpl_medio = statistics.mean(vpls)
    vpl_minimo = min(vpls)
    vpl_maximo = max(vpls)

    desvio_padrao = statistics.pstdev(vpls)

    vpls_negativos = [x for x in vpls if x < 0]

    probabilidade_negativa = (
        len(vpls_negativos) / simulacoes
    ) * 100

    return ResultadoMonteCarlo(
        vpl_medio=float(vpl_medio),
        vpl_minimo=float(vpl_minimo),
        vpl_maximo=float(vpl_maximo),
        desvio_padrao=float(desvio_padrao),
        probabilidade_vpl_negativo=float(probabilidade_negativa),
        simulacoes=int(simulacoes),
    )
