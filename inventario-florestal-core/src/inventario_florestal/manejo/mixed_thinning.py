from __future__ import annotations

from dataclasses import dataclass

from inventario_florestal.manejo.quality_selection import (
    ArvoreQualitativa,
    selecionar_por_area_basal,
    selecionar_por_percentual_arvores,
)


@dataclass(frozen=True)
class ResultadoDesbasteMisto:
    sistematicas_removidas: list[ArvoreQualitativa]
    seletivas_removidas: list[ArvoreQualitativa]
    remanescentes: list[ArvoreQualitativa]
    n_total_inicial: int
    n_removido_total: int
    g_total_inicial: float
    g_removido_total: float
    volume_removido_total: float
    intensidade_n_real: float
    intensidade_g_real: float


class ErroDesbasteMisto(Exception):
    pass



def remover_sistematico_por_percentual(
    arvores: list[ArvoreQualitativa],
    percentual_sistematico: float,
) -> list[ArvoreQualitativa]:
    """
    Remove uma fração sistemática simplificada das árvores.

    Esta primeira versão usa seleção por índice, simulando remoção geométrica
    aproximada. Futuramente poderá usar linha/faixa/coordenadas.
    """

    if percentual_sistematico <= 0:
        return []

    if percentual_sistematico >= 1:
        raise ErroDesbasteMisto(
            "Percentual sistemático deve ser menor que 1."
        )

    passo = max(1, round(1 / percentual_sistematico))

    return [
        arv
        for i, arv in enumerate(arvores)
        if i % passo == 0
    ]



def aplicar_desbaste_misto(
    arvores: list[ArvoreQualitativa],
    intensidade_total: float,
    criterio_meta: str,
    percentual_sistematico: float,
) -> ResultadoDesbasteMisto:
    """
    Aplica desbaste misto em duas fases.

    Fase 1: remoção sistemática simplificada.
    Fase 2: seleção qualitativa complementar até a meta final.

    criterio_meta:
    - arvores
    - area_basal
    """

    if intensidade_total <= 0 or intensidade_total >= 1:
        raise ErroDesbasteMisto(
            "Intensidade total deve estar entre 0 e 1."
        )

    if criterio_meta not in {"arvores", "area_basal"}:
        raise ErroDesbasteMisto(
            f"Critério inválido: {criterio_meta}"
        )

    n_total = len(arvores)
    g_total = sum(arv.area_basal for arv in arvores)

    sistematicas = remover_sistematico_por_percentual(
        arvores=arvores,
        percentual_sistematico=percentual_sistematico,
    )

    ids_sistematicas = {arv.id_arvore for arv in sistematicas}

    apos_sistematico = [
        arv
        for arv in arvores
        if arv.id_arvore not in ids_sistematicas
    ]

    if criterio_meta == "arvores":
        alvo_n_total = int(n_total * intensidade_total)
        n_restante = max(0, alvo_n_total - len(sistematicas))

        intensidade_complementar = (
            n_restante / len(apos_sistematico)
            if apos_sistematico
            else 0
        )

        seletivas = (
            selecionar_por_percentual_arvores(
                apos_sistematico,
                intensidade_complementar,
            )
            if intensidade_complementar > 0
            else []
        )

    else:
        alvo_g_total = g_total * intensidade_total
        g_sistematica = sum(arv.area_basal for arv in sistematicas)
        g_restante = max(0.0, alvo_g_total - g_sistematica)
        g_apos = sum(arv.area_basal for arv in apos_sistematico)

        intensidade_complementar = (
            g_restante / g_apos
            if g_apos > 0
            else 0
        )

        seletivas = (
            selecionar_por_area_basal(
                apos_sistematico,
                intensidade_complementar,
            )
            if intensidade_complementar > 0
            else []
        )

    ids_removidas = {
        arv.id_arvore
        for arv in [*sistematicas, *seletivas]
    }

    remanescentes = [
        arv
        for arv in arvores
        if arv.id_arvore not in ids_removidas
    ]

    removidas_total = [*sistematicas, *seletivas]

    g_removido = sum(arv.area_basal for arv in removidas_total)
    volume_removido = sum(arv.volume for arv in removidas_total)

    intensidade_n_real = len(removidas_total) / n_total if n_total > 0 else 0.0
    intensidade_g_real = g_removido / g_total if g_total > 0 else 0.0

    return ResultadoDesbasteMisto(
        sistematicas_removidas=sistematicas,
        seletivas_removidas=seletivas,
        remanescentes=remanescentes,
        n_total_inicial=n_total,
        n_removido_total=len(removidas_total),
        g_total_inicial=float(g_total),
        g_removido_total=float(g_removido),
        volume_removido_total=float(volume_removido),
        intensidade_n_real=float(intensidade_n_real),
        intensidade_g_real=float(intensidade_g_real),
    )
