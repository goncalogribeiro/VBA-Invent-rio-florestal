from __future__ import annotations

from inventario_florestal.testing.synthetic_dataset_generator import (
    gerar_dataset_sintetico,
)



def cenario_normal():
    return gerar_dataset_sintetico(
        numero_arvores=400,
        idade=8,
        dap_min=12,
        dap_max=28,
        altura_min=10,
        altura_max=24,
    )



def cenario_superlotado():
    return gerar_dataset_sintetico(
        numero_arvores=2200,
        idade=6,
        dap_min=6,
        dap_max=18,
        altura_min=6,
        altura_max=16,
    )



def cenario_baixa_densidade():
    return gerar_dataset_sintetico(
        numero_arvores=120,
        idade=10,
        dap_min=20,
        dap_max=40,
        altura_min=15,
        altura_max=30,
    )



def cenario_elite_genetica():
    return gerar_dataset_sintetico(
        numero_arvores=600,
        idade=7,
        dap_min=18,
        dap_max=35,
        altura_min=16,
        altura_max=30,
    )



def cenario_sitio_ruim():
    return gerar_dataset_sintetico(
        numero_arvores=700,
        idade=9,
        dap_min=6,
        dap_max=16,
        altura_min=5,
        altura_max=14,
    )



def cenario_mortalidade_alta():
    return gerar_dataset_sintetico(
        numero_arvores=300,
        idade=12,
        dap_min=8,
        dap_max=24,
        altura_min=8,
        altura_max=20,
    )



def cenario_desbaste_pesado():
    return gerar_dataset_sintetico(
        numero_arvores=180,
        idade=11,
        dap_min=22,
        dap_max=42,
        altura_min=18,
        altura_max=32,
    )
