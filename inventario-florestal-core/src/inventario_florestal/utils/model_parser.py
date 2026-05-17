"""Parser do catalogo YAML de modelos biometricos."""

from __future__ import annotations

from pathlib import Path

import yaml

from inventario_florestal.modelos.schema import CatalogoModelos


class ErroCatalogoModelos(Exception):
    """Erro relacionado ao catalogo de modelos."""



def carregar_catalogo(caminho_yaml: str | Path) -> CatalogoModelos:
    """Carrega e valida um catalogo de modelos biometricos.

    Parameters
    ----------
    caminho_yaml:
        Caminho do arquivo YAML.

    Returns
    -------
    CatalogoModelos
        Catalogo validado.
    """

    caminho = Path(caminho_yaml)

    if not caminho.exists():
        raise ErroCatalogoModelos(
            f"Arquivo de catalogo nao encontrado: {caminho}"
        )

    with caminho.open("r", encoding="utf-8") as arquivo:
        dados = yaml.safe_load(arquivo)

    if not isinstance(dados, dict):
        raise ErroCatalogoModelos(
            "Estrutura YAML invalida: esperado dicionario raiz"
        )

    return CatalogoModelos.model_validate(dados)
