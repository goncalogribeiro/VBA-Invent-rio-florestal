# Prognose Diamétrica Completa

## Objetivo

Documentar a integração entre:

- prognose estrutural;
- Weibull PRM;
- distribuição diamétrica futura.

Esta camada representa o núcleo de construção estrutural de povoamentos futuros.

---

# Pipeline Atual

```text
Estado Atual
↓
Prognose Estrutural
↓
Estado Futuro
↓
PRM Weibull
↓
Parâmetros Weibull
↓
Distribuição Diamétrica
↓
Árvores por Classe
```

---

# Componentes Integrados

## Prognose Estrutural

Arquivo:

```text
prognose/stand_projection.py
```

Responsável por:

| Variável | Função |
|---|---|
| N | sobrevivência |
| G | crescimento |
| Dg | estrutura diamétrica |
| Hd | produtividade |

---

## Weibull PRM

Arquivo:

```text
weibull/weibull_prm.py
```

Responsável por:

- recuperar parâmetros Weibull;
- representar estrutura diamétrica futura.

Entradas:

| Entrada | Origem |
|---|---|
| Dg | prognose estrutural |
| variância | estrutura diamétrica |
| Dmin | limite operacional |

---

## Distribuição Diamétrica

Arquivo:

```text
weibull/weibull_distribution.py
```

Responsável por:

- gerar classes;
- calcular probabilidades;
- calcular árvores/ha.

---

## Integração Completa

Arquivo:

```text
prognose/diametric_projection.py
```

Função principal:

```python
prognose_diametrica_prm()
```

---

# Filosofia Biométrica

O sistema NÃO deve:

- projetar apenas volume;
- projetar árvores médias fictícias;
- ignorar distribuição diamétrica.

O sistema DEVE:

- manter estrutura do povoamento;
- preservar coerência biométrica;
- gerar classes futuras reais;
- permitir prognose de produtos.

---

# Relação com Taper

A prognose diamétrica NÃO estima diretamente:

- volume comercial;
- produtos;
- sortimentos.

Ela fornece:

- árvores por classe;
- estrutura futura;
- base para taper.

---

# Próxima Camada

## Taper Prognóstico

Fluxo planejado:

```text
Classe Diamétrica
↓
DAP representativo
↓
Taper
↓
Toras
↓
Sortimentos
↓
Volume/Massa
↓
Receita
```

---

# Estado Atual

| Componente | Status |
|---|---|
| prognose estrutural | operacional |
| Weibull PRM | operacional |
| distribuição diamétrica | operacional |
| integração prognóstica | operacional |

---

# Próximos Passos

## Prioridade Alta

- taper prognóstico;
- sortimento prognóstico;
- volume por classe;
- receita futura.

## Prioridade Média

- otimização de manejo;
- simulador multi-rotação;
- análise econômica.
