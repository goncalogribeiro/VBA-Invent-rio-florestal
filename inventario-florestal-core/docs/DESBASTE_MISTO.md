# Regime de Desbaste Misto

## Objetivo

Formalizar a arquitetura operacional e biométrica do desbaste misto.

---

# Conceito

O desbaste misto combina:

| Etapa | Função |
|---|---|
| sistemática | abertura operacional |
| seletiva | refinamento biométrico |

---

# Fluxo Correto

```text
remoção sistemática
↓
recalcular removido parcial
↓
remoção seletiva complementar
↓
atingir meta final
↓
remanescente estrutural
```

---

# Etapa Sistemática

A etapa sistemática deve:

- remover linhas;
- remover posições fixas;
- abrir corredores;
- permitir mecanização.

Exemplos:

| Regime | Operação |
|---|---|
| 5a linha | remove 1 linha a cada 5 |
| 7a linha | remove 1 linha a cada 7 |

---

# Etapa Seletiva

Após a remoção sistemática:

- aplicar seleção qualitativa;
- usar critérios biométricos;
- completar intensidade alvo.

---

# Critérios Biométricos

A etapa seletiva deve considerar:

| Critério | Uso |
|---|---|
| qualidade | prioridade de remoção |
| DAP | dimensão estrutural |
| gi | impacto em G |
| volume | impacto produtivo |

---

# Regra Crítica

O sistema não deve somar intensidades cegamente.

Exemplo incorreto:

```text
20% sistemático + 20% seletivo = 40%
```

Exemplo correto:

```text
meta final = 30%
20% já removido
seletivo remove apenas o restante
```

---

# Controle por N e por G

O sistema deverá suportar:

| Método | Critério de parada |
|---|---|
| misto por N | quantidade final |
| misto por G | área basal final |

---

# Estrutura Residual

Após o desbaste misto:

- recalcular N;
- recalcular G;
- recalcular Dg;
- recalcular Weibull residual.

---

# Limitação Atual

A primeira implementação ainda não modela:

- competição espacial explícita;
- coordenadas de linhas;
- influência espacial da mecanização.

A primeira versão é estrutural e biométrica.

---

# Evolução Futura

Futuramente o sistema poderá:

- usar coordenadas;
- modelar vizinhança;
- modelar competição espacial;
- simular corredores reais.

---

# Conclusão

O desbaste misto deve funcionar como um sistema em duas etapas:

- sistemática para operacionalidade;
- seletiva para qualidade biométrica.

A intensidade final deve ser controlada pelo resultado total das duas fases combinadas.
