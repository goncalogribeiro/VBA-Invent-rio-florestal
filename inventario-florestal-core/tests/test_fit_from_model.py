import numpy as np
import pandas as pd

from inventario_florestal.ajuste.fit_from_model import (
    ajustar_modelo_linear_catalogo,
)
from inventario_florestal.modelos.schema import FonteModelo
from inventario_florestal.modelos.schema import ModeloBiometrico



def test_ajuste_schumacher_hall_catalogo():
    np.random.seed(42)

    dap = np.linspace(10, 40, 80)
    h = np.linspace(12, 28, 80)

    volume = 0.00005 * (dap**1.8) * (h**1.1)

    dados = pd.DataFrame(
        {
            "DAP": dap,
            "H": h,
            "V": volume,
        }
    )

    modelo = ModeloBiometrico(
        id="V01",
        grupo="volumetria",
        nome="Schumacher-Hall",
        formula="ln(V) = beta0 + beta1*ln(DAP) + beta2*ln(H)",
        variavel_dependente="V",
        variaveis_independentes=["DAP", "H"],
        parametros=["beta0", "beta1", "beta2"],
        tipo_regressao="linear",
        linearizavel=True,
        eh_logaritmico=True,
        base_logaritmo="ln",
        metodo_correcao_vies="meyer",
        fonte=FonteModelo(autores="Teste", ano=2026),
    )

    resultado = ajustar_modelo_linear_catalogo(modelo, dados)

    assert resultado.modelo_id == "V01"

    assert resultado.metricas_escala_original is not None

    assert resultado.metricas_escala_original["r2"] > 0.99
