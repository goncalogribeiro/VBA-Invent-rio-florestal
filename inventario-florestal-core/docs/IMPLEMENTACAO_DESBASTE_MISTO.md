# Implementação Operacional do Desbaste Misto

## Objetivo

Documentar a implementação computacional do desbaste misto.

---

# Arquivo Principal

```text
src/inventario_florestal/manejo/mixed_thinning.py
```

---

# Estrutura Atual

A implementação atual opera em duas fases.

| Fase | Função |
|---|---|
| sistemática | remoção operacional geométrica |
| seletiva | complementação biométrica |

---

# Fase Sistemática

Função:

```python
remover_sistematico_por_percentual()
```

---

# Comportamento Atual

A primeira implementação utiliza:

```text
remoção simplificada por índice
```

Objetivo:

- representar corredores operacionais;
- simular abertura mecanizada;
- evitar dependência espacial prematura.

---

# Limitação Atual

Ainda não modela:

- coordenadas espaciais;
- linhas reais;
- orientação do plantio;
- competição espacial.

---

# Evolução Planejada

Futuramente deverá suportar:

| Recurso | Planejamento |
|---|---|
| coordenadas UTM | futuro |
| linhas reais | futuro |
| vizinhança | futuro |
| competição espacial | futuro |
| corredores reais | futuro |

---

# Fase Seletiva Complementar

Após a etapa sistemática:

- calcula remoção parcial;
- calcula intensidade residual necessária;
- aplica seleção qualitativa complementar.

---

# Critérios Utilizados

A seleção complementar utiliza:

| Critério | Uso |
|---|---|
| qualidade | prioridade |
| DAP | efeito estrutural |
| gi | efeito em G |
| volume | efeito produtivo |

---

# Controle por Meta

O sistema suporta:

| Método | Critério Final |
|---|---|
| misto por N | número de árvores |
| misto por G | área basal |

---

# Regra Fundamental

A intensidade seletiva complementar é calculada considerando o que já foi removido pela etapa sistemática.

Exemplo:

```text
meta final = 35%
remoção sistemática = 20%
seletiva complementar ≠ 35%
```

O seletivo remove apenas o necessário para completar a meta.

---

# Variáveis Geradas

O sistema retorna:

| Variável | Descrição |
|---|---|
| sistematicas_removidas | árvores removidas sistematicamente |
| seletivas_removidas | árvores removidas seletivamente |
| remanescentes | estrutura residual |
| intensidade_n_real | intensidade real por N |
| intensidade_g_real | intensidade real por G |
| volume_removido_total | volume total removido |

---

# Integração Futura

A estrutura residual será usada por:

- Weibull residual;
- prognose;
- ICA;
- IMA;
- competição;
- crescimento compensatório.

---

# Conclusão

A implementação atual do desbaste misto estabelece a primeira camada operacional completa do manejo híbrido no sistema.

Ela já permite:

- simulação sistemática;
- seleção biométrica complementar;
- controle por N;
- controle por G;
- rastreabilidade estrutural do remanescente.
