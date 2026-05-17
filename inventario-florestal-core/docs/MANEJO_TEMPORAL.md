# Arquitetura Temporal de Manejo

## Objetivo

Documentar a primeira camada temporal do simulador silvicultural.

Esta implementação cria a estrutura formal para representar:

- desbastes;
- corte final;
- sequência cronológica de intervenções.

---

# Motivação

Até esta etapa, o projeto conseguia:

- comparar regimes economicamente;
- ranquear cenários;
- calcular risco;
- selecionar melhor regime.

Porém, ainda não existia:

```text
sequência temporal explícita de manejo
```

A camada implementada resolve esse problema.

---

# Estruturas Implementadas

## 1. EventoManejo

Arquivo:

```text
src/inventario_florestal/manejo/events.py
```

Representa uma intervenção silvicultural individual.

Campos:

| Campo | Função |
|---|---|
| idade | idade da intervenção |
| tipo | tipo de manejo |
| intensidade | intensidade removida |
| criterio_remocao | regra de remoção |
| cenario_operacional | cenário econômico associado |
| observacoes | metadados técnicos |

---

# Tipos de Evento

| Tipo | Uso |
|---|---|
| desbaste_sistematico | remoção por padrão geométrico |
| desbaste_por_baixo | remoção de árvores inferiores |
| desbaste_pelo_alto | remoção de competidoras superiores |
| desbaste_misto | combinação operacional |
| desbaste_sanitario | remoção fitossanitária |
| corte_final | encerramento da rotação |

---

# Critérios de Remoção

| Critério | Interpretação |
|---|---|
| arvores | percentual de árvores |
| area_basal | percentual de G removido |
| volume | percentual volumétrico |
| classe_diametrica | remoção por distribuição |

---

# Regras de Validação

## Regras implementadas

| Regra | Status |
|---|---|
| idade positiva | ✓ |
| intensidade entre 0 e 1 | ✓ |
| corte final = intensidade 1.0 | ✓ |
| eventos em ordem cronológica | ✓ |
| apenas um corte final | ✓ |
| corte final deve ser último evento | ✓ |

---

# 2. RegimeManejoTemporal

Representa uma sequência cronológica de eventos.

Exemplo conceitual:

```text
Plantio
↓
Desbaste aos 8 anos
↓
Desbaste aos 12 anos
↓
Corte final aos 18 anos
```

---

# Exemplo de Estrutura

```python
regime = RegimeManejoTemporal(
    nome="Regime Realista",
    eventos=[
        EventoManejo(...),
        EventoManejo(...),
        EventoManejo(...),
    ]
)
```

---

# O que esta camada AINDA NÃO faz

Ainda não existe:

- remoção explícita de árvores;
- redistribuição Weibull;
- recalibração de N/G/Dg;
- crescimento pós-desbaste;
- geração de povoamento remanescente.

---

# Próxima Etapa

A próxima camada deverá implementar:

```text
Aplicador de Desbaste
```

Responsabilidades futuras:

- remover árvores;
- recalcular estrutura;
- recalcular distribuição diamétrica;
- recalcular taper;
- separar removido e remanescente.

---

# Importância Arquitetural

Esta etapa é crítica porque:

- separa eventos de manejo da biometria;
- separa cronologia da prognose;
- evita acoplamento excessivo;
- prepara o simulador dinâmico.

---

# Estado Atual

O projeto agora possui:

| Camada | Status |
|---|---|
| biometria | ✓ |
| taper | ✓ |
| Weibull | ✓ |
| economia | ✓ |
| risco | ✓ |
| otimização | ✓ |
| eventos temporais | ✓ |
| simulador de desbaste real | pendente |

---

# Conclusão

A implementação atual representa o início formal do simulador silvicultural dinâmico.

A partir desta camada, o sistema passa a possuir uma cronologia explícita de manejo, requisito essencial para simulação de regimes florestais reais.
