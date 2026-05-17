from __future__ import annotations

from dataclasses import dataclass
from random import uniform


@dataclass(frozen=True)
class ArvoreSintetica:
    id_arvore: int
    parcela: int
    dap_cm: float
    altura_m: float
    idade: int
    x: float
    y: float



def gerar_arvore_sintetica(
    identificador: int,
    parcela: int,
    dap_min: float,
    dap_max: float,
    altura_min: float,
    altura_max: float,
    idade: int,
) -> ArvoreSintetica:
    """
    Gera árvore sintética controlada.
    """

    return ArvoreSintetica(
        id_arvore=identificador,
        parcela=parcela,
        dap_cm=uniform(dap_min, dap_max),
        altura_m=uniform(altura_min, altura_max),
        idade=idade,
        x=uniform(0, 50),
        y=uniform(0, 50),
    )



def gerar_dataset_sintetico(
    numero_arvores: int,
    parcela: int = 1,
    idade: int = 8,
    dap_min: float = 8,
    dap_max: float = 35,
    altura_min: float = 8,
    altura_max: float = 30,
) -> list[ArvoreSintetica]:
    """
    Gera dataset sintético inicial.
    """

    return [
        gerar_arvore_sintetica(
            identificador=i,
            parcela=parcela,
            dap_min=dap_min,
            dap_max=dap_max,
            altura_min=altura_min,
            altura_max=altura_max,
            idade=idade,
        )
        for i in range(1, numero_arvores + 1)
    ]
