# Otimização de Manejo Florestal

## Objetivo

Documentar a camada de otimização automática do simulador florestal.

Esta camada permite:

- comparar regimes silviculturais;
- selecionar rotações ótimas;
- comparar cenários operacionais;
- maximizar retorno econômico;
- minimizar risco.

---

# Filosofia

O sistema NÃO deve:

- depender de seleção manual de regimes;
- utilizar apenas indicadores isolados;
- ignorar risco econômico.

O sistema DEVE:

- comparar múltiplos cenários;
- integrar biometria e economia;
- selecionar automaticamente os melhores resultados.

---

# Pipeline

```text
Prognose
↓
Taper
↓
Sortimento
↓
Receita
↓
Fluxo Econômico
↓
VPL/TIR/VET
↓
Monte Carlo
↓
Otimização
```

---

# Critérios de Seleção

| Critério | Objetivo |
|---|---|
| maior VPL | maximizar retorno |
| maior TIR | maximizar eficiência |
| maior VET | maximizar valor da terra |
| menor risco | reduzir volatilidade |
| menor probabilidade negativa | aumentar robustez |

---

# Variáveis de Manejo

| Variável | Impacto |
|---|---|
| idade corte | muito alto |
| intensidade desbaste | muito alto |
| número de desbastes | alto |
| cenário operacional | alto |
| densidade inicial | médio |

---

# Próximos Passos

## Operacional

- otimização multiobjetivo;
- fronteira eficiente;
- risco-retorno.

## Matemático

- algoritmos genéticos;
- simulated annealing;
- busca heurística.
