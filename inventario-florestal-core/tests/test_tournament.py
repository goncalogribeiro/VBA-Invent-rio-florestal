import numpy as np
import pandas as pd

from inventario_florestal.modelos.schema import CatalogoModelos
from inventario_florestal.modelos.schema import ModeloBiometrico
from inventario_florestal.ranking.tournament import executar_torneio_linear



def test_torneio_linear_volumetrico():
    np.random.seed(42)

    dap = np.linspace(10, 40, 120)
    h = np.linspace(12, 28, 120)

    volume = 0.00005 * (dap**1.8) * (h**1.1)

    dados = pd.DataFrame(
        {
            "DAP": dap,
            "H": h,
            "V": volume,
        }
    )

    modelos = [
        ModeloBiometrico(
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
        ),
        ModeloBiometrico(
            id="V03",
            grupo="volumetria",
            nome="Spurr sem intercepto",
            formula="V = beta1*DAP^2*H",
            variavel_dependente="V",
            variaveis_independentes=["DAP", "H"],
            parametros=["beta1"],
            tipo_regressao="linear_sem_intercepto",
            linearizavel=True,
            eh_logaritmico=False,
        ),
    ]

    catalogo = CatalogoModelos(modelos=modelos)

    resultado = executar_torneio_linear(
        catalogo=catalogo,
        dados=dados,
        grupo="volumetria",
    )

    assert resultado.vencedor is not None

    assert len(resultado.ranking) >= 1

    assert resultado.vencedor.modelo_id in {"V01", "V03"}
