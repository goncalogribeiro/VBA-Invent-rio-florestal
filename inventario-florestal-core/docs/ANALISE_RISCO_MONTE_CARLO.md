# Análise de Risco Monte Carlo

## Objetivo

Documentar a camada probabilística do simulador florestal.

Esta camada permite:

- simular incertezas;
- estimar distribuição de resultados;
- quantificar risco econômico;
- avaliar robustez de regimes de manejo.

---

# Filosofia

O manejo florestal NÃO deve:

- utilizar apenas cenários determinísticos;
- assumir estabilidade de preços;
- ignorar risco operacional.

O manejo florestal DEVE:

- modelar volatilidade;
- simular cenários futuros;
- quantificar probabilidade de perda.

---

# Variáveis Prioritárias

| Variável | Impacto |
|---|---|
| preço da madeira | muito alto |
| produtividade | muito alto |
| mortalidade | alto |
| taxa juros | alto |
| densidade | médio |

---

# Pipeline

```text
Parâmetros Base
↓
Distribuições Probabilísticas
↓
Simulações Aleatórias
↓
Fluxos Econômicos
↓
Distribuição do VPL
↓
Análise de Risco
```

---

# Resultados Esperados

| Indicador | Finalidade |
|---|---|
| média do VPL | expectativa econômica |
| desvio padrão | volatilidade |
| percentil 5% | risco extremo |
| percentil 95% | potencial máximo |
| probabilidade VPL<0 | risco financeiro |

---

# Próximos Passos

## Estatístico

- distribuição normal;
- triangular;
- lognormal;
- uniforme.

## Econômico

- VaR florestal;
- CVaR;
- análise probabilística de rotação.
