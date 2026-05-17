from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArvoreCrescimento:
    identificador: str
    dap_cm: float
    altura_m: float
    indice_competicao: float


class ErroCrescimento(Exception):
    pass



def crescimento_potencial_dap(
    dap_cm: float,
    sitio: float = 1.0,
) -> float:
    """
    Crescimento potencial simplificado.
    """

    return (dap_cm * 0.03) * sitio



def reduzir_por_competicao(
    crescimento: float,
    indice_competicao: float,
) -> float:
    """
    Redução simplificada por competição.
    """

    fator = max(0.1, 1 - (indice_competicao * 0.01))

    return crescimento * fator



def projetar_crescimento_individual(
    arvore: ArvoreCrescimento,
    sitio: float = 1.0,
) -> dict[str, float]:
    """
    Primeira camada de crescimento individual.

    Futuramente:
    - Hegyi;
    - mortalidade;
    - dominância;
    - competição de copa;
    - IA.
    """

    potencial = crescimento_potencial_dap(
        dap_cm=arvore.dap_cm,
        sitio=sitio,
    )

    real = reduzir_por_competicao(
        crescimento=potencial,
        indice_competicao=arvore.indice_competicao,
    )

    return {
        "crescimento_potencial": float(potencial),
        "crescimento_real": float(real),
    }
