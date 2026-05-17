# Matriz de Covariância e Decomposição de Cholesky

## Objetivo

Documentar a evolução do Monte Carlo multivariado para simulações estatisticamente consistentes.

---

# Conceito

Variáveis florestais, econômicas e climáticas podem apresentar dependência estatística.

A matriz de correlação/covariância permite representar essa dependência.

---

# Problema da Aproximação Simples

A simulação com choques independentes ou correlação manual simplificada pode gerar cenários incoerentes.

Exemplo:

- crescimento alto junto com seca extrema;
- mortalidade baixa sob competição muito alta;
- produtividade alta sob evento climático severo.

---

# Solução Estatística

Usar:

```text
matriz de correlação
↓
decomposição de Cholesky
↓
choques correlacionados
↓
cenários multivariados
```

---

# Variáveis Prioritárias

| Variável | Tipo |
|---|---|
| crescimento | biométrica |
| mortalidade | populacional |
| preço | econômica |
| produtividade | estrutural |

---

# Matriz de Correlação

Exemplo conceitual:

| | crescimento | mortalidade | preço | produtividade |
|---|---:|---:|---:|---:|
| crescimento | 1.00 | -0.60 | 0.20 | 0.80 |
| mortalidade | -0.60 | 1.00 | -0.10 | -0.70 |
| preço | 0.20 | -0.10 | 1.00 | 0.30 |
| produtividade | 0.80 | -0.70 | 0.30 | 1.00 |

---

# Decomposição de Cholesky

A decomposição transforma variáveis normais independentes em variáveis correlacionadas.

---

# Integração

O sistema deverá gerar cenários consistentes para:

- prognose;
- VPL;
- fluxo de caixa;
- análise de risco;
- otimização robusta.

---

# Evolução Futura

Futuramente a matriz poderá ser estimada com:

- séries históricas;
- inventários remedições;
- dados climáticos;
- preços reais;
- calibração regional.

---

# Conclusão

A matriz de covariância e a decomposição de Cholesky representam a base estatística correta para simulações Monte Carlo multivariadas realistas.
