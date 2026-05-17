# Estabilização Temporal e Amortecimento Ecológico

## Objetivo

Definir mecanismos de suavização temporal para a prognose florestal.

## Problema

Modelos dinâmicos com crescimento, mortalidade, competição, ecofisiologia e aprendizado podem apresentar oscilações artificiais.

## Conceito

A floresta possui inércia ecológica. Variáveis estruturais e fisiológicas não devem mudar abruptamente sem justificativa biológica.

## Mecanismos

### Suavização Temporal

Reduz oscilações entre ciclos consecutivos.

### Amortecimento

Limita variações bruscas em crescimento, mortalidade, carbono e LAI.

### Controle de Drift

Limita ajustes adaptativos excessivos em cada ciclo.

### Inércia Ecológica

Representa resposta gradual do povoamento a manejo, competição e clima.

## Variáveis Controladas

- crescimento;
- mortalidade;
- LAI;
- GPP;
- NPP;
- carbono;
- ajuste adaptativo.

## Diretriz Técnica

Toda recalibração deverá ser gradual e limitada por ciclo.

## Conclusão

A estabilização temporal é obrigatória antes de executar stress tests sintéticos e validação com dados reais.
