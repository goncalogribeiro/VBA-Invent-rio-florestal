"""Geracao de pesos para regressao ponderada.

A ponderacao deve ser usada com criterio tecnico, especialmente quando houver
heterocedasticidade detectada. Este modulo concentra estrategias simples e
auditaveis para WLS.
"""

from __future__ import annotations

from typing import Literal

import numpy as np
import pandas as pd


EPSILON = 1e-12

EstrategiaPeso = Literal[
    "inverso_variavel_quadrado",
    "inverso_estimado_quadrado",
    "inverso_residuo_abs",
    "inverso_residuo_quadrado",
]


class ErroPesosWLS(Exception):
    """Erro na geracao de pesos WLS."""



def _validar_pesos(pesos: np.ndarray) -> np.ndarray:
    """Valida e normaliza pesos positivos."""

    w = np.asarray(pesos, dtype=float)

    if w.ndim != 1:
        raise ErroPesosWLS("Pesos devem formar um vetor unidimensional.")

    if np.any(~np.isfinite(w)):
        raise ErroPesosWLS("Pesos contem valores nao finitos.")

    if np.any(w <= 0):
        raise ErroPesosWLS("Todos os pesos devem ser positivos.")

    media = np.mean(w)

    if media <= EPSILON:
        raise ErroPesosWLS("Media dos pesos invalida.")

    return w / media



def pesos_por_variavel(
    dados: pd.DataFrame,
    coluna: str,
    potencia: float = 2.0,
) -> np.ndarray:
    """Gera pesos inversamente proporcionais a uma variavel.

    Forma geral:

    w_i = 1 / x_i^potencia

    Uso comum:

    - 1 / DAP²;
    - 1 / H²;
    - 1 / volume_estimado².
    """

    if coluna not in dados.columns:
        raise ErroPesosWLS(f"Coluna nao encontrada para pesos: {coluna}")

    valores = dados[coluna].astype(float).to_numpy()

    if np.any(valores <= 0):
        raise ErroPesosWLS(
            "A coluna usada para pesos deve possuir valores positivos."
        )

    pesos = 1 / np.maximum(valores, EPSILON) ** potencia

    return _validar_pesos(pesos)



def pesos_por_estimado(
    estimado: np.ndarray,
    potencia: float = 2.0,
) -> np.ndarray:
    """Gera pesos inversamente proporcionais ao valor estimado."""

    valores = np.asarray(estimado, dtype=float)

    if np.any(valores <= 0):
        raise ErroPesosWLS(
            "Estimativas usadas para pesos devem ser positivas."
        )

    pesos = 1 / np.maximum(valores, EPSILON) ** potencia

    return _validar_pesos(pesos)



def pesos_por_residuo(
    residuos: np.ndarray,
    potencia: float = 1.0,
) -> np.ndarray:
    """Gera pesos inversamente proporcionais aos residuos absolutos.

    Esta estrategia deve ser usada com cautela, preferencialmente em rotinas
    iterativas ou em comparacoes controladas, pois pode reduzir excessivamente
    a influencia de observacoes importantes.
    """

    valores = np.abs(np.asarray(residuos, dtype=float))

    pesos = 1 / np.maximum(valores, EPSILON) ** potencia

    return _validar_pesos(pesos)



def gerar_pesos_wls(
    estrategia: EstrategiaPeso,
    dados: pd.DataFrame | None = None,
    coluna: str | None = None,
    estimado: np.ndarray | None = None,
    residuos: np.ndarray | None = None,
) -> np.ndarray:
    """Gera pesos WLS conforme estrategia declarada."""

    if estrategia == "inverso_variavel_quadrado":
        if dados is None or coluna is None:
            raise ErroPesosWLS(
                "Estrategia por variavel requer dados e coluna."
            )
        return pesos_por_variavel(dados=dados, coluna=coluna, potencia=2.0)

    if estrategia == "inverso_estimado_quadrado":
        if estimado is None:
            raise ErroPesosWLS(
                "Estrategia por estimado requer vetor estimado."
            )
        return pesos_por_estimado(estimado=estimado, potencia=2.0)

    if estrategia == "inverso_residuo_abs":
        if residuos is None:
            raise ErroPesosWLS(
                "Estrategia por residuo requer vetor de residuos."
            )
        return pesos_por_residuo(residuos=residuos, potencia=1.0)

    if estrategia == "inverso_residuo_quadrado":
        if residuos is None:
            raise ErroPesosWLS(
                "Estrategia por residuo requer vetor de residuos."
            )
        return pesos_por_residuo(residuos=residuos, potencia=2.0)

    raise ErroPesosWLS(f"Estrategia de pesos nao suportada: {estrategia}")
