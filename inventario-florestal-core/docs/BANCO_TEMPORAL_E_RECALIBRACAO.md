# Banco Temporal e Recalibração Contínua

## Objetivo

Documentar a arquitetura de persistência temporal e recalibração contínua da prognose florestal.

---

# Conceito

A prognose deverá evoluir continuamente conforme novos dados forem adicionados.

O sistema deverá armazenar:

- inventários;
- remedições;
- erros históricos;
- recalibrações;
- cenários.

---

# Estrutura Geral

```text
inventários
↓
armazenamento histórico
↓
comparação temporal
↓
recalibração
↓
aprendizado contínuo
```

---

# Papel do Banco Temporal

O banco temporal permitirá:

- rastreabilidade;
- auditoria;
- evolução histórica;
- regionalização;
- aprendizado adaptativo.

---

# Informações Prioritárias

| Informação | Uso |
|---|---|
| crescimento observado | recalibração |
| mortalidade observada | sobrevivência |
| produtividade | prognose |
| preços históricos | economia |
| clima histórico | risco |

---

# Integração com Prognose

Cada novo inventário poderá:

- recalibrar Weibull;
- recalibrar crescimento;
- recalibrar mortalidade;
- recalibrar economia.

---

# Persistência Temporal

O sistema deverá armazenar:

| Entidade | Temporalidade |
|---|---|
| parcelas | permanente |
| árvores | permanente |
| medições | periódica |
| manejo | histórica |
| prognoses | histórica |

---

# Benefícios

A abordagem temporal permitirá:

- redução de erro;
- adaptação regional;
- melhoria contínua;
- aprendizado estatístico.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| data warehouse | ✓ |
| machine learning | ✓ |
| IA preditiva | ✓ |
| séries climáticas | ✓ |
| autoajuste automático | ✓ |

---

# Conclusão

O banco temporal e a recalibração contínua representam a infraestrutura responsável por transformar o sistema em uma plataforma evolutiva de prognose florestal.
