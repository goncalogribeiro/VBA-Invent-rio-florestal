# Integração da Competição no Simulador Temporal

## Objetivo

Documentar a integração direta da competição espacial ao ciclo anual sintético.

## Conceito

A cada ano, o simulador deverá recalcular a competição individual e usar esse valor para alterar crescimento e mortalidade.

## Fluxo

ano t -> calcular competição -> ajustar crescimento -> ajustar mortalidade -> ano t+1.

## Efeitos

### Crescimento

Alta competição reduz o incremento individual em DAP.

### Mortalidade

Alta competição aumenta a probabilidade de mortalidade individual.

### Estrutura

A competição altera a distribuição diamétrica, favorecendo árvores dominantes e penalizando árvores dominadas.

## Critérios de Validação

- crescimento não pode ser negativo;
- mortalidade deve permanecer entre 0 e 1;
- população não pode ser negativa;
- DAP e altura devem permanecer positivos.

## Conclusão

A integração da competição ao simulador temporal representa a primeira dinâmica ecológica espacial completa da plataforma.
