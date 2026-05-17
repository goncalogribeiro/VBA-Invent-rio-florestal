from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RegistroTemporal:
    entidade: str
    identificador: str
    valor: float
    data_medicao: datetime
    origem: str


@dataclass
class BancoTemporal:
    registros: list[RegistroTemporal] = field(default_factory=list)

    def adicionar_registro(
        self,
        registro: RegistroTemporal,
    ) -> None:
        self.registros.append(registro)

    def buscar_registros(
        self,
        entidade: str,
        identificador: str,
    ) -> list[RegistroTemporal]:
        return [
            r
            for r in self.registros
            if r.entidade == entidade
            and r.identificador == identificador
        ]


class ErroRepositorioTemporal(Exception):
    pass



def comparar_medicoes(
    historico: list[RegistroTemporal],
) -> dict[str, float]:
    """
    Primeira camada temporal.

    Futuramente:
    - banco persistente;
    - SQL;
    - séries temporais;
    - autoajuste;
    - machine learning.
    """

    if len(historico) < 2:
        raise ErroRepositorioTemporal(
            "Histórico insuficiente."
        )

    historico_ordenado = sorted(
        historico,
        key=lambda r: r.data_medicao,
    )

    inicial = historico_ordenado[0]
    final = historico_ordenado[-1]

    variacao = final.valor - inicial.valor

    percentual = (
        (variacao / inicial.valor) * 100
        if inicial.valor != 0
        else 0.0
    )

    return {
        "valor_inicial": float(inicial.valor),
        "valor_final": float(final.valor),
        "variacao": float(variacao),
        "variacao_percentual": float(percentual),
    }
