from inventario_florestal.core.biological_constraints import (
    validar_crescimento_dap,
    validar_lai,
    validar_mortalidade,
    validar_variavel_nao_negativa,
)



def test_validar_crescimento_dap_limite_inferior():
    assert validar_crescimento_dap(-1.0) == 0.0



def test_validar_crescimento_dap_limite_superior():
    assert validar_crescimento_dap(10.0) == 5.0



def test_validar_mortalidade_limite_inferior():
    assert validar_mortalidade(-0.5) == 0.0



def test_validar_mortalidade_limite_superior():
    assert validar_mortalidade(2.0) == 1.0



def test_validar_lai_limite_superior():
    assert validar_lai(20.0) == 12.0



def test_validar_variavel_nao_negativa():
    assert validar_variavel_nao_negativa(-5.0) == 0.0
    assert validar_variavel_nao_negativa(3.0) == 3.0
