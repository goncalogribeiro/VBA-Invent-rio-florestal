# Análise Econômica Avançada

## Objetivo

Documentar a camada avançada de engenharia econômica do simulador florestal.

Esta camada integra:

- produção futura;
- fluxo de caixa;
- valuation;
- análise financeira.

---

# Pipeline Econômico Completo

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
↓
TIR
↓
VET
```

---

# Arquivos Principais

```text
financial_engine.py
advanced_financial_engine.py
```

---

# Indicadores Implementados

| Indicador | Status |
|---|---|
| VPL | operacional |
| B/C | operacional |
| TIR | operacional |
| VET | operacional |

---

# TIR

A Taxa Interna de Retorno:

- mede rentabilidade do projeto;
- compara alternativas de manejo;
- suporta decisões de investimento.

Método implementado:

```text
Newton-Raphson
```

---

# VET

O Valor Esperado da Terra:

- estima valor econômico da terra florestal;
- utiliza conceito clássico de Faustmann;
- permite comparação patrimonial.

---

# Filosofia Arquitetural

O sistema NÃO deve:

- misturar cálculos financeiros e biométricos;
- executar cálculos financeiros em interfaces;
- duplicar fórmulas econômicas.

O sistema DEVE:

- centralizar cálculos;
- manter rastreabilidade matemática;
- permitir auditoria econômica.

---

# Próximos Passos

## Econômico

- análise de sensibilidade;
- análise de risco;
- Monte Carlo;
- otimização de rotação.

## Operacional

- múltiplos desbastes;
- multi-rotação;
- regimes alternativos.
