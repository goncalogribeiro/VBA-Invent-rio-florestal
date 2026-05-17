# Simulação Temporal Sintética

## Objetivo

Documentar a simulação temporal sintética usada para stress tests longitudinais.

## Conceito

Os cenários sintéticos estáticos deverão ser evoluídos ao longo do tempo para testar crescimento, mortalidade, competição, manejo e recalibração.

## Estrutura Temporal

A simulação deverá gerar ciclos anuais.

```text
ano 0 -> ano 1 -> ano 2 -> ... -> ano n
```

## Processos Simulados

- crescimento anual em DAP;
- crescimento anual em altura;
- mortalidade anual;
- remedição simulada;
- resposta ao perfil silvicultural;
- aplicação de limites biológicos.

## Aplicações

- stress test de prognose;
- validação de estabilidade;
- validação de drift;
- avaliação longitudinal;
- preparação para dados reais.

## Critérios de Aceitação

A simulação não poderá gerar:

- DAP negativo;
- altura negativa;
- mortalidade acima de 100%;
- população negativa;
- crescimento explosivo.

## Conclusão

A simulação temporal sintética representa a primeira validação longitudinal controlada da plataforma.
