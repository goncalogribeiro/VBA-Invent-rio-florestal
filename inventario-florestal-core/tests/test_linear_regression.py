import numpy as np
import pandas as pd

from inventario_florestal.ajuste.linear_regression import ajustar_ols



def test_ajuste_linear_simples():
    np.random.seed(42)

    dap = np.linspace(10, 40, 100)

    altura = 5 + 0.7 * dap

    dados = pd.DataFrame(
        {
            "dap": dap,
            "altura": altura,
        }
    )

    resultado = ajustar_ols(
        dados=dados,
        variavel_dependente="altura",
        variaveis_independentes=["dap"],
    )

    assert resultado.n == 100

    assert "dap" in resultado.coeficientes

    assert resultado.metricas["r2"] > 0.99

    assert abs(resultado.metricas["bias"]) < 1e-6
