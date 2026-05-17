from inventario_florestal.testing.synthetic_dataset_generator import (
    gerar_dataset_sintetico,
)
from inventario_florestal.testing.temporal_simulator import (
    simular_ano,
    simular_periodo,
)



def test_simular_ano_retorna_lista():
    dataset = gerar_dataset_sintetico(
        numero_arvores=100,
    )

    resultado = simular_ano(dataset)

    assert isinstance(resultado, list)



def test_simular_ano_sem_valores_negativos():
    dataset = gerar_dataset_sintetico(
        numero_arvores=100,
    )

    resultado = simular_ano(dataset)

    for arvore in resultado:
        assert arvore.dap_cm > 0
        assert arvore.altura_m > 0
        assert arvore.idade > 0



def test_simular_periodo_funciona():
    dataset = gerar_dataset_sintetico(
        numero_arvores=100,
    )

    resultado = simular_periodo(
        dataset,
        anos=5,
    )

    assert isinstance(resultado, list)



def test_simular_periodo_nao_colapsa_populacao():
    dataset = gerar_dataset_sintetico(
        numero_arvores=100,
    )

    resultado = simular_periodo(
        dataset,
        anos=5,
    )

    assert len(resultado) > 0
