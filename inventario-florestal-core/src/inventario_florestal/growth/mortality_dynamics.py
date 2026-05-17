from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArvoreDinamica:
    identificador: str
    dap_cm: float
    indice_competicao: float
    vigor: float


class ErroMortalidade(Exception):
    pass



def calcular_probabilidade_mortalidade(
    arvore: ArvoreDinamica,
) -> float:
    """
    Probabilidade simplificada de mortalidade.
    """

    competencia = arvore.indice_competicao * 0.02

    vigor = max(0.0, 1 - arvore.vigor)

    mortalidade = competencia + vigor

    return min(1.0, mortalidade)



def classificar_dominancia(
    dap_cm: float,
) -> str:
    """
    Classificação simplificada de dominância.
    """

    if dap_cm < 15:
        return "dominada"

    if dap_cm < 30:
        return "codominante"

    return "dominante"



def analisar_dinamica_ecologica(
    arvore: ArvoreDinamica,
) -> dict[str, float | str]:
    """
    Primeira camada de dinâmica ecológica.

    Futuramente:
    - BAL;
    - Hegyi;
    - sucessão;
    - mortalidade espacial;
    - IA ecológica.
    """

    mortalidade = calcular_probabilidade_mortalidade(
        arvore
    )

    dominancia = classificar_dominancia(
        arvore.dap_cm
    )

    return {
        "probabilidade_mortalidade": float(mortalidade),
        "classe_dominancia": dominancia,
    }
