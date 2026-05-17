# Aplicador de Desbaste

## Objetivo

Documentar a arquitetura do motor responsável por aplicar eventos de manejo sobre o povoamento.

Esta camada representa o núcleo do simulador silvicultural dinâmico.

---

# Responsabilidades

O Aplicador de Desbaste deverá:

- receber o estado atual do povoamento;
- aplicar um EventoManejo;
- remover árvores;
- recalcular estrutura do povoamento;
- gerar povoamento removido;
- gerar povoamento remanescente;
- preparar o estado para nova prognose.

---

# Fluxo Conceitual

```text
Povoamento Atual
↓
EventoManejo
↓
AplicadorDeDesbaste
↓
Removido + Remanescente
↓
Nova Prognose
```

---

# Entradas Esperadas

| Entrada | Finalidade |
|---|---|
| Weibull atual | distribuição diamétrica |
| N | árvores/ha |
| G | área basal |
| Dg | diâmetro quadrático |
| Hd | altura dominante |
| cenário operacional | sortimento |
| taper | volumes e toras |

---

# Saídas Esperadas

| Saída | Finalidade |
|---|---|
| árvores removidas | produção do desbaste |
| árvores remanescentes | continuidade da rotação |
| nova distribuição | estado pós-desbaste |
| receita do desbaste | fluxo econômico |

---

# Tipos de Aplicação

## Sistemático

Remoção proporcional fixa.

Exemplo:

```text
remover 20% das árvores
```

---

## Por Baixo

Remove preferencialmente:

- menores DAPs;
- classes inferiores;
- árvores dominadas.

---

## Pelo Alto

Remove competidoras dominantes.

Mais complexo.

Exige lógica de competição.

---

## Misto

Combina:

- sistemático;
- seletivo.

---

# Observação Crítica

A redistribuição diamétrica pós-desbaste NÃO deve:

- simplesmente reduzir N;
- manter Weibull fixa;
- ignorar reação do povoamento.

O sistema deverá recalcular:

- distribuição;
- Dg;
- G;
- potencial de crescimento.

---

# Integrações Futuras

| Camada | Integração |
|---|---|
| Weibull | recalibração |
| prognose | crescimento futuro |
| taper | novo perfil do fuste |
| econômico | receita do desbaste |
| Monte Carlo | risco operacional |

---

# Conclusão

O Aplicador de Desbaste representa o núcleo da dinâmica silvicultural do simulador.

A partir dele, o projeto deixa de ser apenas biométrico-econômico e passa a representar explicitamente a dinâmica estrutural do povoamento ao longo do tempo.
