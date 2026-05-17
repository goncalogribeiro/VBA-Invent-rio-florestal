# Estado Atual do Manejo no Código

## Objetivo

Registrar, de forma técnica e auditável, o estado atual da camada de manejo florestal no projeto `inventario-florestal-core`.

Este documento diferencia:

- o que já está implementado;
- o que está apenas estruturado;
- o que ainda precisa ser implementado para configurar um simulador completo de regimes silviculturais.

---

# Situação Atual

Atualmente, o projeto já possui uma estrutura inicial para representar e comparar regimes de manejo, mas ainda não possui um simulador completo de desbastes operacionais acoplado à prognose biométrica.

A camada implementada está concentrada em:

```text
src/inventario_florestal/economico/management_optimizer.py
```

---

# O que já está implementado

## 1. Representação de Regime de Manejo

Classe:

```python
RegimeManejo
```

Campos:

| Campo | Função |
|---|---|
| nome | identificação do regime |
| idade_corte | idade final de corte |
| numero_desbastes | número previsto de desbastes |
| intensidade_desbaste | intensidade geral declarada |
| cenario_operacional | cenário de sortimento/preço |

Esta estrutura representa a configuração geral de um regime, mas ainda não executa automaticamente os desbastes dentro da prognose.

---

## 2. Resultado de Otimização

Classe:

```python
ResultadoOtimizacao
```

Campos:

| Campo | Função |
|---|---|
| regime | regime avaliado |
| score | pontuação econômica penalizada por risco |
| vpl | valor presente líquido |
| relacao_bc | relação benefício/custo |
| risco_negativo | probabilidade de VPL negativo |

---

## 3. Score Econômico Penalizado por Risco

Função:

```python
calcular_score_regime()
```

Estrutura lógica:

```text
score = VPL × B/C × (1 - risco)
```

Onde:

```text
risco = probabilidade de VPL negativo / 100
```

Objetivo:

- evitar selecionar regimes apenas pelo maior VPL;
- penalizar regimes economicamente instáveis;
- integrar retorno e risco.

---

## 4. Seleção do Melhor Regime

Função:

```python
selecionar_melhor_regime()
```

Fluxo:

```text
lista de candidatos
↓
calcula score de cada regime
↓
compara scores
↓
retorna melhor regime
```

Cada candidato deve ser composto por:

```text
RegimeManejo + ResultadoFinanceiro + ResultadoMonteCarlo
```

---

# O que ainda NÃO está implementado

## 1. Simulação explícita de desbastes

Ainda falta implementar:

- idade de cada desbaste;
- intensidade por evento;
- remoção por classe diamétrica;
- tipo de desbaste;
- impacto do desbaste sobre N, G, Dg, Hd;
- receita intermediária dos desbastes;
- redistribuição diamétrica após desbaste.

---

## 2. Regime temporal completo

Ainda não existe uma estrutura completa como:

```text
plantio → inventário atual → desbaste 1 → desbaste 2 → corte final
```

O que existe hoje é uma representação simplificada do regime, usada para comparação econômica.

---

## 3. Integração desbaste + Weibull

Ainda falta:

- selecionar árvores removidas por classe;
- recalcular distribuição remanescente;
- projetar novamente a distribuição pós-desbaste;
- diferenciar produção removida e produção remanescente.

---

## 4. Otimização silvicultural real

Ainda não existe otimização automática de:

- idade ótima de desbaste;
- número ótimo de desbastes;
- intensidade ótima;
- idade ótima de rotação;
- melhor combinação entre produção e risco.

---

# Estado Conceitual do Manejo

O manejo está hoje em nível de:

```text
representação + comparação econômica
```

Ainda não está em nível de:

```text
simulação silvicultural dinâmica completa
```

---

# Arquitetura Recomendada para Próximas Etapas

## 1. Criar Evento de Manejo

Estrutura sugerida:

```python
EventoManejo
```

Campos:

| Campo | Função |
|---|---|
| idade | idade da intervenção |
| tipo | desbaste ou corte final |
| intensidade | percentual removido |
| criterio_remocao | sistemático, por baixo, por cima, seletivo |
| cenario_operacional | cenário aplicado |

---

## 2. Criar Regime Temporal

Estrutura sugerida:

```python
RegimeManejoTemporal
```

Composto por uma lista ordenada de eventos.

---

## 3. Criar Simulador de Regime

Função futura:

```python
simular_regime_manejo()
```

Fluxo desejado:

```text
estado inicial
↓
prognose até evento 1
↓
aplica desbaste
↓
calcula receita do desbaste
↓
recalcula remanescente
↓
prognose até próximo evento
↓
corte final
↓
fluxo de caixa completo
```

---

# Conclusão Técnica

O código já possui uma base correta para comparar regimes de manejo economicamente, mas ainda falta implementar a camada silvicultural dinâmica.

Portanto, neste estágio, o manejo no sistema deve ser interpretado como:

```text
módulo de otimização econômica de regimes candidatos
```

E não ainda como:

```text
simulador completo de desbaste e crescimento pós-intervenção
```

A próxima etapa tecnicamente correta é implementar `EventoManejo` e `RegimeManejoTemporal` antes de avançar para otimização multiobjetivo.
