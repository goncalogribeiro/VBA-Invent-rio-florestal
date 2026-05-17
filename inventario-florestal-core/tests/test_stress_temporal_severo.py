from inventario_florestal.testing.extreme_scenarios import (
    cenario_elite_genetica,
    cenario_normal,
    cenario_sitio_ruim,
    cenario_superlotado,
)
from inventario_florestal.testing.temporal_simulator import (
    simular_periodo,
)



def _validar_arvores(arvores):
    for arvore in arvores:
        assert arvore.dap_cm > 0
        assert arvore.altura_m > 0
        assert arvore.idade > 0
        assert arvore.dap_cm < 150
        assert arvore.altura_m < 80



def test_cenario_normal_25_anos_mantem_plausibilidade():
    dataset = cenario_normal()

    resultado = simular_periodo(
        dataset,
        anos=25,
        perfil_nome="operacional",
    )

    assert len(resultado) > 0
    _validar_arvores(resultado)



def test_cenario_elite_25_anos_nao_explode():
    dataset = cenario_elite_genetica()

    resultado = simular_periodo(
        dataset,
        anos=25,
        perfil_nome="elite_genetica",
    )

    assert len(resultado) > 0
    _validar_arvores(resultado)



def test_cenario_sitio_ruim_25_anos_nao_colapsa_totalmente():
    dataset = cenario_sitio_ruim()

    resultado = simular_periodo(
        dataset,
        anos=25,
        perfil_nome="conservador",
    )

    assert len(resultado) > 0
    _validar_arvores(resultado)



def test_cenario_superlotado_10_anos_sem_negativos():
    dataset = cenario_superlotado()

    resultado = simular_periodo(
        dataset,
        anos=10,
        perfil_nome="conservador",
    )

    _validar_arvores(resultado)



def test_sobrevivencia_superlotado_reduz_populacao():
    dataset = cenario_superlotado()

    resultado = simular_periodo(
        dataset,
        anos=10,
        perfil_nome="conservador",
    )

    assert len(resultado) <= len(dataset)
