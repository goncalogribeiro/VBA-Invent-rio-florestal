# Roadmap Técnico

# Fase 1 — Consolidação VBA

Status: em andamento

## Objetivos

- consolidar módulos atuais;
- eliminar duplicações;
- centralizar funções globais;
- padronizar tratamento de erros;
- estabilizar rotinas de inventário;
- exportar módulos VBA para versionamento.

---

# Fase 2 — Motor Universal de Ranking

## Objetivo

Criar um motor genérico de competição de modelos biométricos.

## Aplicações

- hipsometria;
- volumetria;
- taper;
- índice de sítio;
- prognose;
- distribuição diamétrica.

## Critérios Estatísticos

- R²;
- R² ajustado;
- Syx;
- Syx%;
- RMSE;
- AIC;
- BIC;
- PRESS;
- erro médio;
- erro relativo;
- resíduos;
- parcimônia;
- estabilidade.

---

# Fase 3 — Cubagem Rigorosa

## Métodos previstos

- Smalian;
- Huber;
- Newton.

## Objetivos

- cálculo de volume rigoroso;
- geração de base para regressões volumétricas;
- geração de base para taper;
- geração de fatores de forma reais.

---

# Fase 4 — Equações Volumétricas

## Espécies prioritárias

- Pinus taeda;
- Pinus elliottii;
- Eucalyptus dunnii;
- Eucalyptus benthamii;
- Eucalyptus viminalis.

## Modelos previstos

- Schumacher-Hall;
- Spurr;
- Stoate;
- Meyer;
- Näslund;
- Honer;
- Brenac;
- Takata;
- Clutter;
- Prodan;
- Chapman-Richards;
- Weibull.

---

# Fase 5 — Correção de Viés

## Métodos previstos

- Meyer;
- Baskerville;
- Snowdon.

Objetivo:

corrigir modelos transformados logaritmicamente.

---

# Fase 6 — Taper

## Modelos previstos

- Kozak;
- Demaerschalk;
- Ormerod;
- Garay;
- Max-Burkhart.

## Objetivos

- estimativa de diâmetro ao longo do fuste;
- geração dinâmica de sortimento;
- integração com cenários.

---

# Fase 7 — Sortimento

## Objetivos

- classificação industrial;
- simulação econômica;
- integração taper + preços;
- integração volume + massa;
- múltiplos cenários.

## Cenários previstos

- pessimista;
- realista;
- otimista.

---

# Fase 8 — Índice de Sítio

## Métodos previstos

- curva-guia;
- anamórfico;
- polimórfico.

## Objetivos

- classificação produtiva;
- prognose;
- comparação entre materiais genéticos.

---

# Fase 9 — Prognose

## Componentes previstos

- crescimento;
- mortalidade;
- sobrevivência;
- incremento;
- distribuição diamétrica;
- desbaste;
- produção.

---

# Fase 10 — Distribuição Diamétrica

## Funções previstas

- Normal;
- Lognormal;
- Weibull;
- Gamma.

## Objetivos

- prognose estrutural;
- simulação de desbastes;
- estimativa de produtos.

---

# Fase 11 — Python Científico

## Objetivos

- regressões avançadas;
- processamento vetorial;
- integração GIS futura;
- machine learning futuro;
- simulações Monte Carlo;
- inferência bayesiana.

---

# Diretriz Científica Central

O sistema deve operar por meio de torneio de modelos biométricos.

Nenhuma equação deve ser tratada como fixa.

O sistema deve:

1. ajustar múltiplos modelos;
2. comparar estatisticamente;
3. corrigir viés quando necessário;
4. avaliar resíduos;
5. ranquear;
6. selecionar automaticamente o melhor modelo aprovado.
