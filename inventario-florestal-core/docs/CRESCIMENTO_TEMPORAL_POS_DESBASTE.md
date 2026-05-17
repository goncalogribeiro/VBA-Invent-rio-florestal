# Crescimento Temporal Pós-Desbaste

## Objetivo

Documentar a arquitetura do crescimento temporal após intervenções silviculturais.

---

# Conceito

Após o desbaste, o povoamento não continua crescendo sob as mesmas condições estruturais anteriores.

O sistema deve:

- recalcular competição;
- recalcular estrutura diamétrica;
- recalcular crescimento individual e coletivo.

---

# Fluxo Geral

```text
inventário inicial
↓
torneios biométricos
↓
desbaste
↓
remanescente estrutural
↓
Weibull residual
↓
crescimento temporal
↓
prognose futura
```

---

# Componentes do Crescimento

| Componente | Função |
|---|---|
| sítio | potencial produtivo |
| Weibull residual | estrutura diamétrica |
| mortalidade | redução populacional |
| ICA | crescimento periódico |
| IMA | crescimento médio |
| competição | redistribuição de crescimento |
| manejo | alteração estrutural |

---

# Crescimento Compensatório

Após desbaste:

- árvores remanescentes recebem mais recursos;
- DAP cresce mais rapidamente;
- copa expande;
- crescimento diamétrico aumenta.

O sistema deverá representar este efeito futuramente.

---

# Estrutura Temporal

A prognose será executada em ciclos.

Exemplo:

```text
idade atual
↓
projetar +1 ano
↓
atualizar estrutura
↓
recalcular Weibull
↓
próximo ciclo
```

---

# Observação Importante

O sistema não deverá projetar diretamente até o corte final sem recalibração estrutural intermediária.

A estrutura deverá ser atualizada continuamente.

---

# Integração com Remedições

Quando houver novo inventário:

- recalibrar equações;
- recalibrar Weibull;
- recalcular crescimento observado;
- validar prognose anterior.

---

# Conclusão

O crescimento temporal pós-desbaste representa a transição definitiva do sistema de um inventário estático para um simulador dinâmico de crescimento e produção.
