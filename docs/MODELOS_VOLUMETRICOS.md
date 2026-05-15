# Modelos Volumétricos

# Objetivo

Este documento reúne os modelos volumétricos previstos para o sistema.

Todos os modelos devem:

- participar do torneio estatístico;
- possuir diagnóstico residual;
- possuir correção de viés quando aplicável;
- possuir rastreabilidade matemática.

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
- AIC;
- BIC;
- PRESS;
- estabilidade.

---

# Modelos Previstos

## Schumacher-Hall

ln(v) = b0 + b1 × ln(DAP) + b2 × ln(h)

---

## Spurr

v = b0 + b1 × (DAP² × h)

---

## Stoate

v = b0 + b1 × DAP² + b2 × DAP² × h + b3 × h

---

## Meyer

ln(v) = b0 + b1 × ln(DAP) + b2 × ln(h)

---

## Näslund

v = DAP² / (b0 + b1 × DAP)²

---

## Honer

v = DAP² / (b0 + b1 / h)

---

## Brenac

ln(v) = b0 + b1 × ln(DAP) + b2 × (1 / DAP)

---

## Takata

v = DAP² × h / (b0 + b1 × DAP)

---

## Clutter

ln(v) = b0 + b1 × ln(DAP² × h)

---

## Prodan

v = DAP² / (b0 + b1 × DAP + b2 × DAP²)

---

# Correção de Viés

Obrigatória para modelos logarítmicos.

Métodos previstos:

- Meyer;
- Baskerville;
- Snowdon.

---

# Diretrizes Técnicas

- evitar extrapolação;
- registrar faixa diamétrica;
- registrar idade;
- registrar região de ajuste;
- registrar tipo de manejo.

---

# Objetivo do Sistema

Selecionar automaticamente o melhor modelo volumétrico conforme:

- espécie;
- idade;
- material genético;
- região;
- condição silvicultural.
