# Prognose Estrutural de Povoamentos

## Objetivo

Documentar a arquitetura da prognose estrutural implementada no núcleo biométrico florestal.

A prognose estrutural é responsável por projetar os atributos fundamentais do povoamento entre duas idades.

---

# Variáveis Estruturais

O sistema trabalha inicialmente com:

| Variável | Significado |
|---|---|
| N | árvores por hectare |
| G | área basal |
| Dg | diâmetro quadrático |
| Hd | altura dominante |
| S | índice de sítio |

---

# Fluxo Estrutural

```text
Estado Atual
↓
Modelo de Sobrevivência
↓
Modelo de Área Basal
↓
Recalculo de Dg
↓
Prognose de Hd
↓
Estado Futuro
```

---

# Arquitetura Atual

Arquivo principal:

```text
prognose/stand_projection.py
```

---

# Estado do Povoamento

Classe:

```python
EstadoPovoamento
```

Campos:

| Campo | Descrição |
|---|---|
| idade | idade atual |
| n_arvores_ha | densidade |
| area_basal | área basal |
| dap_medio | Dg |
| altura_dominante | Hd |
| indice_sitio | produtividade |

---

# Modelo Inicial Implementado

## Clutter (1970)

A implementação atual utiliza uma estrutura inspirada nos modelos clássicos de Clutter.

---

# Sobrevivência

Estrutura:

```text
N2 = N1 * (I2/I1)^β1 * exp[(β0 + β2*S)*(I2-I1)]
```

Objetivo:

- projetar mortalidade natural;
- atualizar densidade do povoamento.

---

# Área Basal

Estrutura:

```text
ln(G2) = β0 + ln(G1)*(I1/I2)
         + β1*(1-I1/I2)
         + β2*(1-I1/I2)*S
```

Objetivo:

- projetar crescimento estrutural.

---

# Recalculo de Dg

O Dg é recalculado por:

```text
Dg = sqrt((40000 * G)/(π * N))
```

Isso garante consistência biométrica entre:

- densidade;
- área basal;
- diâmetro médio.

---

# Altura Dominante

A implementação atual utiliza:

```text
Hd2 = Hd1 * ((I2/I1)^0.25)
```

OBSERVAÇÃO:

Esta é uma implementação provisória.

Posteriormente será substituída por:

- Chapman-Richards;
- Silva-Bailey;
- curvas anamórficas;
- curvas polimórficas.

---

# Integração Planejada

A prognose estrutural alimentará diretamente:

```text
Estado Futuro
↓
PRM Weibull
↓
Distribuição Diamétrica
↓
Taper
↓
Sortimento
↓
Receita
```

---

# Filosofia Científica

O sistema NÃO deve:

- projetar apenas volume;
- ignorar estrutura diamétrica;
- projetar DAP diretamente sem consistência biométrica.

O sistema DEVE:

- manter coerência entre N, G e Dg;
- utilizar prognose baseada em povoamento;
- alimentar distribuição diamétrica;
- manter rastreabilidade matemática.

---

# Estado Atual

| Componente | Status |
|---|---|
| Estado estrutural | operacional |
| Prognose Clutter básica | operacional |
| Sobrevivência | operacional |
| Prognose de G | operacional |
| Recalculo de Dg | operacional |

---

# Próximos Passos

## Prioridade Alta

- integração prognose + Weibull;
- prognose diamétrica completa;
- modelos reais de sítio;
- prognose de Hd robusta.

## Prioridade Média

- taper avançado;
- sortimento prognóstico.
