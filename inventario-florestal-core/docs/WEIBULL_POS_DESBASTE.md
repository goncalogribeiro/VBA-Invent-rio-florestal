# Weibull Pós-Desbaste

## Objetivo

Documentar a camada responsável por recalibrar a distribuição diamétrica após a remoção seletiva de árvores.

---

# Conceito

Após o desbaste, a distribuição diamétrica original não representa mais o povoamento.

O sistema deve usar as árvores remanescentes para recalcular:

- DAP médio;
- variância diamétrica;
- DAP mínimo;
- DAP máximo;
- parâmetros Weibull;
- nova frequência por classe.

---

# Fluxo

```text
árvores remanescentes
↓
extração dos DAPs
↓
estatísticas diamétricas
↓
Weibull MLE ou PRM
↓
nova distribuição diamétrica
↓
prognose futura
```

---

# Estratégia Inicial

A primeira implementação deverá usar os DAPs individuais remanescentes e ajustar Weibull por MLE.

Motivo:

- os dados individuais já existem após a seleção;
- MLE usa diretamente a distribuição observada;
- evita aproximação excessiva nesta etapa.

---

# Alternativa Futura

Também poderá ser usado PRM quando apenas atributos agregados estiverem disponíveis.

Fluxo PRM:

```text
D médio + variância + Dmin
↓
recuperação dos parâmetros Weibull
```

---

# Observação Crítica

A Weibull pós-desbaste não deve ser obtida apenas reduzindo N da Weibull original.

Isso seria incorreto porque:

- desbaste seletivo altera a forma da distribuição;
- remove classes específicas;
- muda a assimetria;
- muda a variância;
- altera o DAP mínimo efetivo.

---

# Saídas Esperadas

| Saída | Finalidade |
|---|---|
| parâmetros Weibull | nova distribuição |
| distribuição residual | prognose |
| DAP médio residual | estrutura |
| variância residual | forma |
| N residual | densidade |

---

# Conclusão

A Weibull pós-desbaste é o primeiro mecanismo matemático de resposta estrutural dinâmica do povoamento.
