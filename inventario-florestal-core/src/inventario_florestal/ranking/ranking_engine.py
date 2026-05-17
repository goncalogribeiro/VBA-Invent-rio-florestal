"""Motor universal de ranking biometrico."""

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



def calcular_pontuacao_padrao(
    metricas: dict[str, float],
    pesos: dict[str, float] | None = None,
) -> float:
    """Calcula pontuacao sintetica para ranking.

    A versao inicial utiliza:

    - R² ajustado como criterio positivo;
    - Syx% como criterio negativo;
    - Bias absoluto como criterio negativo.

    A estrutura sera expandida posteriormente para:

    - AIC;
    - BIC;
    - heterocedasticidade;
    - estabilidade;
    - penalizacao de complexidade;
    - extrapolacao.
    """

    pesos_padrao = {
        "r2_ajustado": 0.5,
        "syx_percentual": -0.3,
        "bias": -0.2,
    }

    pesos_utilizados = pesos or pesos_padrao

    score = 0.0

    for chave, peso in pesos_utilizados.items():
        valor = metricas.get(chave, 0.0)

        if chave == "bias":
            valor = abs(valor)

        score += valor * peso

    return float(score)
