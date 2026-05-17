import pytest

from inventario_florestal.silviculture.silvicultural_profiles import (
    PERFIS_SILVICULTURAIS,
    obter_perfil_silvicultural,
)



def test_obter_perfil_operacional():
    perfil = obter_perfil_silvicultural(
        "operacional"
    )

    assert perfil.nome == "operacional"



def test_perfis_existentes():
    assert "conservador" in PERFIS_SILVICULTURAIS
    assert "operacional" in PERFIS_SILVICULTURAIS
    assert "elite_genetica" in PERFIS_SILVICULTURAIS



def test_perfil_inexistente():
    with pytest.raises(ValueError):
        obter_perfil_silvicultural(
            "perfil_inexistente"
        )
