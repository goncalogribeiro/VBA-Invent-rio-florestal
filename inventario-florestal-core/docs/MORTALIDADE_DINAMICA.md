# Mortalidade Dinâmica na Prognose Florestal

## Objetivo

Documentar a arquitetura de mortalidade dinâmica integrada ao crescimento e manejo.

---

# Conceito

O povoamento não cresce mantendo o mesmo número de árvores.

Ao longo do tempo ocorrem:

- mortalidade natural;
- mortalidade competitiva;
- mortalidade fitossanitária;
- mortalidade induzida pelo manejo.

---

# Papel da Mortalidade

A mortalidade altera diretamente:

| Variável | Impacto |
|---|---|
| N | densidade |
| G | área basal |
| Weibull | estrutura diamétrica |
| competição | crescimento |
| ICA | incremento |
| estabilidade | risco operacional |

---

# Integração Correta

A mortalidade deve ser integrada ao ciclo temporal.

```text
crescimento
↓
competição
↓
mortalidade
↓
recalcular estrutura
↓
novo ciclo
```

---

# Modelos Utilizados

O sistema utilizará inicialmente os modelos:

| Modelo | YAML |
|---|---|
| Clutter | N01 |
| Lenhart | N02 |
| Pienaar & Shiver | N03 |
| Burkhart & Sprinz | N04 |
| Acerbi Jr | N05 |
| Bailey modificado | N06 |

---

# Critérios de Seleção

Os modelos deverão participar de torneio biométrico.

Critérios:

- R² ajustado;
- Syx%;
- viés;
- estabilidade;
- coerência biológica.

---

# Mortalidade Competitiva

A mortalidade competitiva deverá considerar futuramente:

- densidade relativa;
- Reineke;
- Hart-Becking;
- competição local.

---

# Mortalidade Fitossanitária

Futuramente o sistema deverá incorporar:

| Evento | Impacto |
|---|---|
| Sirex noctilio | mortalidade seletiva |
| formigas | falhas |
| pulgões | redução vigor |
| vento | quebra |

---

# Observação Técnica

A mortalidade não deve ser aplicada apenas como percentual fixo.

Ela deve responder à:

- estrutura do povoamento;
- densidade;
- sítio;
- manejo;
- idade.

---

# Conclusão

A mortalidade dinâmica representa a camada responsável por transformar a prognose em um processo populacional completo, permitindo simular a evolução estrutural real do povoamento ao longo do tempo.
