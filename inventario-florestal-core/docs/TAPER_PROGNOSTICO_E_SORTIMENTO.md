# Taper Prognóstico e Estrutura de Sortimento

## Objetivo

Documentar a arquitetura do taper prognóstico e sua integração com a prognose diamétrica.

Esta camada transforma:

```text
classes diamétricas futuras
```

em:

```text
produtos florestais futuros
```

---

# Pipeline Atual

```text
Estado Atual
↓
Prognose Estrutural
↓
Weibull
↓
Distribuição Diamétrica
↓
Classe Diamétrica
↓
Taper Prognóstico
↓
Toras
↓
Volume
```

---

# Arquivo Principal

```text
taper/prognostic_taper.py
```

---

# Filosofia Biométrica

O sistema NÃO deve:

- estimar apenas volume total;
- utilizar árvore média fictícia;
- ignorar geometria do fuste.

O sistema DEVE:

- simular toras;
- respeitar ponta fina;
- priorizar produtos de maior valor;
- manter consistência geométrica.

---

# Estrutura do Taper

A implementação atual utiliza:

```text
d = dap * ((1 - h/H)^alpha)
```

Onde:

| Variável | Significado |
|---|---|
| d | diâmetro na altura h |
| dap | diâmetro à altura do peito |
| H | altura total |
| alpha | fator de afilamento |

---

# Fator de Afilamento

Estrutura atual:

```text
alpha = 0.53 / fator_forma
```

Objetivo:

- manter compatibilidade biométrica com o sistema VBA original;
- representar afilamento médio do povoamento.

---

# Estrutura das Toras

Classe:

```python
ToraSortimento
```

Campos:

| Campo | Função |
|---|---|
| comprimento | comprimento da tora |
| diametro_ponta_fina | classificação comercial |
| sortimento | produto |
| volume_m3 | volume da tora |

---

# Estratégia de Alocação

As toras são testadas:

```text
maior valor → menor valor
```

Exemplo:

```text
Laminação
↓
Serraria
↓
Celulose
↓
Energia
```

---

# Critério de Classificação

O enquadramento comercial é feito por:

```text
diâmetro da ponta fina
```

E NÃO:

- pelo DAP;
- pelo diâmetro médio.

---

# Cálculo Volumétrico

A implementação atual utiliza:

```text
V = (π/40000) * d_med² * comprimento
```

Onde:

| Variável | Significado |
|---|---|
| d_med | média entre base e topo |
| comprimento | comprimento da tora |

---

# Integração Planejada

## Próxima Camada

```text
Toras
↓
Conversão m³ → ton
↓
Receita
↓
Fluxo de caixa
↓
Indicadores econômicos
```

---

# Estado Atual

| Componente | Status |
|---|---|
| taper prognóstico | operacional |
| toras simuladas | operacional |
| volume por tora | operacional |
| volume por hectare | operacional |

---

# Próximos Passos

## Prioridade Alta

- motor de sortimento prognóstico;
- conversão massa;
- receita futura;
- indicadores econômicos.

## Prioridade Média

- taper segmentado;
- taper Kozak;
- taper Bi;
- taper variável.
