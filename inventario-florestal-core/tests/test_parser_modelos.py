from pathlib import Path

from inventario_florestal.utils.model_parser import carregar_catalogo


ROOT = Path(__file__).resolve().parents[1]



def test_carregar_catalogo_yaml():
    caminho = (
        ROOT
        / "data"
        / "modelos"
        / "modelos_biometricos.yaml"
    )

    catalogo = carregar_catalogo(caminho)

    assert len(catalogo.modelos) >= 2

    modelo = catalogo.buscar_por_id("H01")

    assert modelo is not None
    assert modelo.nome == "Prodan"
    assert modelo.grupo == "hipsometria"
