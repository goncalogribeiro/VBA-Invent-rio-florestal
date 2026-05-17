# Desbaste Seletivo por N e por G com Efeito Individual

## Objetivo

Registrar a regra técnica comum aos desbastes seletivos controlados por número de árvores e por área basal.

---

# Conceito Central

Nos dois métodos, a escolha das árvores segue a mesma hierarquia qualitativa.

A diferença está apenas no critério de parada:

| Método | Gatilho de parada |
|---|---|
| seletivo por N | quantidade de árvores removidas |
| seletivo por G | área basal acumulada removida |

---

# Regra Biométrica Fundamental

Mesmo quando o gatilho é número de árvores, cada árvore removida carrega seus próprios atributos individuais:

- DAP;
- área basal individual;
- volume individual;
- qualidade.

Portanto, o remanescente deve ser calculado a partir das árvores que realmente ficaram no povoamento.

---

# Implicação para Desbaste por N

No desbaste seletivo por número de árvores:

```text
qualidade define a ordem
quantidade define a parada
DAP e gi definem o impacto estrutural real
```

Isso significa que remover 30% das árvores não implica remover exatamente 30% da área basal.

---

# Implicação para Desbaste por G

No desbaste seletivo por área basal:

```text
qualidade define a ordem
gi define o acúmulo
G alvo define a parada
```

---

# Fluxo Comum

```text
árvores individuais
↓
ordenação por qualidade
↓
seleção conforme critério de parada
↓
separação removidas/remanescentes
↓
cálculo real de N, G e volume removidos
↓
cálculo real de N, G e volume remanescentes
```

---

# Intensidade Nominal vs Intensidade Real

A intensidade informada pelo usuário é a intensidade nominal.

A intensidade real deve ser calculada após a seleção.

| Intensidade | Como calcular |
|---|---|
| N removido | n_removido / n_total |
| G removido | g_removido / g_total |
| volume removido | volume_removido / volume_total |

---

# Observação Crítica

O sistema não deve assumir que:

```text
30% de N = 30% de G = 30% de volume
```

Essa igualdade raramente ocorre em dados reais.

---

# Conclusão

A seleção seletiva por N e por G compartilha a mesma lógica qualitativa.

A diferença está no gatilho de parada, mas o impacto final sempre deve ser calculado pelos atributos individuais das árvores selecionadas.
