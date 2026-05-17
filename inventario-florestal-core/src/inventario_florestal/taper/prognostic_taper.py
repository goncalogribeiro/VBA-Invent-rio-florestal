from __future__ import annotations

from dataclasses import dataclass
import math

from inventario_florestal.config.scenario_engine import (
    CenarioOperacional,
)
from inventario_florestal.weibull.weibull_distribution import (
    ClasseDiametricaWeibull,
)


@dataclass(frozen=True)
class ToraSortimento:
    comprimento: float
    diametro_ponta_fina: float
    sortimento: str
    volume_m3: float


@dataclass(frozen=True)
class ResultadoTaperClasse:
    dap_centro_classe: float
    altura_estimada: float
    arvores_ha: float
    toras: list[ToraSortimento]
    volume_total_m3_ha: float


class ErroTaperPrognostico(Exception):
    pass



def taper_generico_prognostico(
    classe: ClasseDiametricaWeibull,
    altura_estimada: float,
    fator_forma: float,
    cenario: CenarioOperacional,
) -> ResultadoTaperClasse:
    """Simula taper e sortimento usando um cenario operacional.

    O cenario define:
    - produtos;
    - comprimentos de tora;
    - diametros minimos;
    - valores comerciais.
    """

    if fator_forma <= 0 or fator_forma > 1:
        raise ErroTaperPrognostico(
            "Fator de forma invalido."
        )

    dap = classe.centro_classe

    altura_util = max(altura_estimada - 0.1, 0.0)

    if altura_util <= 0:
        raise ErroTaperPrognostico(
            "Altura util invalida."
        )

    alpha = 0.53 / fator_forma

    h_atual = 0.1

    toras: list[ToraSortimento] = []

    volume_total = 0.0

    while h_atual < altura_util:
        tora_alocada = False

        for sortimento in cenario.sortimentos:
            h_final = h_atual + sortimento.comprimento_m

            if h_final > altura_util:
                continue

            rel = h_final / altura_estimada

            d_topo = dap * ((1 - rel) ** alpha)

            if d_topo >= sortimento.diametro_ponta_fina_min_cm:
                d_base = dap * (
                    (1 - (h_atual / altura_estimada)) ** alpha
                )

                d_med = (d_base + d_topo) / 2

                volume = (
                    (math.pi / 40000)
                    * (d_med**2)
                    * sortimento.comprimento_m
                )

                toras.append(
                    ToraSortimento(
                        comprimento=float(sortimento.comprimento_m),
                        diametro_ponta_fina=float(d_topo),
                        sortimento=sortimento.nome,
                        volume_m3=float(volume),
                    )
                )

                volume_total += volume

                h_atual = h_final

                tora_alocada = True
                break

        if not tora_alocada:
            break

    volume_total_ha = volume_total * classe.arvores_por_ha

    return ResultadoTaperClasse(
        dap_centro_classe=float(dap),
        altura_estimada=float(altura_estimada),
        arvores_ha=float(classe.arvores_por_ha),
        toras=toras,
        volume_total_m3_ha=float(volume_total_ha),
    )
