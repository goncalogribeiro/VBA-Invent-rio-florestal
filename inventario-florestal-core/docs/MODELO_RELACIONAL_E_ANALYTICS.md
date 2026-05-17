# Modelo Relacional e Analytics Corporativo

## Objetivo

Documentar a arquitetura relacional corporativa e analytics integrado da plataforma de prognose florestal.

---

# Conceito

A plataforma deverá utilizar um modelo relacional estruturado para garantir:

- rastreabilidade;
- integridade;
- auditoria;
- analytics;
- escalabilidade.

---

# Estrutura Geral

```text
inventários
↓
banco relacional
↓
analytics
↓
dashboards
↓
BI corporativo
```

---

# Entidades Principais

| Entidade | Função |
|---|---|
| fazendas | gestão territorial |
| talhões | unidade operacional |
| parcelas | inventário |
| árvores | biometria |
| medições | temporalidade |
| prognoses | simulações |
| manejo | operações |
| economia | receitas/custos |

---

# Relacionamentos

O sistema deverá permitir:

- histórico por árvore;
- histórico por parcela;
- histórico por talhão;
- rastreabilidade de manejo;
- rastreabilidade econômica.

---

# Analytics

O sistema deverá gerar:

| Indicador | Uso |
|---|---|
| ICA | produtividade |
| IMA | culminação |
| VPL | economia |
| mortalidade | sobrevivência |
| risco | robustez |
| carbono | ESG |

---

# Dashboards

Os dashboards deverão permitir:

- visualização temporal;
- comparação entre cenários;
- comparação entre manejos;
- análise de risco;
- indicadores FSC.

---

# Integração com FSC

A arquitetura deverá suportar:

- rastreabilidade;
- auditoria;
- governança;
- compliance;
- histórico operacional.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| APIs | ✓ |
| cloud | ✓ |
| IA | ✓ |
| GIS | ✓ |
| sensoriamento remoto | ✓ |

---

# Conclusão

O modelo relacional e analytics corporativo representam a infraestrutura responsável por transformar a plataforma em um sistema integrado de inteligência florestal.
