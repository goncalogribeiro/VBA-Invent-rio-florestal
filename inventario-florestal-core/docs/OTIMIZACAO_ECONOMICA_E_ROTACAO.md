# Otimização Econômica e Rotação Florestal

## Objetivo

Documentar a integração econômica da prognose florestal.

---

# Conceito

A melhor decisão silvicultural nem sempre corresponde ao maior volume.

O sistema deverá integrar:

- produtividade;
- receitas;
- custos;
- valor dos sortimentos;
- idade de corte.

---

# Rotação Técnica vs Econômica

| Tipo | Critério |
|---|---|
| rotação técnica | culminação do IMA |
| rotação econômica | maior retorno financeiro |

---

# Componentes Econômicos

O sistema deverá considerar:

| Variável | Uso |
|---|---|
| preço por sortimento | receita |
| conversão m³→ton | comercialização |
| custos operacionais | viabilidade |
| taxa de desconto | VPL |
| receitas intermediárias | desbastes |

---

# Integração com YAML

Os cenários do YAML já fornecem:

- sortimentos;
- comprimentos;
- diâmetros mínimos;
- preço por tonelada;
- conversão m³→ton.

---

# Valor Médio Ponderado

O valor médio por tonelada deverá ser ponderado.

O sistema não deverá usar média simples.

A ponderação deverá considerar:

- participação volumétrica;
- participação mássica;
- valor individual do sortimento.

---

# Fluxo Econômico

```text
prognose
↓
sortimento
↓
receita
↓
custos
↓
fluxo de caixa
↓
VPL
↓
rotação ótima
```

---

# Integração com Manejo

O sistema deverá comparar:

| Estratégia | Resultado |
|---|---|
| sem desbaste | maior volume bruto |
| desbaste moderado | maior valor agregado |
| desbaste intenso | maior diâmetro individual |

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| carbono | ✓ |
| risco operacional | ✓ |
| otimização multiobjetivo | ✓ |
| Monte Carlo | ✓ |
| análise espacial | ✓ |

---

# Conclusão

A otimização econômica representa a camada responsável por transformar a prognose biométrica em suporte real ao planejamento florestal empresarial.
