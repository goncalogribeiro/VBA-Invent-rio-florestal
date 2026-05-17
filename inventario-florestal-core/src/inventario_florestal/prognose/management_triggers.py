from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoManejo:
    recomendar_desbaste: bool
    recomendar_corte: bool
    zona_manejo: str
    justificativas: list[str]



def verificar_culminacao(
    ica: float,
    ima: float,
    tolerancia_percentual: float = 5.0,
) -> bool:
    """
    Verifica aproximação ICA ≈ IMA.
    """

    if ima <= 0:
        return False

    diferenca = abs(ica - ima)

    percentual = (
        diferenca / ima
    ) * 100

    return percentual <= tolerancia_percentual



def avaliar_manejo(
    reineke_percentual: float,
    hart_becking_percentual: float,
    ica: float,
    ima: float,
) -> ResultadoManejo:
    """
    Primeira camada de recomendação silvicultural.

    Futuramente:
    - otimização econômica;
    - VPL;
    - carbono;
    - multiobjetivo;
    - estabilidade estrutural.
    """

    justificativas: list[str] = []

    recomendar_desbaste = False
    recomendar_corte = False

    if reineke_percentual > 45:
        recomendar_desbaste = True
        justificativas.append("alta_competicao_reineke")

    if hart_becking_percentual < 20:
        recomendar_desbaste = True
        justificativas.append("superlotacao_hart")

    if verificar_culminacao(ica, ima):
        recomendar_corte = True
        justificativas.append("culminacao_ima")

    if recomendar_corte:
        zona = "avaliar_corte"
    elif recomendar_desbaste:
        zona = "avaliar_desbaste"
    else:
        zona = "crescimento_normal"

    return ResultadoManejo(
        recomendar_desbaste=recomendar_desbaste,
        recomendar_corte=recomendar_corte,
        zona_manejo=zona,
        justificativas=justificativas,
    )
