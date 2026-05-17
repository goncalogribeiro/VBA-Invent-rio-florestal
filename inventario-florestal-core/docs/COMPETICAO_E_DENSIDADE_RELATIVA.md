# Competição e Densidade Relativa

## Objetivo

Documentar a arquitetura de competição florestal e densidade relativa integrada à prognose.

---

# Conceito

O crescimento florestal depende fortemente da competição entre árvores.

A competição controla:

- crescimento diamétrico;
- mortalidade;
- estabilidade;
- fechamento do dossel;
- produtividade.

---

# Indicadores Principais

O sistema utilizará inicialmente:

| Indicador | Função |
|---|---|
| Reineke | densidade relativa |
| Hart-Becking | espaçamento relativo |
| N | lotação |
| G | ocupação estrutural |

---

# Reineke

## Conceito

Representa a relação entre:

- número de árvores;
- diâmetro médio.

---

# Fórmula

```text
log10(N) = log10(a) - 1.605 * log10(DAP)
```

---

# Uso

| Faixa | Interpretação |
|---|---|
| >45% | pré-desbaste |
| 25–35% | manejo ideal |
| <20% | baixa ocupação |

---

# Hart-Becking

## Conceito

Relaciona:

- espaçamento médio;
- altura dominante.

---

# Fórmula

```text
S% = (espacamento_medio / hdom) * 100
```

---

# Uso

| Faixa | Interpretação |
|---|---|
| <20 | superlotação |
| 20–35 | manejo adequado |
| >35 | baixa ocupação |

---

# Integração com Prognose

A competição deverá influenciar:

| Processo | Efeito |
|---|---|
| crescimento | redução/aumento |
| mortalidade | aumento |
| desbaste | gatilho |
| estabilidade | risco estrutural |
| Weibull | redistribuição |

---

# Integração com Manejo

O sistema deverá usar competição para:

- sugerir desbastes;
- validar intensidade;
- evitar superlotação;
- evitar subutilização do sítio.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| competição espacial | ✓ |
| vizinhança | ✓ |
| índice de Hegyi | ✓ |
| crown competition factor | ✓ |
| distância dependente | ✓ |

---

# Conclusão

A competição e a densidade relativa representam o mecanismo central que conecta crescimento, mortalidade e manejo dentro da prognose dinâmica.
