from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


TipoEventoManejo = Literal[
    "desbaste_sistematico",
    "desbaste_por_baixo",
    "desbaste_pelo_alto",
    "desbaste_misto",
    "desbaste_sanitario",
    "corte_final",
]

CriterioRemocao = Literal[
    "arvores",
    "area_basal",
    "volume",
    "classe_diametrica",
]


@dataclass(frozen=True)
class EventoManejo:
    """Evento temporal de manejo silvicultural."""

    idade: float
    tipo: TipoEventoManejo
    intensidade: float
    criterio_remocao: CriterioRemocao = "arvores"
    cenario_operacional: str | None = None
    observacoes: list[str] = field(default_factory=list)

    def validar(self) -> None:
        if self.idade <= 0:
            raise ValueError("Idade do evento deve ser positiva.")

        if self.tipo == "corte_final":
            if self.intensidade != 1.0:
                raise ValueError(
                    "Evento corte_final deve possuir intensidade igual a 1.0."
                )
            return

        if self.intensidade <= 0 or self.intensidade >= 1:
            raise ValueError(
                "Intensidade de desbaste deve estar entre 0 e 1."
            )


@dataclass(frozen=True)
class RegimeManejoTemporal:
    """Sequencia ordenada de eventos de manejo."""

    nome: str
    eventos: list[EventoManejo]
    descricao: str | None = None

    def validar(self) -> None:
        if not self.eventos:
            raise ValueError("Regime deve possuir pelo menos um evento.")

        idades = [evento.idade for evento in self.eventos]

        if idades != sorted(idades):
            raise ValueError("Eventos de manejo devem estar em ordem cronologica.")

        for evento in self.eventos:
            evento.validar()

        cortes = [evento for evento in self.eventos if evento.tipo == "corte_final"]

        if len(cortes) != 1:
            raise ValueError("Regime deve possuir exatamente um corte_final.")

        if self.eventos[-1].tipo != "corte_final":
            raise ValueError("O corte_final deve ser o ultimo evento do regime.")


class ErroManejoTemporal(Exception):
    pass



def criar_regime_temporal(
    nome: str,
    eventos: list[EventoManejo],
    descricao: str | None = None,
) -> RegimeManejoTemporal:
    regime = RegimeManejoTemporal(
        nome=nome,
        eventos=eventos,
        descricao=descricao,
    )

    try:
        regime.validar()
    except ValueError as exc:
        raise ErroManejoTemporal(str(exc)) from exc

    return regime
