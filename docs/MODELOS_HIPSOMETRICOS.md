# Modelos Hipsométricos

# Objetivo

Este documento reúne os modelos hipsométricos previstos para o sistema.

Todos os modelos devem:

- ser ajustados automaticamente;
- participar do ranking;
- possuir análise residual;
- possuir rastreabilidade estatística.

---

# Espécies Prioritárias

- Pinus taeda
- Pinus elliottii
- Eucalyptus dunnii
- Eucalyptus benthamii
- Eucalyptus viminalis

---

# Critérios Estatísticos

## Obrigatórios

- R² ajustado;
- Syx;
- Syx%;
- RMSE;
- resíduos;
- PRESS;
- erro médio;
- estabilidade.

---

# Modelos Previstos

## Stoffels

ln(h) = b0 + b1 × ln(DAP)

---

## Curtis

ln(h) = b0 + b1 × (1 / DAP)

---

## Trorey

h = b0 + b1 × DAP + b2 × DAP²

---

## Henriksen

h = b0 + b1 × ln(DAP)

---

## Näslund

h = DAP² / (b0 + b1 × DAP)²

---

## Petterson

h = (DAP / (b0 + b1 × DAP))³

---

## Assmann

h = b0 + b1 × ln(DAP)

---

## Prodan

h = DAP² / (b0 + b1 × DAP + b2 × DAP²)

---

# Diretrizes Técnicas

- avaliar heterocedasticidade;
- avaliar comportamento residual;
- evitar extrapolação fora da faixa de ajuste;
- registrar espécie e região de validação.

---

# Correção de Viés

Obrigatória para modelos logarítmicos.

Métodos previstos:

- Meyer;
- Baskerville;
- Snowdon.

---

# Objetivo do Sistema

O sistema deve selecionar automaticamente o melhor modelo hipsométrico para:

- espécie;
- região;
- idade;
- condição silvicultural.
