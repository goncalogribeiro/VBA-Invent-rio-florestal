# Integração Seleção Qualitativa, Remoção e Remanescente

## Objetivo

Documentar a integração entre:

- seleção qualitativa;
- remoção por número de árvores;
- remoção por área basal;
- geração de árvores removidas;
- geração de árvores remanescentes;
- recálculo estrutural pós-desbaste.

---

# Diretriz Técnica

A seleção qualitativa deve ocorrer antes da redistribuição estrutural.

Fluxo correto:

```text
árvores individuais
↓
ordenação qualitativa
↓
seleção por critério de parada
↓
removidas + remanescentes
↓
recálculo estrutural
↓
prognose pós-desbaste
```

---

# Critérios de Remoção Suportados

| Critério | Descrição |
|---|---|
| arvores | remove percentual de N |
| area_basal | remove percentual de G |

---

# Hierarquia Qualitativa

A hierarquia vem dos parâmetros operacionais do YAML.

Ordem atual:

| Prioridade | Classe |
|---|---|
| 1 | copa_quebrada |
| 2 | bifurcacao_baixa |
| 3 | macaco_prego |
| 4 | torta |
| 5 | bifurcacao_alta |

---

# Saídas Esperadas

| Saída | Finalidade |
|---|---|
| removidas | receita intermediária |
| remanescentes | nova prognose |
| N removido | intensidade operacional |
| G removido | intensidade biométrica |
| volume removido | produção intermediária |
| estrutura remanescente | estado pós-desbaste |

---

# Observação Crítica

Esta camada ainda não representa a resposta completa de crescimento pós-desbaste.

Ela representa o primeiro elo operacional:

```text
quem sai e quem fica
```

A reação posterior do povoamento será tratada em camada própria.

---

# Próxima Etapa

A próxima camada deverá recalibrar a distribuição diamétrica remanescente por Weibull, usando as árvores remanescentes ou seus atributos agregados.
