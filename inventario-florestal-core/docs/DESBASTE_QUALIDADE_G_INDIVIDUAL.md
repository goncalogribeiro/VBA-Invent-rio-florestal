# Desbaste por Qualidade com Controle por Area Basal Individual

## Objetivo

Registrar a regra operacional para desbaste seletivo controlado por area basal removida.

---

# Conceito Central

Quando o desbaste for controlado por area basal, a escolha das arvores continua seguindo a hierarquia qualitativa definida no YAML.

Entretanto, cada arvore removida contribui para o alvo de remocao conforme sua area basal individual.

Portanto:

```text
qualidade define a ordem
DAP define a contribuicao em G
```

---

# Area Basal Individual

A area basal individual e funcao direta do DAP:

```text
gi = pi * DAP^2 / 40000
```

Onde:

| Variavel | Unidade |
|---|---|
| DAP | cm |
| gi | m2/arvore |

---

# Fluxo Correto

```text
arvores individuais
↓
ordenacao por qualidade
↓
acumulo de gi individual
↓
parada ao atingir G alvo
↓
separacao removidas/remanescentes
```

---

# Exemplo Conceitual

Se o alvo for remover 30% da area basal:

```text
G alvo removido = G total * 0.30
```

O sistema deve selecionar arvores na ordem qualitativa e somar `gi` ate atingir ou ultrapassar o alvo.

---

# Implicacao Biométrica

Duas arvores de mesma classe qualitativa podem ter impactos diferentes na remocao por G, pois possuem DAPs diferentes.

Assim:

- uma arvore grossa defeituosa pode atingir rapidamente o alvo de G;
- muitas arvores finas defeituosas podem ser necessarias para atingir o mesmo alvo.

---

# Diretriz de Implementacao

A primeira versao deve manter:

- prioridade qualitativa como criterio primario;
- area basal individual como criterio de acumulacao;
- parada ao atingir o percentual alvo de G.

---

# Criterios Futuros

No momento correto, o sistema podera evoluir para score multicriterio com:

| Fator | Finalidade |
|---|---|
| qualidade | defeito e valor potencial |
| DAP | dimensao estrutural |
| gi | impacto em G |
| volume | impacto produtivo |
| dominancia | posicao sociologica |
| competicao | resposta pos-desbaste |
| sanidade | risco fitossanitario |
| estabilidade | risco mecanico |

---

# Conclusao

O desbaste por area basal deve usar a qualidade para ordenar a remocao e a area basal individual para controlar a intensidade real do desbaste.
