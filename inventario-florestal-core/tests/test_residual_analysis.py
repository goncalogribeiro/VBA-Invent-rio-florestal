import numpy as np

from inventario_florestal.ranking.residual_analysis import (
    diagnosticar_residuos,
)



def test_diagnostico_residual_basico():
    observado = np.array([10.0, 12.0, 14.0, 16.0])
    estimado = np.array([9.8, 12.1, 13.9, 16.2])

    diagnostico = diagnosticar_residuos(
        observado=observado,
        estimado=estimado,
    )

    assert diagnostico.press >= 0

    assert len(diagnostico.residuos) == 4

    assert len(diagnostico.residuos_percentuais) == 4

    assert diagnostico.max_abs_residuo_percentual >= 0
