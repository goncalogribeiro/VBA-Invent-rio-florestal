# Weibull e Prognose Diamétrica

## Objetivo

Documentar a arquitetura de distribuição diamétrica e prognose estrutural do sistema biométrico florestal.

Esta camada é responsável por:

- modelar a estrutura diamétrica;
- gerar distribuições futuras;
- suportar prognose florestal;
- alimentar módulos de taper e sortimento;
- estimar produção futura por classe.

---

# Fundamentos Biométricos

A distribuição Weibull é amplamente utilizada em modelagem florestal por sua flexibilidade matemática e capacidade de representar diferentes estruturas diamétricas.

Aplicações:

- prognose diamétrica;
- simulação de desbastes;
- produção por classe;
- sortimento futuro;
- avaliação econômica.

---

# Weibull 3P

A implementação utiliza Weibull de 3 parâmetros:

```text
f(x) = (c/b) * ((x-a)/b)^(c-1) * exp(-((x-a)/b)^c)
```

Parâmetros:

| Parâmetro | Interpretação |
|---|---|
| a | deslocamento |
| b | escala |
| c | forma |

---

# Implementações Atuais

## 1. Weibull MLE

Arquivo:

```text
weibull/weibull_mle.py
```

Método:

- máxima verossimilhança;
- otimização via L-BFGS-B;
- bounds controlados.

Aplicação principal:

- ajuste com dados individuais de DAP.

---

## 2. Weibull PRM

Arquivo:

```text
weibull/weibull_prm.py
```

Método:

- Parameter Recovery Method;
- recuperação dos parâmetros a partir de atributos do povoamento.

Entradas principais:

| Variável | Descrição |
|---|---|
| DAP médio | média diamétrica |
| variância | variância diamétrica |
| Dmin | diâmetro mínimo |

Aplicação principal:

- prognose florestal.

---

# Distribuição Diamétrica

Arquivo:

```text
weibull/weibull_distribution.py
```

Fluxo:

```text
Parâmetros Weibull → CDF → Probabilidade por Classe → Árvores/ha
```

---

# Classes Diamétricas

A distribuição é construída por:

```text
CDF(limite superior) - CDF(limite inferior)
```

Isso evita:

- aproximações por centro de classe;
- distorções de frequência;
- problemas de integração.

---

# Estrutura da Distribuição

Cada classe armazena:

| Campo | Função |
|---|---|
| limite inferior | delimitação |
| limite superior | delimitação |
| centro de classe | gráficos |
| probabilidade | matemática |
| árvores/ha | prognose |

---

# Fluxo Completo de Prognose

## Estrutura Atual

```text
Idade → Atributos do Povoamento → Weibull → Classes Diamétricas
```

## Estrutura Final Planejada

```text
Idade atual
↓
Prognose estrutural
↓
Weibull futura
↓
Distribuição diamétrica
↓
Taper
↓
Sortimento
↓
Receita
↓
Indicadores econômicos
```

---

# Relação com Taper

A distribuição Weibull NÃO estima produtos diretamente.

Ela fornece:

- número de árvores por classe;
- distribuição estrutural do povoamento.

O cálculo de produtos depende posteriormente de:

- taper;
- altura;
- qualidade;
- regras de sortimento.

---

# Relação com Prognose

O sistema seguirá o modelo clássico:

| Etapa | Variáveis |
|---|---|
| sobrevivência | N |
| crescimento | G, Dg, Hd |
| distribuição | Weibull |
| produtos | taper + sortimento |

---

# Bases Científicas

Principais referências:

- Clutter (1970)
- Bailey & Clutter
- Pienaar & Shiver
- Ferraz Filho (2009)
- Viana (2016)
- Wendling et al. (2011)
- Schmidt (2014)
- Arce (2004)

---

# Estado Atual

| Componente | Status |
|---|---|
| Weibull MLE | operacional |
| Weibull PRM | operacional |
| distribuição diamétrica | operacional |
| classes automáticas | operacional |
| árvores por classe | operacional |

---

# Próximos Passos

## Prioridade Alta

- prognose estrutural;
- modelos de sobrevivência;
- prognose de área basal;
- prognose de Dg;
- integração Weibull-prognose.

## Prioridade Média

- taper avançado;
- sortimento prognóstico;
- otimização econômica.

## Prioridade Futura

- simulador multi-rotação;
- Monte Carlo;
- risco climático.
