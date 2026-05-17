# Fluxo Econômico Temporal

## Objetivo

Documentar a arquitetura de fluxo econômico temporal integrada à prognose florestal.

---

# Conceito

O retorno econômico florestal ocorre ao longo do tempo.

O sistema deverá representar:

- custos anuais;
- receitas intermediárias;
- receitas finais;
- desbastes;
- fluxo de caixa.

---

# Componentes Econômicos

| Componente | Tipo |
|---|---|
| implantação | custo |
| manutenção | custo |
| proteção fitossanitária | custo |
| inventário | custo |
| desbaste | receita/custo |
| corte final | receita |

---

# Fluxo Temporal

```text
ano 0
↓
implantação
↓
manutenção
↓
desbastes
↓
receitas intermediárias
↓
corte final
↓
resultado econômico
```

---

# Receitas Intermediárias

Os desbastes deverão gerar:

- fluxo de caixa parcial;
- redução de risco financeiro;
- antecipação de receita.

---

# Integração com Sortimento

O sistema deverá usar:

- distribuição diamétrica;
- taper;
- sortimentos;
- preços por tonelada.

---

# Integração com Prognose

Cada ciclo deverá atualizar:

| Variável | Atualização |
|---|---|
| crescimento | anual |
| mortalidade | anual |
| competição | anual |
| receita | anual |
| custos | anual |

---

# Cenários Econômicos

O sistema deverá suportar:

| Cenário | Objetivo |
|---|---|
| pessimista | segurança |
| realista | planejamento |
| otimista | potencial máximo |

---

# Integração com YAML

Os cenários do YAML deverão controlar:

- preços;
- sortimentos;
- conversão m³→ton;
- regras operacionais.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| inflação | ✓ |
| juros variáveis | ✓ |
| Monte Carlo | ✓ |
| carbono | ✓ |
| risco climático | ✓ |

---

# Conclusão

O fluxo econômico temporal representa a camada responsável por transformar a prognose em planejamento financeiro florestal completo.
