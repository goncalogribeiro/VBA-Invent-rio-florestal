# Scenario Engine Operacional

## Objetivo

Documentar a arquitetura da camada de cenários operacionais do simulador florestal.

Esta camada centraliza:

- sortimentos;
- comprimentos de tora;
- diâmetros mínimos;
- preços por tonelada;
- conversão m3 → ton.

---

# Filosofia Arquitetural

O sistema NÃO deve:

- possuir preços hardcoded;
- possuir comprimentos fixos no código;
- possuir regras operacionais espalhadas.

O sistema DEVE:

- centralizar parâmetros no YAML;
- carregar cenários dinamicamente;
- permitir múltiplos regimes industriais.

---

# Fonte Oficial

Arquivo:

```text
data/modelos/modelos_biometricos.yaml
```

---

# Estrutura dos Cenários

Cada cenário contém:

| Campo | Uso |
|---|---|
| nome | identificação comercial |
| diametro_ponta_fina_min_cm | classificação |
| comprimento_m | produção |
| valor_ton | receita |

---

# Cenários Implementados

| Cenário | Estratégia |
|---|---|
| pessimista | maior participação de produtos inferiores |
| realista | mercado operacional médio |
| otimista | maior agregação de valor |

---

# Conversão m3 → ton

A conversão foi centralizada em:

```text
parametros_operacionais.conversao_m3_ton
```

---

# Motivação Biométrica

A conversão:

- varia com idade;
- varia com densidade;
- varia com espécie;
- impacta diretamente a receita.

Portanto NÃO deve ser:

- constante fixa;
- parâmetro manual solto.

---

# Integração Completa

Fluxo operacional:

```text
Cenário
↓
Sortimentos
↓
Taper
↓
Volume
↓
Conversão ton
↓
Receita
↓
Indicadores econômicos
```

---

# Próximos Passos

## Prioridade Alta

- Scenario Engine;
- carregador YAML;
- integração taper → cenário;
- integração receita → cenário.
