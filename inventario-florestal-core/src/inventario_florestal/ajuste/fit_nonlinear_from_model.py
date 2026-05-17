"""Executor universal de modelos nao lineares a partir do catalogo YAML."""

from __future__ import annotations

import numpy as np
import pandas as pd

from inventario_florestal.ajuste.nonlinear_regression import ajustar_nls
from inventario_florestal.modelos.nonlinear_functions import (
    obter_funcao_nao_linear,
)
from inventario_florestal.modelos.schema import ModeloBiometrico


class ErroExecucaoModeloNaoLinear(Exception):
    """Erro na execucao automatica de modelos NLS."""



def ajustar_modelo_nao_linear(
    modelo: ModeloBiometrico,
    dados: pd.DataFrame,
):
    """Executa um modelo nao linear definido no catalogo YAML."""

    if modelo.nls is None:
        raise ErroExecucaoModeloNaoLinear(
            f"Modelo {modelo.id} nao possui configuracao NLS."
        )

    funcao = obter_funcao_nao_linear(modelo.nls.funcao_registrada)

    colunas = [
        modelo.variavel_dependente,
        *modelo.variaveis_independentes,
    ]

    dados_validos = dados[colunas].dropna().copy()

    if dados_validos.empty:
        raise ErroExecucaoModeloNaoLinear(
            f"Modelo {modelo.id} nao possui dados validos."
        )

    y = dados_validos[modelo.variavel_dependente].astype(float).to_numpy()

    if len(modelo.variaveis_independentes) == 1:
        x = (
            dados_validos[modelo.variaveis_independentes[0]]
            .astype(float)
            .to_numpy()
        )
    else:
        x = np.vstack(
            [
                dados_validos[coluna].astype(float).to_numpy()
                for coluna in modelo.variaveis_independentes
            ]
        )

    limites = None

    if (
        modelo.nls.limites_inferiores is not None
        and modelo.nls.limites_superiores is not None
    ):
        limites = (
            modelo.nls.limites_inferiores,
            modelo.nls.limites_superiores,
        )

    return ajustar_nls(
        funcao=funcao,
        x=x,
        y=y,
        nomes_parametros=modelo.parametros,
        chute_inicial=modelo.nls.chute_inicial,
        limites=limites,
        max_iteracoes=modelo.nls.max_iteracoes,
    )
