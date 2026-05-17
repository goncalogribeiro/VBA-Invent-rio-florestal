from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class SortimentoCenario:
    id: str
    nome: str
    diametro_ponta_fina_min_cm: float
    comprimento_m: float
    valor_ton: float


@dataclass(frozen=True)
class CenarioOperacional:
    nome: str
    idade_min: int
    idade_max: int
    sortimentos: list[SortimentoCenario]


class ErroScenarioEngine(Exception):
    pass



def carregar_yaml_modelos(path_yaml: str | Path) -> dict:
    path = Path(path_yaml)

    if not path.exists():
        raise ErroScenarioEngine(
            f"Arquivo YAML nao encontrado: {path}"
        )

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)



def carregar_cenario(
    path_yaml: str | Path,
    nome_cenario: str,
) -> CenarioOperacional:
    dados = carregar_yaml_modelos(path_yaml)

    cenarios = dados.get("cenarios_sortimento", {})

    if nome_cenario not in cenarios:
        raise ErroScenarioEngine(
            f"Cenario nao encontrado: {nome_cenario}"
        )

    cenario = cenarios[nome_cenario]

    sortimentos: list[SortimentoCenario] = []

    for s in cenario.get("sortimentos", []):
        sortimentos.append(
            SortimentoCenario(
                id=s["id"],
                nome=s["nome"],
                diametro_ponta_fina_min_cm=float(
                    s["diametro_ponta_fina_min_cm"]
                ),
                comprimento_m=float(s["comprimento_m"]),
                valor_ton=float(s["valor_ton"]),
            )
        )

    sortimentos.sort(
        key=lambda x: x.diametro_ponta_fina_min_cm,
        reverse=True,
    )

    return CenarioOperacional(
        nome=nome_cenario,
        idade_min=int(cenario["idade_min"]),
        idade_max=int(cenario["idade_max"]),
        sortimentos=sortimentos,
    )



def obter_conversao_m3_ton(
    path_yaml: str | Path,
    idade: int,
) -> float:
    dados = carregar_yaml_modelos(path_yaml)

    tabela = (
        dados
        .get("parametros_operacionais", {})
        .get("conversao_m3_ton", {})
        .get("valores", {})
    )

    if not tabela:
        raise ErroScenarioEngine(
            "Tabela de conversao m3 ton nao encontrada."
        )

    idade_int = int(round(idade))

    if idade_int in tabela:
        return float(tabela[idade_int])

    idades = sorted(int(i) for i in tabela.keys())

    menor = min(idades)
    maior = max(idades)

    idade_ajustada = max(menor, min(maior, idade_int))

    return float(tabela[idade_ajustada])
