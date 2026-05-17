# Motor Financeiro Florestal

## Objetivo

Documentar a arquitetura financeira do simulador florestal.

Esta camada transforma:

```text
produção futura
```

em:

```text
viabilidade econômica
```

---

# Pipeline Econômico Atual

```text
Prognose
↓
Weibull
↓
Taper
↓
Sortimento
↓
Massa
↓
Receita
↓
Fluxo de Caixa
↓
VPL
↓
B/C
```

---

# Arquivo Principal

```text
src/inventario_florestal/economico/financial_engine.py
```

---

# Estruturas Implementadas

## FluxoCaixaAno

Representa um período econômico anual.

Campos:

| Campo | Descrição |
|---|---|
| ano | horizonte temporal |
| receita | entradas financeiras |
| custo | saídas financeiras |
| saldo | resultado líquido |

---

## ResultadoFinanceiro

Consolidação financeira completa.

Campos:

| Campo | Descrição |
|---|---|
| vpl | valor presente líquido |
| relacao_bc | benefício/custo |
| receita_total | soma das receitas |
| custo_total | soma dos custos |
| fluxo_caixa | estrutura anualizada |

---

# Indicadores Implementados

## Valor Presente Líquido

Formulação:

```text
VPL = Σ FCt / (1+i)^t
```

Objetivo:

- avaliar viabilidade econômica;
- comparar regimes de manejo;
- otimizar rotações.

---

## Relação Benefício/Custo

Formulação:

```text
B/C = Benefícios descontados / Custos descontados
```

Interpretação:

| Resultado | Interpretação |
|---|---|
| B/C > 1 | viável |
| B/C = 1 | equilíbrio |
| B/C < 1 | inviável |

---

# Filosofia Arquitetural

O sistema NÃO deve:

- misturar cálculos biométricos e financeiros;
- calcular indicadores diretamente em interfaces;
- utilizar parâmetros econômicos hardcoded.

O sistema DEVE:

- separar camadas;
- manter rastreabilidade matemática;
- permitir auditoria financeira.

---

# Integração Atual

```text
Scenario Engine
↓
Taper
↓
Receita
↓
Financial Engine
```

---

# Próximos Passos

## Econômico

- TIR;
- VET;
- análise de sensibilidade;
- análise de risco;
- otimização de manejo.

## Operacional

- múltiplos ciclos;
- multi-rotação;
- fluxo operacional por desbaste.
