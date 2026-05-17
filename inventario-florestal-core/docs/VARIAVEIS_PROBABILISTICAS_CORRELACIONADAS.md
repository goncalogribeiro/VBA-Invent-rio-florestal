# Variáveis Probabilísticas Correlacionadas

## Objetivo

Documentar a arquitetura de variáveis probabilísticas correlacionadas dentro da prognose florestal.

---

# Conceito

Os componentes do sistema florestal não variam independentemente.

Exemplos:

| Variável | Relação |
|---|---|
| seca | reduz crescimento |
| seca | aumenta mortalidade |
| crescimento | altera produtividade |
| produtividade | altera receita |
| preços | alteram VPL |

---

# Problema da Independência

Simular todas as variáveis isoladamente gera:

- distorções;
- cenários irreais;
- subestimação de risco.

---

# Estrutura Correta

```text
variáveis correlacionadas
↓
cenários integrados
↓
Monte Carlo multivariado
↓
risco realista
```

---

# Variáveis Prioritárias

| Variável | Tipo |
|---|---|
| crescimento | biométrica |
| mortalidade | populacional |
| preço | econômica |
| clima | ambiental |
| produtividade | estrutural |

---

# Correlações Esperadas

| Relação | Tendência |
|---|---|
| seca × crescimento | negativa |
| seca × mortalidade | positiva |
| produtividade × receita | positiva |
| competição × mortalidade | positiva |

---

# Integração com Prognose

A simulação deverá:

- atualizar crescimento;
- recalcular mortalidade;
- recalcular receitas;
- recalcular VPL.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| matrizes de covariância | ✓ |
| distribuições multivariadas | ✓ |
| clima histórico | ✓ |
| IA preditiva | ✓ |
| séries temporais | ✓ |

---

# Conclusão

As variáveis probabilísticas correlacionadas representam a camada responsável por transformar a simulação Monte Carlo em modelagem estratégica realista.
