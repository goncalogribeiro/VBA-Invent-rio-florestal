# Recalibração Weibull Residual Pós-Desbaste

## Objetivo

Documentar a recalibração da distribuição diamétrica após eventos de manejo.

---

# Conceito

Após um desbaste, o povoamento remanescente possui uma nova estrutura diamétrica.

Portanto, a distribuição Weibull original não deve ser apenas reduzida proporcionalmente.

O sistema deve recalibrar a distribuição com base nas árvores remanescentes.

---

# Fluxo Correto

```text
árvores remanescentes
↓
DAPs remanescentes
↓
ajuste Weibull MLE
↓
parâmetros residuais
↓
nova distribuição diamétrica
↓
prognose futura
```

---

# Por que usar MLE nesta etapa?

A máxima verossimilhança é adequada porque:

- usa dados individuais;
- captura mudança real de forma;
- evita aproximação grosseira;
- reflete remoções seletivas e sistemáticas.

---

# Saídas Esperadas

| Saída | Função |
|---|---|
| parâmetros Weibull residuais | nova forma da distribuição |
| distribuição residual | base para prognose |
| estatísticas residuais | auditoria |
| N residual | densidade |

---

# Observação Técnica

Quando não houver dados individuais, o sistema poderá usar PRM como alternativa.

Nesta etapa, a prioridade é MLE porque o sistema possui DAPs individuais remanescentes.

---

# Conclusão

A recalibração Weibull residual representa o primeiro mecanismo matemático completo de resposta estrutural pós-desbaste.
