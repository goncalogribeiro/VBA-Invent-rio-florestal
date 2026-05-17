import numpy as np

from inventario_florestal.ranking.bias import (
    aplicar_fator_retransformacao,
    fator_meyer,
)



def test_fator_meyer_maior_que_um():
    residuos = np.array([0.1, -0.2, 0.05, -0.1])

    fm = fator_meyer(residuos)

    assert fm > 1.0



def test_retransformacao_ln():
    valores_log = np.array([1.0, 2.0])

    resultado = aplicar_fator_retransformacao(
        estimado_transformado=valores_log,
        fator_correcao=1.0,
        base_logaritmo="ln",
    )

    esperado = np.exp(valores_log)

    assert np.allclose(resultado, esperado)
