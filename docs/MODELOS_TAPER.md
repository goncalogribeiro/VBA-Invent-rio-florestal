# Modelos de Taper / Afilamento

## Objetivo

Este documento define a base técnica inicial para implementação de funções de taper no sistema de inventário, sortimento e prognose florestal.

As funções de taper têm como objetivo estimar o diâmetro do fuste em diferentes alturas, permitindo:

- estimativa de volume comercial;
- cálculo de volume por seção;
- simulação de multiprodutos;
- geração de sortimento por classe;
- integração com cenários econômicos;
- comparação entre regimes silviculturais.

---

# Diretriz Técnica Central

Nenhum modelo de taper deve ser adotado como fixo.

Todos os modelos devem participar de torneio estatístico, com:

1. ajuste;
2. validação;
3. análise residual por posição relativa no fuste;
4. análise de viés por segmento;
5. ranking;
6. seleção automática do melhor modelo aprovado.

---

# Variáveis Fundamentais

| Símbolo | Descrição | Unidade |
|---|---|---|
| d | diâmetro na altura h | cm |
| DAP | diâmetro à altura do peito | cm |
| h | altura da seção no fuste | m |
| H | altura total da árvore | m |
| h/H | altura relativa | adimensional |

---

# Modelos Iniciais

## T01 — Hadetzky

Forma geral:

```text
d/DAP = β0 + β1(h/H)^p1 + β2(h/H)^p2 + ... + βn(h/H)^pn
```

Observações:

- modelo flexível;
- adequado para competição com polinômios fracionários;
- exige validação dos expoentes;
- pode demandar ajuste não linear.

---

## T02 — Bi

Forma geral:

```text
d = DAP × [ln(sin(πh/2H)) / ln(sin(π×1,3/2H))]^f(...)
```

Observações:

- modelo de forma variável;
- maior complexidade computacional;
- recomendado para avaliação em espécies de Eucalyptus;
- exige controle rigoroso de domínio matemático.

---

## T03 — Schöepfer

Forma geral:

```text
d/DAP = β0 + β1T + β2T² + β3T³ + β4T⁴ + β5T⁵
```

Onde:

```text
T = h/H
```

Observações:

- modelo polinomial tradicional;
- simples de implementar;
- pode apresentar instabilidade nas extremidades do fuste.

---

## T04 — Kozak et al. (1969)

Forma geral:

```text
(d/DAP)² = β0 + β1T + β2T²
```

Observações:

- modelo simples;
- linearizável;
- útil como modelo de comparação base.

---

## T05 — Demaerschalk

Forma geral:

```text
(d/DAP)² = 10^(2β0) × DAP^(2β1-2) × (H-h)^(2β2) × H^(2β3)
```

Observações:

- modelo compatível com volume;
- exige cuidado com base logarítmica;
- pode ser linearizado em algumas formulações.

---

## T06 — Prodan / Polinomial de 5º grau

Forma geral:

```text
d/DAP = β0 + β1T + β2T² + β3T³ + β4T⁴ + β5T⁵
```

Observação:

matematicamente semelhante ao modelo de Schöepfer quando usada a mesma estrutura polinomial.

---

## T07 — Ormerod

Forma geral:

```text
d/DAP = ((H-h)/(h-1,3))^β1
```

Observações críticas:

- exige validação do domínio;
- há singularidade quando h se aproxima de 1,3 m;
- não deve ser usado sem tratamento numérico.

---

## T08 — Clark et al. (1991)

Forma geral:

```text
d = f(DAP, H, h)
```

Modelo segmentado com porções distintas do fuste.

Observações:

- maior complexidade;
- adequado para fustes com mudanças claras de forma;
- exige ajuste não linear segmentado.

---

# Critérios de Avaliação

Os modelos de taper devem ser avaliados por:

- erro médio absoluto;
- RMSE por seção;
- viés por altura relativa;
- erro percentual por segmento;
- estabilidade na base;
- estabilidade no topo;
- coerência monotônica do diâmetro;
- capacidade de estimar volume comercial.

---

# Integração com Sortimento

O taper deve alimentar diretamente o motor de sortimento.

Fluxo:

```text
DAP + H + modelo taper → diâmetro por altura → toras → classes → volume → massa → valor
```

---

# Regras de Segurança Matemática

- não permitir diâmetros negativos;
- não permitir aumento incoerente do diâmetro no sentido base-topo, salvo anomalias tratadas;
- validar domínio de logaritmos;
- validar domínio de potências fracionárias;
- controlar extrapolação fora da faixa de cubagem;
- registrar espécie, idade, região e manejo.

---

# Status

Este documento representa o catálogo inicial de modelos taper.

Cada modelo ainda deve receber:

- referência bibliográfica completa;
- faixa de uso;
- espécie validada;
- região de aplicação;
- testes numéricos;
- implementação em VBA/Python;
- validação com cubagem rigorosa.
