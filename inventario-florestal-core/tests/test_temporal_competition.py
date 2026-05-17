from inventario_florestal.ecology.temporal_competition import (
    distancia,
    fator_aumento_mortalidade,
    fator_reducao_crescimento,
    indice_competicao_hegyi,
)
from inventario_florestal.testing.synthetic_dataset_generator import (
    gerar_dataset_sintetico,
)



def test_distancia_positiva():
    dataset = gerar_dataset_sintetico(2)

    d = distancia(dataset[0], dataset[1])

    assert d > 0



def test_indice_competicao_finito():
    dataset = gerar_dataset_sintetico(10)

    indice = indice_competicao_hegyi(
        dataset[0],
        dataset,
    )

    assert indice >= 0



def test_fator_reducao_crescimento_positivo():
    fator = fator_reducao_crescimento(100)

    assert fator > 0



def test_fator_aumento_mortalidade_positivo():
    fator = fator_aumento_mortalidade(10)

    assert fator > 1
