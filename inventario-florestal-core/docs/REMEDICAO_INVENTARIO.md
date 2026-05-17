# Arquitetura de Remedição de Inventário

## Objetivo

Definir como o sistema deve identificar e tratar remedições de inventário florestal.

---

# Conceito

Uma remedição é uma nova medição realizada sobre um inventário anterior, mantendo vínculo temporal e estrutural com o povoamento.

A remedição deve alimentar:

- prognose;
- recalibração biométrica;
- crescimento;
- mortalidade;
- atualização de modelos.

---

# Estratégia Recomendada

O sistema deve usar:

| Camada | Finalidade |
|---|---|
| detecção automática | identificar possíveis vínculos |
| confirmação do usuário | validar operação |

---

# Motivo

Apenas detecção automática pode gerar erros.

Exemplos:

| Situação | Risco |
|---|---|
| mesmo projeto com talhão novo | falso positivo |
| parcelas renumeradas | pareamento incorreto |
| mudança de área | ambiguidade |
| inventário parcial | inconsistência |

---

# Critérios de Detecção

O sistema deverá analisar:

| Campo | Uso |
|---|---|
| projeto | comparação principal |
| talhão | vínculo estrutural |
| parcela | remedição direta |
| data inventário | ordem temporal |
| data plantio | validação |
| área | conferência |
| coordenadas | validação espacial futura |

---

# Fluxo Operacional

```text
importação
↓
busca de inventários compatíveis
↓
identificação de possível remedição
↓
confirmação do usuário
↓
vinculação histórica
```

---

# Opções do Usuário

Quando houver correspondência:

```text
1. Novo inventário
2. Remedição
3. Substituição/correção
```

---

# Consequências Biométricas

Quando confirmado como remedição:

- atualizar crescimento;
- recalcular ICA;
- recalcular IMA;
- atualizar Weibull;
- recalibrar prognose;
- validar equações ativas.

---

# Diretriz Importante

As equações vencedoras não devem permanecer eternamente fixas.

Remedições deverão permitir:

- revalidação;
- novo torneio;
- recalibração adaptativa.

---

# Conclusão

O sistema deverá tratar remedições como eventos históricos vinculados ao mesmo povoamento, mantendo rastreabilidade completa da evolução estrutural do inventário.
