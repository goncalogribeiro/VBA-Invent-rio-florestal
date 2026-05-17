from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessoFisiologico:
    identificador: str
    radiacao_interceptada: float
    eficiencia_fotossintetica: float
    biomassa_kg: float


class ErroCarbono(Exception):
    pass



def calcular_gpp(
    radiacao_interceptada: float,
    eficiencia_fotossintetica: float,
) -> float:
    """
    Gross Primary Productivity simplificada.
    """

    return (
        radiacao_interceptada
        * eficiencia_fotossintetica
    )



def respiracao_autotrofica(
    biomassa_kg: float,
) -> float:
    """
    Respiração autotrófica simplificada.
    """

    return biomassa_kg * 0.015



def calcular_npp(
    gpp: float,
    respiracao: float,
) -> float:
    """
    Net Primary Productivity simplificada.
    """

    return max(0.0, gpp - respiracao)



def analisar_balanco_carbono(
    processo: ProcessoFisiologico,
) -> dict[str, float]:
    """
    Primeira camada fisiológica funcional.

    Futuramente:
    - FPAR;
    - eficiência quântica;
    - respiração heterotrófica;
    - IA ecofisiológica.
    """

    gpp = calcular_gpp(
        processo.radiacao_interceptada,
        processo.eficiencia_fotossintetica,
    )

    respiracao = respiracao_autotrofica(
        processo.biomassa_kg
    )

    npp = calcular_npp(
        gpp,
        respiracao,
    )

    return {
        "gpp": float(gpp),
        "respiracao": float(respiracao),
        "npp": float(npp),
    }
