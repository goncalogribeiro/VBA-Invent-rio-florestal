"""Interpretador inicial de formulas lineares biometricas.

Este modulo converte uma formula linear do catalogo YAML em vetores y e X
para ajuste por OLS. A versao inicial cobre as formas mais comuns:

- Y = beta0 + beta1*X
- ln(Y) = beta0 + beta1*ln(X1) + beta2*ln(X2)
- log10(Y) = beta0 + beta1*(1/X)
- termos simples com potencia: DAP^2, d^2, H^2
- produtos: DAP^2*H

A proposta e evoluir gradualmente para um parser matematico completo, mantendo
controle e auditabilidade.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class FormulaLinearPreparada:
    """Formula transformada para ajuste linear."""

    y_nome: str
    y: pd.Series
    x: pd.DataFrame
    y_transformado: bool
    base_logaritmo_y: str | None
    termos_x: list[str]


class ErroFormulaLinear(Exception):
    """Erro de interpretacao de formula linear."""



def _normalizar(expressao: str) -> str:
    """Normaliza caracteres para facilitar o parse."""
    return (
        expressao.replace(" ", "")
        .replace("×", "*")
        .replace("·", "*")
        .replace("^", "**")
    )



def _avaliar_termo(termo: str, dados: pd.DataFrame) -> pd.Series:
    """Avalia um termo simples da formula no DataFrame."""

    termo = termo.strip()

    # Remove coeficiente beta multiplicando o termo.
    termo = re.sub(r"^beta\d+\*", "", termo)
    termo = re.sub(r"^B\d+\*", "", termo)

    # Termo constante/intercepto e ignorado em X.
    if re.fullmatch(r"beta\d+|B\d+", termo):
        raise ErroFormulaLinear("Termo constante nao deve ser avaliado como X.")

    # ln(variavel)
    match_ln = re.fullmatch(r"ln\(([^)]+)\)", termo)
    if match_ln:
        nome = match_ln.group(1)
        return np.log(_avaliar_termo(nome, dados))

    # log10(variavel)
    match_log10 = re.fullmatch(r"log10\(([^)]+)\)", termo)
    if match_log10:
        nome = match_log10.group(1)
        return np.log10(_avaliar_termo(nome, dados))

    # 1/variavel ou 1/(variavel)
    match_inv = re.fullmatch(r"1/\(?([A-Za-z_][A-Za-z0-9_]*)\)?", termo)
    if match_inv:
        nome = match_inv.group(1)
        return 1 / dados[nome].astype(float)

    # potencia simples: DAP**2
    match_pot = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_]*)\*\*(\d+)", termo)
    if match_pot:
        nome = match_pot.group(1)
        expoente = int(match_pot.group(2))
        return dados[nome].astype(float) ** expoente

    # produto de termos simples: DAP**2*H
    if "*" in termo:
        partes = termo.split("*")
        resultado = pd.Series(1.0, index=dados.index)
        i = 0
        while i < len(partes):
            parte = partes[i]
            if i + 2 < len(partes) and partes[i + 1] == "" and partes[i + 2].isdigit():
                combinado = f"{parte}**{partes[i + 2]}"
                resultado = resultado * _avaliar_termo(combinado, dados)
                i += 3
            else:
                resultado = resultado * _avaliar_termo(parte, dados)
                i += 1
        return resultado

    # variavel simples
    if termo in dados.columns:
        return dados[termo].astype(float)

    raise ErroFormulaLinear(f"Termo nao suportado na formula linear: {termo}")



def preparar_formula_linear(
    formula: str,
    dados: pd.DataFrame,
) -> FormulaLinearPreparada:
    """Prepara y e X a partir de uma formula linear.

    Parameters
    ----------
    formula:
        Formula no formato `lado_esquerdo = lado_direito`.
    dados:
        DataFrame com as variaveis observadas.
    """

    expr = _normalizar(formula)

    if "=" not in expr:
        raise ErroFormulaLinear("Formula deve conter sinal de igualdade.")

    esquerda, direita = expr.split("=", 1)

    y_transformado = False
    base_log = None

    match_y_ln = re.fullmatch(r"ln\(([^)]+)\)", esquerda)
    match_y_log10 = re.fullmatch(r"log10\(([^)]+)\)", esquerda)

    if match_y_ln:
        y_nome = match_y_ln.group(1)
        y = np.log(dados[y_nome].astype(float))
        y_transformado = True
        base_log = "ln"
    elif match_y_log10:
        y_nome = match_y_log10.group(1)
        y = np.log10(dados[y_nome].astype(float))
        y_transformado = True
        base_log = "log10"
    elif esquerda in dados.columns:
        y_nome = esquerda
        y = dados[y_nome].astype(float)
    else:
        raise ErroFormulaLinear(f"Variavel dependente nao suportada: {esquerda}")

    termos_brutos = direita.split("+")
    colunas = {}
    termos_x = []

    for termo in termos_brutos:
        # ignora intercepto beta0/B0
        if re.fullmatch(r"beta0|B0", termo):
            continue

        try:
            serie = _avaliar_termo(termo, dados)
        except ErroFormulaLinear:
            # se for constante parametrica, ignora; senao propaga
            if re.fullmatch(r"beta\d+|B\d+", termo):
                continue
            raise

        nome_coluna = termo
        colunas[nome_coluna] = serie
        termos_x.append(nome_coluna)

    if not colunas:
        raise ErroFormulaLinear("Nenhum termo independente foi identificado.")

    x = pd.DataFrame(colunas, index=dados.index)

    return FormulaLinearPreparada(
        y_nome=y_nome,
        y=pd.Series(y, index=dados.index, name=y_nome),
        x=x,
        y_transformado=y_transformado,
        base_logaritmo_y=base_log,
        termos_x=termos_x,
    )
