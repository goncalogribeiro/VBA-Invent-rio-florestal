# Estabilização Matemática da Prognose

## Objetivo

Definir mecanismos de segurança matemática e biológica para a prognose florestal.

## Problema

A plataforma possui múltiplos feedbacks entre crescimento, mortalidade, competição, ecofisiologia e aprendizado adaptativo.

Sem controle matemático, podem ocorrer:

- crescimento explosivo;
- mortalidade impossível;
- área basal incoerente;
- carbono negativo;
- drift adaptativo;
- colapso populacional artificial.

## Diretriz

Toda saída dinâmica deverá passar por validação de limites plausíveis.

## Limites Iniciais

| Variável | Limite inicial |
|---|---|
| crescimento anual DAP | 0 a 5 cm/ano |
| mortalidade anual | 0 a 100% |
| LAI | 0 a 12 |
| GPP | >= 0 |
| NPP | >= 0 |
| área basal | >= 0 |
| volume | >= 0 |

## Camadas de Controle

### Controle de Crescimento

Validar:

- crescimento anual;
- crescimento acumulado;
- resposta à competição;
- resposta à luz.

### Controle de Mortalidade

Validar:

- probabilidade entre 0 e 1;
- mortalidade populacional plausível;
- ausência de N negativo.

### Controle Ecofisiológico

Validar:

- LAI plausível;
- GPP/NPP não negativos;
- carbono não negativo.

### Controle Adaptativo

Validar:

- ajuste máximo por ciclo;
- ausência de drift;
- estabilidade temporal.

## Conclusão

A estabilização matemática é etapa obrigatória antes da validação com datasets reais.
