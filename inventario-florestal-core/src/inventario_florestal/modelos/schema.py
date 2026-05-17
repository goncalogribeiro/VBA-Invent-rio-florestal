"""Schemas para modelos biometricos.

Este modulo define a estrutura validavel dos modelos descritos em YAML.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


GrupoModelo = Literal[
    "hipsometria",
    "volumetria",
    "taper",
    "sitio",
    "weibull",
    "sobrevivencia",
    "prognose",
    "sortimento",
]

TipoRegressao = Literal[
    "linear",
    "linear_sem_intercepto",
    "nao_linear",
    "nao_linear_segmentada",
]

StatusValidacao = Literal[
    "pendente",
    "validado",
    "experimental",
    "revisar_formula",
    "revisar_fonte",
    "nao_implementar",
]


class FonteModelo(BaseModel):
    """Fonte bibliografica resumida do modelo."""

    autores: str
    ano: int | None = None
    titulo: str | None = None
    doi: str | None = None
    observacao: str | None = None


class ConfiguracaoNLS(BaseModel):
    """Configuracao para ajuste nao linear controlado."""

    funcao_registrada: str
    chute_inicial: list[float]
    limites_inferiores: list[float] | None = None
    limites_superiores: list[float] | None = None
    max_iteracoes: int = 10000


class ModeloBiometrico(BaseModel):
    """Definicao estruturada de uma equacao biometrica."""

    id: str
    grupo: GrupoModelo
    nome: str
    formula: str

    variavel_dependente: str
    variaveis_independentes: list[str] = Field(default_factory=list)
    parametros: list[str] = Field(default_factory=list)

    tipo_regressao: TipoRegressao
    linearizavel: bool
    eh_logaritmico: bool
    base_logaritmo: Literal["ln", "log10"] | None = None

    metodo_ajuste: str | None = None
    metodo_inverso: str | None = None
    metodo_correcao_vies: str | None = None
    nls: ConfiguracaoNLS | None = None

    especie: list[str] = Field(default_factory=list)
    regiao: list[str] = Field(default_factory=list)

    fonte: FonteModelo | list[FonteModelo] | None = None
    status_validacao: StatusValidacao = "pendente"
    observacoes: list[str] = Field(default_factory=list)
    metadados: dict[str, Any] = Field(default_factory=dict)


class CatalogoModelos(BaseModel):
    """Catalogo completo de modelos biometricos."""

    metadata: dict[str, Any] = Field(default_factory=dict)
    modelos: list[ModeloBiometrico] = Field(default_factory=list)

    def filtrar_por_grupo(self, grupo: GrupoModelo) -> list[ModeloBiometrico]:
        """Retorna modelos pertencentes a um grupo biometrico."""
        return [modelo for modelo in self.modelos if modelo.grupo == grupo]

    def buscar_por_id(self, modelo_id: str) -> ModeloBiometrico | None:
        """Busca um modelo pelo identificador."""
        for modelo in self.modelos:
            if modelo.id == modelo_id:
                return modelo
        return None
