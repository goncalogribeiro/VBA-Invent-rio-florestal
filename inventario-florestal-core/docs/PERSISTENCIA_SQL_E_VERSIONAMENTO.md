# Persistência SQL e Versionamento de Prognoses

## Objetivo

Documentar a arquitetura de persistência SQL, versionamento e auditoria da prognose florestal.

---

# Conceito

A prognose florestal corporativa exige:

- persistência confiável;
- rastreabilidade;
- auditoria;
- histórico de decisões.

---

# Estrutura Geral

```text
inventários
↓
persistência SQL
↓
versionamento
↓
auditoria
↓
analytics
```

---

# Papel do Banco SQL

O banco deverá armazenar:

| Entidade | Uso |
|---|---|
| parcelas | histórico |
| árvores | histórico |
| medições | temporal |
| prognoses | versionamento |
| manejo | auditoria |
| economia | analytics |

---

# Versionamento

Cada prognose deverá possuir:

- identificador único;
- data de execução;
- parâmetros utilizados;
- modelos utilizados;
- cenário utilizado.

---

# Auditoria

O sistema deverá registrar:

| Evento | Registro |
|---|---|
| recalibração | histórico |
| manejo | histórico |
| prognose | histórico |
| alteração de parâmetros | histórico |

---

# Integração com FSC

A rastreabilidade histórica será importante para:

- auditoria FSC;
- governança;
- compliance;
- validação técnica.

---

# Integração com Analytics

O banco temporal permitirá:

- dashboards;
- indicadores;
- séries históricas;
- benchmarking.

---

# Evolução Futura

Futuramente o sistema poderá incorporar:

| Camada | Futuro |
|---|---|
| data warehouse | ✓ |
| BI corporativo | ✓ |
| IA preditiva | ✓ |
| APIs | ✓ |
| cloud | ✓ |

---

# Conclusão

A persistência SQL e o versionamento representam a infraestrutura responsável por transformar o sistema em uma plataforma corporativa auditável e rastreável.
