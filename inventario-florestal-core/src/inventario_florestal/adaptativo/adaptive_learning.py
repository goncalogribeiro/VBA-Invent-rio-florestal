from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoAprendizado:
    valor_observado: float
    valor_projetado: float
    erro_absoluto: float
    erro_percentual: float
    ajuste_recomendado: float


class ErroAprendizado(Exception):
    pass



def calcular_erro_percentual(
    observado: float,
    projetado: float,
) -> float:
    """
    Calcula erro percentual relativo.
    """

    if observado == 0:
        raise ErroAprendizado(
            "Valor observado não pode ser zero."
        )

    return (
        (projetado - observado)
        / observado
    ) * 100



def avaliar_aprendizado(
    observado: float,
    projetado: float,
) -> ResultadoAprendizado:
    """
    Primeira camada adaptativa.

    Futuramente:
    - autoajuste;
    - IA;
    - machine learning;
    - calibração automática.
    """

    erro_abs = abs(projetado - observado)

    erro_pct = calcular_erro_percentual(
        observado=observado,
        projetado=projetado,
    )

    ajuste = 1 - (erro_pct / 100)

    return ResultadoAprendizado(
        valor_observado=float(observado),
        valor_projetado=float(projetado),
        erro_absoluto=float(erro_abs),
        erro_percentual=float(erro_pct),
        ajuste_recomendado=float(ajuste),
    )
