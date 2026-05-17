# Desbaste Seletivo por Área Basal

## Objetivo

Documentar o comportamento do desbaste seletivo controlado por área basal removida.

---

# Conceito

O desbaste seletivo por área basal segue a mesma lógica qualitativa do desbaste seletivo por número de árvores.

A diferença principal é:

| Método | Critério de parada |
|---|---|
| por árvores | percentual de N |
| por área basal | percentual de G |

---

# Ordem de Seleção

A ordem de remoção deverá permanecer:

| Prioridade | Classe |
|---|---|
| 1 | copa_quebrada |
| 2 | bifurcacao_baixa |
| 3 | macaco_prego |
| 4 | torta |
| 5 | bifurcacao_alta |

---

# Fluxo Operacional

selecionar piores árvores
↓
ordenar por prioridade qualitativa
↓
acumular área basal removida
↓
parar ao atingir G alvo

---

# Observação Biométrica

Este método é superior ao controle apenas por número de árvores.

Porque:

- considera estrutura do povoamento;
- considera dimensão individual;
- controla intensidade real do desbaste;
- reduz distorções estruturais.

---

# Tendências Esperadas

| Variável | Tendência |
|---|---|
| N | redução variável |
| G | controle preciso |
| Dg | aumento |
| valor médio árvore | aumento |
| sortimento nobre | aumento |

---

# Integração Futura

Futuramente o sistema deverá:

- ponderar qualidade + DAP;
- ponderar qualidade + competição;
- ponderar qualidade + dominância;
- integrar estabilidade mecânica;
- integrar risco fitossanitário.

---

# Conclusão

O desbaste seletivo por área basal representa uma aproximação mais realista do manejo operacional aplicado em povoamentos comerciais de Pinus.
