from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoEconomico:
    receita_total: float
    custo_total: float
    vpl: float
    valor_medio_ponderado_ton: float
    idade_rotacao: int


class ErroEconomico(Exception):
    pass



def calcular_valor_medio_ponderado(
    toneladas: list[float],
    valores_ton: list[float],
) -> float:
    """
    Calcula valor médio ponderado.

    A ponderação usa participação mássica.
    """

    if len(toneladas) != len(valores_ton):
        raise ErroEconomico(
            "Listas incompatíveis."
        )

    total_ton = sum(toneladas)

    if total_ton <= 0:
        return 0.0

    receita = sum(
        ton * valor
        for ton, valor in zip(toneladas, valores_ton)
    )

    return receita / total_ton



def calcular_vpl(
    fluxo_caixa: list[float],
    taxa_desconto: float,
) -> float:
    """
    Calcula Valor Presente Líquido.
    """

    vpl = 0.0

    for periodo, valor in enumerate(fluxo_caixa):
        vpl += valor / ((1 + taxa_desconto) ** periodo)

    return vpl



def avaliar_rotacao_economica(
    receita_total: float,
    custo_total: float,
    fluxo_caixa: list[float],
    taxa_desconto: float,
    toneladas: list[float],
    valores_ton: list[float],
    idade_rotacao: int,
) -> ResultadoEconomico:
    """
    Primeira camada de avaliação econômica.

    Futuramente:
    - carbono;
    - multiobjetivo;
    - risco;
    - Monte Carlo.
    """

    vpl = calcular_vpl(
        fluxo_caixa=fluxo_caixa,
        taxa_desconto=taxa_desconto,
    )

    valor_ponderado = calcular_valor_medio_ponderado(
        toneladas=toneladas,
        valores_ton=valores_ton,
    )

    return ResultadoEconomico(
        receita_total=float(receita_total),
        custo_total=float(custo_total),
        vpl=float(vpl),
        valor_medio_ponderado_ton=float(valor_ponderado),
        idade_rotacao=idade_rotacao,
    )
