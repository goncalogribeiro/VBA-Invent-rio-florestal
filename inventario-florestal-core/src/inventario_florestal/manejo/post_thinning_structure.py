from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.manejo.events import EventoManejo
from inventario_florestal.manejo.thinning_engine import (
    EstadoPovoamento,
    ResultadoDesbaste,
)


@dataclass(frozen=True)
class EstruturaPosDesbaste:
    """Estrutura biométrica remanescente após desbaste."""

    n: float
    g: float
    dg: float
    hd: float


class ErroRedistribuicaoEstrutural(Exception):
    pass



def recalcular_estrutura_pos_desbaste(
    estado_original: EstadoPovoamento,
    resultado_desbaste: ResultadoDesbaste,
    evento: EventoManejo,
) -> EstruturaPosDesbaste:
    """
    Recalcula estrutura biométrica simplificada.

    Primeira implementação:
    - recalcula N;
    - recalcula G;
    - ajusta Dg empiricamente;
    - mantém Hd constante.

    Ainda NÃO:
    - recalcula Weibull;
    - recalcula taper;
    - recalcula prognose.
    """

    n_novo = resultado_desbaste.remanescente_n
    g_novo = resultado_desbaste.remanescente_g

    intensidade = evento.intensidade

    dg_original = estado_original.dg

    if evento.tipo == "desbaste_por_baixo":
        fator_dg = 1 + (0.12 * intensidade)

    elif evento.tipo == "desbaste_pelo_alto":
        fator_dg = 1 + (0.03 * intensidade)

    elif evento.tipo == "desbaste_sistematico":
        fator_dg = 1 + (0.01 * intensidade)

    elif evento.tipo == "desbaste_misto":
        fator_dg = 1 + (0.06 * intensidade)

    else:
        fator_dg = 1.0

    dg_novo = dg_original * fator_dg

    if dg_novo <= 0:
        raise ErroRedistribuicaoEstrutural(
            "Dg pós-desbaste inválido."
        )

    return EstruturaPosDesbaste(
        n=float(n_novo),
        g=float(g_novo),
        dg=float(dg_novo),
        hd=float(estado_original.hd),
    )
