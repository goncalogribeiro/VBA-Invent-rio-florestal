from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArvoreLuz:
    identificador: str
    altura_m: float
    area_copa_m2: float
    dominancia: str


class ErroLuz(Exception):
    pass



def fator_interceptacao_luz(
    arvore: ArvoreLuz,
) -> float:
    """
    Interceptação luminosa simplificada.
    """

    if arvore.dominancia == "dominante":
        return 1.0

    if arvore.dominancia == "codominante":
        return 0.75

    return 0.45



def crescimento_adaptativo(
    crescimento_base: float,
    fator_luz: float,
) -> float:
    """
    Crescimento dependente de luz.
    """

    return crescimento_base * fator_luz



def analisar_competicao_luminosa(
    arvore: ArvoreLuz,
    crescimento_base: float,
) -> dict[str, float]:
    """
    Primeira camada de competição luminosa.

    Futuramente:
    - ray tracing;
    - sucessão espacial;
    - IA ecológica;
    - competição estrutural.
    """

    fator_luz = fator_interceptacao_luz(
        arvore
    )

    crescimento = crescimento_adaptativo(
        crescimento_base,
        fator_luz,
    )

    return {
        "fator_luz": float(fator_luz),
        "crescimento_adaptativo": float(crescimento),
    }
