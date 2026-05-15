# Fluxo Operacional

# Objetivo

Este documento define o fluxo operacional oficial do sistema de inventário florestal.

O objetivo é padronizar:

- entrada de dados;
- processamento biométrico;
- geração de modelos;
- auditoria estatística;
- prognose;
- relatórios.

---

# Fluxo Geral

Campo → Validação → Hipsometria → Volumetria → Taper → Sortimento → Estatísticas → Prognose → Relatórios

---

# Etapa 1 — Entrada de Dados

## Dados mínimos obrigatórios

- projeto;
- data do inventário;
- data de plantio;
- parcela;
- árvore;
- espécie;
- DAP ou CAP;
- altura total;
- situação da árvore.

---

# Etapa 2 — Validação

## Regras mínimas

- conversão CAP → DAP;
- remoção de duplicidades;
- verificação de valores extremos;
- consistência de unidades;
- verificação de alturas incompatíveis;
- consistência de idade.

---

# Etapa 3 — Hipsometria

## Objetivo

Estimativa de altura total para árvores sem medição de altura.

## Processo

1. ajustar múltiplas equações;
2. avaliar estatísticas;
3. gerar resíduos;
4. ranquear modelos;
5. selecionar melhor modelo;
6. estimar alturas faltantes.

---

# Etapa 4 — Volumetria

## Objetivo

Estimativa volumétrica individual e por hectare.

## Fontes possíveis

- fator de forma;
- cubagem rigorosa;
- regressões volumétricas;
- taper.

---

# Etapa 5 — Taper

## Objetivo

Estimar diâmetros ao longo do fuste.

## Aplicações

- sortimento;
- volume comercial;
- prognose;
- multiprodutos.

---

# Etapa 6 — Sortimento

## Objetivo

Classificar toras conforme:

- comprimento;
- diâmetro mínimo;
- cenário econômico;
- produto final.

## Cenários

- pessimista;
- realista;
- otimista.

---

# Etapa 7 — Estatísticas

## Indicadores mínimos

- árvores por hectare;
- DAP médio;
- altura média;
- área basal;
- volume;
- distribuição diamétrica;
- IMA;
- incremento;
- densidade.

---

# Etapa 8 — Prognose

## Componentes

- crescimento;
- mortalidade;
- sobrevivência;
- desbaste;
- distribuição diamétrica;
- produção.

---

# Etapa 9 — Relatórios

## Saídas previstas

- relatórios técnicos;
- dashboards;
- tabelas operacionais;
- relatórios científicos;
- auditoria estatística.

---

# Diretrizes Operacionais

- preservar rastreabilidade;
- manter compatibilidade histórica;
- registrar versões de modelos;
- documentar alterações críticas.
