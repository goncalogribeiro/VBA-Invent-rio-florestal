# Integração entre Taper Prognóstico e Scenario Engine

## Objetivo

Documentar a integração entre:

- taper prognóstico;
- cenários operacionais;
- estrutura industrial de sortimento.

---

# Filosofia Arquitetural

O sistema NÃO deve:

- utilizar listas hardcoded de produtos;
- definir comprimentos diretamente no código;
- possuir múltiplas fontes operacionais.

O sistema DEVE:

- utilizar o YAML como fonte única;
- carregar cenários dinamicamente;
- executar o taper conforme o regime operacional.

---

# Estrutura Atual

Fluxo completo:

```text
YAML
↓
Scenario Engine
↓
Cenário Operacional
↓
Taper Prognóstico
↓
Toras
↓
Volume
↓
Massa
↓
Receita
```

---

# Fonte Operacional Oficial

Arquivo:

```text
data/modelos/modelos_biometricos.yaml
```

---

# Integração Implementada

O taper agora recebe:

```python
cenario: CenarioOperacional
```

E NÃO:

```python
comprimentos: list
```

---

# Vantagens Técnicas

| Benefício | Resultado |
|---|---|
| centralização | elimina redundância |
| parametrização | múltiplos regimes |
| rastreabilidade | auditoria completa |
| desacoplamento | manutenção simplificada |
| flexibilidade | adaptação industrial |

---

# Estratégia de Alocação

Os produtos são testados:

```text
maior ponta fina → menor ponta fina
```

Objetivo:

- maximizar valor agregado;
- priorizar produtos nobres;
- manter lógica industrial.

---

# Critério Comercial

O enquadramento utiliza:

```text
diâmetro da ponta fina
```

E NÃO:

- DAP;
- diâmetro médio.

---

# Estrutura Industrial Atual

| Cenário | Estratégia |
|---|---|
| pessimista | maior energia/celulose |
| realista | equilíbrio operacional |
| otimista | maior laminação |

---

# Conversão Massa

A conversão:

```text
m3 → ton
```

é carregada automaticamente do YAML.

---

# Motivação Biométrica

A densidade operacional:

- varia com idade;
- varia com espécie;
- impacta diretamente a receita.

---

# Próximos Passos

## Econômico

- fluxo de caixa;
- VPL;
- TIR;
- VET;
- análise de sensibilidade.

## Biométrico

- taper segmentado;
- taper Kozak;
- taper Bi;
- taper variável.
