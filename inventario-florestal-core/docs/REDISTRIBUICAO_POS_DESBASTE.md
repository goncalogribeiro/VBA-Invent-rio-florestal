# Redistribuição Estrutural Pós-Desbaste

## Objetivo

Documentar a arquitetura biométrica responsável por recalcular a estrutura do povoamento após eventos de desbaste.

Esta camada representa o início da dinâmica estrutural real do simulador silvicultural.

---

# Problema Biométrico

Após um desbaste:

- a distribuição diamétrica muda;
- a competição muda;
- o crescimento futuro muda;
- a relação entre N, G e Dg muda.

Portanto:

```text
reduzir apenas N NÃO é suficiente
```

---

# Diretriz Técnica

O sistema NÃO deve:

- manter Weibull fixa;
- manter Dg fixo;
- manter distribuição original;
- ignorar o tipo de desbaste.

O sistema DEVE:

- recalcular estrutura remanescente;
- recalcular distribuição;
- recalcular parâmetros da Weibull;
- atualizar Dg;
- atualizar G;
- permitir reação pós-desbaste.

---

# Efeitos Esperados por Tipo de Desbaste

## Por Baixo

Tendências esperadas:

| Variável | Tendência |
|---|---|
| N | forte redução |
| G | redução moderada |
| Dg | aumento |
| competição | redução |
| crescimento individual | aumento |

---

## Pelo Alto

Tendências esperadas:

| Variável | Tendência |
|---|---|
| N | redução moderada |
| G | forte redução |
| Dg | pouco aumento |
| heterogeneidade | aumento |

---

## Sistemático

Tendências esperadas:

| Variável | Tendência |
|---|---|
| N | redução proporcional |
| G | redução proporcional |
| Dg | pouca alteração inicial |

---

# Estratégia Inicial de Implementação

A primeira versão deverá:

- recalcular N;
- recalcular G;
- recalcular Dg simplificado;
- manter Hd temporariamente estável.

---

# Estratégia Avançada Futura

Etapas futuras:

| Camada | Objetivo |
|---|---|
| Weibull dinâmica | nova distribuição |
| prognose pós-desbaste | novo crescimento |
| mortalidade dependente densidade | competição |
| ICA/IMA pós-intervenção | resposta silvicultural |

---

# Observação Crítica

A redistribuição estrutural é uma das partes mais complexas do projeto.

Ela depende de:

- espécie;
- sítio;
- idade;
- intensidade;
- genética;
- histórico silvicultural.

Portanto:

as primeiras versões deverão ser conservadoras e auditáveis.

---

# Conclusão

A redistribuição pós-desbaste representa a transição do simulador de um sistema biométrico estático para um simulador silvicultural dinâmico real.
