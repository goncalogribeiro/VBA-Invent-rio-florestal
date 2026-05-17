"""Motor universal de ranking biometrico.

A pontuacao sintetica nao substitui a analise tecnica, mas permite ordenar
modelos em um torneio automatizado considerando ajuste, erro, vies e
estabilidade residual.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoRanking:
    """Resultado resumido de um torneio biometrico."""

    modelo_id: str
    pontuacao: float
    metricas: dict[str, float]
    aic: float | None = None
    bic: float | None = None
    observacoes: list[str] | None = None



def _normalizar_penalizacao(
    valor: float,
    escala: float = 100.0,
) -> float:
    """Normaliza penalizacoes para reduzir dominancia numerica."""

    return valor / (abs(valor) + escala)



def calcular_pontuacao_padrao(
    metricas: dict[str, float],
    pesos: dict[str, float] | None = None,
) -> float:
    """Calcula pontuacao sintetica para ranking biometrico robusto.

    O criterio principal continua sendo R² ajustado.

    Penalizacoes adicionais sao aplicadas para:

    - erro residual;
    - PRESS;
    - residuos extremos;
    - observacoes influentes.
    """

    pesos_padrao = {
        "r2_ajustado": 0.55,
        "syx_percentual": -0.20,
        "bias": -0.10,
        "press_rmse": -0.05,
        "media_abs_residuos_percentuais": -0.05,
        "max_abs_residuo_percentual": -0.02,
        "max_cook_distance": -0.02,
        "n_observacoes_influentes": -0.01,
    }

    pesos_utilizados = pesos or pesos_padrao

    score = 0.0

    for chave, peso in pesos_utilizados.items():
        valor = float(metricas.get(chave, 0.0))

        if chave == "bias":
            valor = abs(valor)

        if peso < 0:
            valor = _normalizar_penalizacao(valor)

        score += valor * peso

    return float(score)



def combinar_metricas_com_diagnostico(
    metricas: dict[str, float],
    diagnostico: object | None,
) -> dict[str, float]:
    """Combina metricas do ajuste com indicadores residuais."""

    combinadas = dict(metricas)

    if diagnostico is None:
        return combinadas

    for atributo in (
        "press",
        "press_rmse",
        "media_residuos",
        "media_abs_residuos_percentuais",
        "max_abs_residuo_percentual",
        "max_cook_distance",
        "n_observacoes_influentes",
    ):
        if hasattr(diagnostico, atributo):
            valor = getattr(diagnostico, atributo)

            if valor is not None:
                combinadas[atributo] = float(valor)

    return combinadas
