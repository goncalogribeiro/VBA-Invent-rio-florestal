from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.manejo.events import EventoManejo


@dataclass(frozen=True)
class EstadoPovoamento:
    """Estado simplificado do povoamento."""

    n: float
    g: float
    dg: float
    hd: float


@dataclass(frozen=True)
class ResultadoDesbaste:
    """Resultado simplificado do desbaste."""

    removido_n: float
    removido_g: float
    remanescente_n: float
    remanescente_g: float
    intensidade_aplicada: float


class ErroAplicacaoDesbaste(Exception):
    pass



def aplicar_desbaste_sistematico(
    estado: EstadoPovoamento,
    evento: EventoManejo,
) -> ResultadoDesbaste:
    """
    Aplica desbaste sistemático simplificado.

    Nesta primeira versão:
    - remove proporcionalmente N e G;
    - NÃO recalcula Weibull;
    - NÃO recalcula Dg;
    - NÃO recalcula Hd.

    Esta implementação existe apenas como camada estrutural inicial.
    """

    if evento.tipo not in {
        "desbaste_sistematico",
        "desbaste_misto",
    }:
        raise ErroAplicacaoDesbaste(
            "Evento incompatível com desbaste sistemático."
        )

    intensidade = evento.intensidade

    removido_n = estado.n * intensidade
    removido_g = estado.g * intensidade

    remanescente_n = estado.n - removido_n
    remanescente_g = estado.g - removido_g

    return ResultadoDesbaste(
        removido_n=float(removido_n),
        removido_g=float(removido_g),
        remanescente_n=float(remanescente_n),
        remanescente_g=float(remanescente_g),
        intensidade_aplicada=float(intensidade),
    )
