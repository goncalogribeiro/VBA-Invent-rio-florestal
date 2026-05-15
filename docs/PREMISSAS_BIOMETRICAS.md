# Premissas Biométricas

# Objetivo

Este documento define as premissas biométricas oficiais do projeto de inventário florestal.

As premissas devem ser baseadas prioritariamente em:

- artigos científicos;
- literatura biométrica florestal;
- publicações técnicas;
- EMBRAPA;
- IPEF;
- UFPR;
- UDESC;
- UFSM;
- revistas científicas florestais;
- dissertações e teses.

O foco principal do projeto é:

- Pinus taeda;
- Pinus elliottii;
- Eucalyptus dunnii;
- Eucalyptus benthamii;
- Eucalyptus viminalis.

Região prioritária:

- Sul do Brasil.

---

# Diretriz Científica Fundamental

Nenhuma equação deve ser fixa.

Todos os modelos biométricos devem passar por:

1. ajuste estatístico;
2. diagnóstico;
3. análise de resíduos;
4. correção de viés quando aplicável;
5. ranking;
6. seleção automática.

---

# Conversão CAP → DAP

Sempre que houver CAP (Circunferência à Altura do Peito), deve-se converter para DAP.

Equação:

DAP = CAP / π

Onde:

- CAP em cm;
- DAP em cm.

---

# Área Basal Individual

Equação oficial:

gi = (π × DAP²) / 40000

Onde:

- gi em m²;
- DAP em cm.

---

# Volume

O sistema deve permitir:

- fator de forma;
- cubagem rigorosa;
- regressões volumétricas;
- taper;
- volume comercial;
- volume total.

---

# Cubagem Rigorosa

Métodos obrigatórios:

- Smalian;
- Huber;
- Newton.

Objetivos:

- geração de volume rigoroso;
- geração de fatores de forma;
- geração de regressões volumétricas;
- geração de taper.

---

# Correção de Viés

Obrigatória para modelos logarítmicos.

Métodos previstos:

- Meyer;
- Baskerville;
- Snowdon.

---

# Ranking de Modelos

Todo modelo biométrico deve passar por torneio estatístico.

Critérios mínimos:

- R² ajustado;
- Syx;
- Syx%;
- RMSE;
- AIC;
- BIC;
- resíduos;
- erro médio;
- PRESS;
- estabilidade.

---

# Hipsometria

O sistema deve permitir ajuste simultâneo de múltiplas equações hipsométricas.

Objetivo:

seleção automática do melhor modelo regional.

---

# Volumetria

O sistema deve permitir ajuste simultâneo de múltiplas equações volumétricas.

Modelos previstos:

- Schumacher-Hall;
- Spurr;
- Stoate;
- Meyer;
- Näslund;
- Honer;
- Brenac;
- Takata;
- Clutter;
- Prodan.

---

# Taper

O sistema deve permitir torneio de funções taper.

Modelos previstos:

- Kozak;
- Demaerschalk;
- Ormerod;
- Garay;
- Max-Burkhart.

---

# Índice de Sítio

Métodos previstos:

- curva-guia;
- anamórfico;
- polimórfico.

---

# Distribuição Diamétrica

Funções previstas:

- Normal;
- Lognormal;
- Weibull;
- Gamma.

---

# Sortimento

O sistema deve permitir:

- classificação dinâmica de toras;
- múltiplos cenários;
- integração taper + volume;
- integração econômica.

---

# Prognose

A prognose deve considerar:

- crescimento;
- mortalidade;
- sobrevivência;
- incremento;
- distribuição diamétrica;
- desbaste;
- produção.

---

# Diretriz de Qualidade

Todo modelo implementado deve possuir:

- referência bibliográfica;
- unidade definida;
- rastreabilidade matemática;
- interpretação estatística;
- validação regional quando possível.
