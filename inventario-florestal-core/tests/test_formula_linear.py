import numpy as np
import pandas as pd

from inventario_florestal.ajuste.formula_linear import (
    preparar_formula_linear,
)



def test_formula_logaritmica_schumacher_hall():
    dados = pd.DataFrame(
        {
            "DAP": np.array([10, 15, 20, 25], dtype=float),
            "H": np.array([12, 15, 18, 22], dtype=float),
            "V": np.array([0.1, 0.3, 0.6, 1.1], dtype=float),
        }
    )

    formula = "ln(V) = beta0 + beta1*ln(DAP) + beta2*ln(H)"

    preparada = preparar_formula_linear(formula, dados)

    assert preparada.y_transformado is True
    assert preparada.base_logaritmo_y == "ln"

    assert preparada.x.shape[1] == 2



def test_formula_linear_simples():
    dados = pd.DataFrame(
        {
            "d": np.array([10, 20, 30], dtype=float),
            "h": np.array([12, 18, 24], dtype=float),
        }
    )

    formula = "h = beta0 + beta1*d"

    preparada = preparar_formula_linear(formula, dados)

    assert preparada.y_nome == "h"
    assert preparada.x.shape[1] == 1
