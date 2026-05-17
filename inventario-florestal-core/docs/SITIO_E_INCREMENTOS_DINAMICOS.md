# Sítio e Incrementos Dinâmicos

## Objetivo

Documentar a integração entre índice de sítio, ICA e IMA dentro da prognose dinâmica.

---

# Conceito

A produtividade florestal depende diretamente da qualidade do sítio.

O sítio controla:

- crescimento;
- altura dominante;
- culminação;
- idade técnica de corte;
- resposta ao manejo.

---

# Papel do Índice de Sítio

O índice de sítio representa o potencial produtivo do local.

Normalmente baseado em:

| Variável | Uso |
|---|---|
| altura dominante | principal |
| idade | referência |

---

# Integração Correta

```text
sítio
↓
capacidade produtiva
↓
ICA
↓
IMA
↓
culminação
↓
manejo
```

---

# ICA

## Conceito

Incremento Corrente Anual.

Representa o crescimento ocorrido no último período.

---

# Fórmula

```text
ICA = Y(t) - Y(t-1)
```

---

# IMA

## Conceito

Incremento Médio Anual.

Representa o crescimento médio acumulado.

---

# Fórmula

```text
IMA = Y(t) / t
```

---

# Culminação

A culminação do IMA representa:

- idade técnica de máxima eficiência volumétrica;
- referência clássica de rotação.

---

# Integração com Manejo

O sistema deverá usar:

| Variável | Uso |
|---|---|
| ICA | crescimento atual |
| IMA | produtividade média |
| sítio | potencial produtivo |
| competição | ajuste estrutural |

---

# Integração com Prognose

O crescimento deverá responder:

- ao sítio;
- à idade;
- à competição;
- ao manejo.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| anamórfico | ✓ |
| polimórfico | ✓ |
| ADA | ✓ |
| GADA | ✓ |
| sítio dinâmico | ✓ |

---

# Conclusão

A integração entre sítio, ICA e IMA representa o mecanismo responsável por transformar a prognose estrutural em prognose produtiva.
