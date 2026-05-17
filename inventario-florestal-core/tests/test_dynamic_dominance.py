from inventario_florestal.ecology.dynamic_dominance import (
    CODOMINANTE,
    DOMINADA,
    DOMINANTE,
    SUPRIMIDA,
    classificar_posicao_sociologica,
    dap_medio,
    altura_media,
)
from inventario_florestal.testing.synthetic_dataset_generator import (
    gerar_dataset_sintetico,
)



def test_dap_medio_positivo():
    dataset = gerar_dataset_sintetico(50)

    assert dap_medio(dataset) > 0



def test_altura_media_positiva():
    dataset = gerar_dataset_sintetico(50)

    assert altura_media(dataset) > 0



def test_classificacao_sociologica_valida():
    dataset = gerar_dataset_sintetico(50)

    dap_med = dap_medio(dataset)
    alt_med = altura_media(dataset)

    classe = classificar_posicao_sociologica(
        dataset[0],
        dap_med,
        alt_med,
    )

    assert classe in {
        DOMINANTE,
        CODOMINANTE,
        DOMINADA,
        SUPRIMIDA,
    }
