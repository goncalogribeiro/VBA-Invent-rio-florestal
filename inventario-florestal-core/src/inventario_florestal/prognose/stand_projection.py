from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class EstadoPovoamento:
    idade: float
    n_arvores_ha: float
    area_basal: float
    dap_medio: float
    altura_dominante: float
    indice_sitio: float | None = None


@dataclass(frozen=True)
class ResultadoPrognoseEstrutural:
    estado_inicial: EstadoPovoamento
    estado_futuro: EstadoPovoamento
    delta_idade: float
    modelo_sobrevivencia: str
    modelo_area_basal: str


class ErroPrognoseEstrutural(Exception):
    pass



def prognose_clutter_basica(
    estado: EstadoPovoamento,
    idade_futura: float,
    beta_n: tuple[float, float, float],
    beta_g: tuple[float, float, float],
) -> ResultadoPrognoseEstrutural:
    if idade_futura <= estado.idade:
        raise ErroPrognoseEstrutural(
            "Idade futura deve ser maior que a idade atual."
        )

    if estado.indice_sitio is None:
        raise ErroPrognoseEstrutural(
            "Indice de sitio obrigatorio para prognose estrutural."
        )

    i1 = estado.idade
    i2 = idade_futura
    s = estado.indice_sitio

    b0_n, b1_n, b2_n = beta_n

    n2 = estado.n_arvores_ha * ((i2 / i1) ** b1_n) * math.exp(
        (b0_n + b2_n * s) * (i2 - i1)
    )

    b0_g, b1_g, b2_g = beta_g

    ln_g2 = (
        b0_g
        + math.log(max(estado.area_basal, 1e-9)) * (i1 / i2)
        + b1_g * (1 - i1 / i2)
        + b2_g * (1 - i1 / i2) * s
    )

    g2 = math.exp(ln_g2)

    dg2 = math.sqrt((40000 * g2) / (math.pi * max(n2, 1e-9)))

    hd2 = estado.altura_dominante * ((i2 / i1) ** 0.25)

    estado_futuro = EstadoPovoamento(
        idade=float(i2),
        n_arvores_ha=float(n2),
        area_basal=float(g2),
        dap_medio=float(dg2),
        altura_dominante=float(hd2),
        indice_sitio=float(s),
    )

    return ResultadoPrognoseEstrutural(
        estado_inicial=estado,
        estado_futuro=estado_futuro,
        delta_idade=float(i2 - i1),
        modelo_sobrevivencia="Clutter (1970)",
        modelo_area_basal="Clutter (1970)",
    )
