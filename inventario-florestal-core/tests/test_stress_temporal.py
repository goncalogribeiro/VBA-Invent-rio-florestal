from inventario_florestal.testing.extreme_scenarios import (
    cenario_baixa_densidade,
    cenario_elite_genetica,
    cenario_normal,
    cenario_sitio_ruim,
    cenario_superlotado,
)
from inventario_florestal.testing.temporal_simulator import (
    simular_periodo,
)



def _validar_estado_final(arvores):
    assert isinstance(arvores, list)
    assert len(arvores) >= 0

    for arvore in arvores:
        assert arvore.dap_cm > 0
        assert arvore.altura_m > 0
        assert arvore.idade > 0



def test_stress_cenario_normal_10_anos():
    dataset = cenario_normal()

    resultado = simular_periodo(
        dataset,
        anos=10,
        perfil_nome="operacional",
    )

    _validar_estado_final(resultado)
    assert len(resultado) > 0



def test_stress_cenario_elite_10_anos():
    dataset = cenario_elite_genetica()

    resultado = simular_periodo(
        dataset,
        anos=10,
        perfil_nome="elite_genetica",
    )

    _validar_estado_final(resultado)
    assert len(resultado) > 0



def test_stress_cenario_sitio_ruim_10_anos():
    dataset = cenario_sitio_ruim()

    resultado = simular_periodo(
        dataset,
        anos=10,
        perfil_nome="conservador",
    )

    _validar_estado_final(resultado)
    assert len(resultado) > 0



def test_stress_cenario_baixa_densidade_15_anos():
    dataset = cenario_baixa_densidade()

    resultado = simular_periodo(
        dataset,
        anos=15,
        perfil_nome="operacional",
    )

    _validar_estado_final(resultado)
    assert len(resultado) > 0



def test_stress_cenario_superlotado_nao_gera_negativos():
    dataset = cenario_superlotado()

    resultado = simular_periodo(
        dataset,
        anos=5,
        perfil_nome="conservador",
    )

    _validar_estado_final(resultado)
