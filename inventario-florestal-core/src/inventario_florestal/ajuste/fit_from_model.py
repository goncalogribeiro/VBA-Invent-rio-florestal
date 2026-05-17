"""Ajuste automatico de modelos biometricos a partir do catalogo YAML.

Este modulo conecta:

- ModeloBiometrico;
- interpretador de formula linear;
- motor OLS;
- correcao de vies para modelos logaritmicos;
- diagnostico residual.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from inventario_florestal.ajuste.formula_linear import preparar_formula_linear
from inventario_florestal.ajuste.linear_regression import (
    ResultadoRegressaoLinear,
    ajustar_ols,
)
from inventario_florestal.modelos.schema import ModeloBiometrico
from inventario_florestal.ranking.bias import (
    aplicar_fator_retransformacao,
    fator_meyer,
)
from inventario_florestal.ranking.metrics import (
    bias,
    mae,
    r2,
    r2_ajustado,
    rmse,
    syx,
    syx_percentual,
)
from inventario_florestal.ranking.residual_analysis import (
    DiagnosticoResidual,
    diagnosticar_residuos,
)


@dataclass(frozen=True)
class ResultadoAjusteModelo:
    """Resultado padronizado de ajuste a partir de um modelo do catalogo."""

    modelo_id: str
    nome_modelo: str
    grupo: str
    resultado_linear: ResultadoRegressaoLinear
    estimado_escala_original: np.ndarray | None
    fator_correcao_vies: float | None
    metricas_escala_original: dict[str, float] | None
    diagnostico_residual: DiagnosticoResidual


class ErroAjusteModelo(Exception):
    """Erro no ajuste automatico de modelo."""



def ajustar_modelo_linear_catalogo(
    modelo: ModeloBiometrico,
    dados: pd.DataFrame,
) -> ResultadoAjusteModelo:
    """Ajusta um modelo linear ou linearizado descrito no catalogo."""

    if modelo.tipo_regressao not in {"linear", "linear_sem_intercepto"}:
        raise ErroAjusteModelo(
            f"Modelo {modelo.id} nao e linear/linearizado: {modelo.tipo_regressao}"
        )

    preparada = preparar_formula_linear(modelo.formula, dados)

    dados_ajuste = pd.concat(
        [preparada.y.rename("__y__"), preparada.x],
        axis=1,
    )

    resultado = ajustar_ols(
        dados=dados_ajuste,
        variavel_dependente="__y__",
        variaveis_independentes=list(preparada.x.columns),
        intercepto=(modelo.tipo_regressao != "linear_sem_intercepto"),
    )

    estimado_original = None
    fator_correcao = None
    metricas_original = None

    observado_diagnostico = resultado.observado
    estimado_diagnostico = resultado.estimado

    if preparada.y_transformado:
        if modelo.metodo_correcao_vies == "meyer" or modelo.eh_logaritmico:
            fator_correcao = fator_meyer(
                resultado.residuos,
                n_parametros=resultado.n_parametros,
            )
        else:
            fator_correcao = 1.0

        estimado_original = aplicar_fator_retransformacao(
            estimado_transformado=resultado.estimado,
            fator_correcao=fator_correcao,
            base_logaritmo=preparada.base_logaritmo_y or "ln",
        )

        observado_original = dados[preparada.y_nome].to_numpy(dtype=float)
        n_parametros = resultado.n_parametros

        metricas_original = {
            "r2": r2(observado_original, estimado_original),
            "r2_ajustado": r2_ajustado(
                observado_original,
                estimado_original,
                n_parametros,
            ),
            "syx": syx(observado_original, estimado_original, n_parametros),
            "syx_percentual": syx_percentual(
                observado_original,
                estimado_original,
                n_parametros),
            "rmse": rmse(observado_original, estimado_original),
            "mae": mae(observado_original, estimado_original),
            "bias": bias(observado_original, estimado_original),
        }

        observado_diagnostico = observado_original
        estimado_diagnostico = estimado_original

    diagnostico = diagnosticar_residuos(
        observado=observado_diagnostico,
        estimado=estimado_diagnostico,
        matriz_x=resultado.matriz_x,
    )

    return ResultadoAjusteModelo(
        modelo_id=modelo.id,
        nome_modelo=modelo.nome,
        grupo=modelo.grupo,
        resultado_linear=resultado,
        estimado_escala_original=estimado_original,
        fator_correcao_vies=fator_correcao,
        metricas_escala_original=metricas_original,
        diagnostico_residual=diagnostico,
    )
