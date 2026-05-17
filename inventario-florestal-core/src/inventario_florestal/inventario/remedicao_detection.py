from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class InventarioMetadata:
    projeto: str
    talhao: str
    parcela: str | None
    data_inventario: date
    data_plantio: date | None
    area_ha: float | None


@dataclass(frozen=True)
class ResultadoDeteccaoRemedicao:
    possivel_remedicao: bool
    score: float
    motivos: list[str]



def detectar_possivel_remedicao(
    atual: InventarioMetadata,
    anterior: InventarioMetadata,
) -> ResultadoDeteccaoRemedicao:
    """
    Detecta possível remedição entre inventários.

    Primeira implementação baseada em regras.
    """

    score = 0.0
    motivos: list[str] = []

    if atual.projeto == anterior.projeto:
        score += 0.35
        motivos.append("mesmo_projeto")

    if atual.talhao == anterior.talhao:
        score += 0.30
        motivos.append("mesmo_talhao")

    if (
        atual.parcela is not None
        and anterior.parcela is not None
        and atual.parcela == anterior.parcela
    ):
        score += 0.20
        motivos.append("mesma_parcela")

    if (
        atual.data_plantio is not None
        and anterior.data_plantio is not None
        and atual.data_plantio == anterior.data_plantio
    ):
        score += 0.10
        motivos.append("mesma_data_plantio")

    if atual.data_inventario > anterior.data_inventario:
        score += 0.05
        motivos.append("sequencia_temporal")

    return ResultadoDeteccaoRemedicao(
        possivel_remedicao=score >= 0.60,
        score=score,
        motivos=motivos,
    )
