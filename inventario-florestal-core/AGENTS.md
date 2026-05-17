# AGENTS.md — Inventário Florestal Core

## Objetivo

Este subprojeto contém a arquitetura científica principal do sistema de inventário florestal.

O foco é construir um motor biométrico modular, auditável e orientado a torneio estatístico de modelos.

---

# Regras obrigatórias

- Não utilizar modelos fixos.
- Toda equação deve participar de ranking.
- Toda equação deve possuir rastreabilidade bibliográfica.
- Modelos logarítmicos exigem correção de viés.
- Toda implementação deve possuir validação estatística.
- Não quebrar compatibilidade futura com a planilha VBA.
- Não misturar lógica biométrica com interface.

---

# Estrutura principal

## docs/

Documentação técnica e científica.

## data/modelos/

Banco estruturado de modelos biométricos.

## src/inventario_florestal/

Motores Python.

## tests/

Validação automatizada.

## vba/

Módulos exportados do Excel.

---

# Componentes prioritários

1. parser YAML de modelos;
2. motor universal de ranking;
3. regressão linear;
4. regressão não linear;
5. correção de viés;
6. taper;
7. sortimento;
8. prognose.

---

# Diretriz científica

As premissas biométricas devem ser baseadas prioritariamente em:

- artigos científicos;
- EMBRAPA;
- IPEF;
- UFPR;
- UDESC;
- UFSM;
- revistas científicas florestais;
- teses e dissertações.
