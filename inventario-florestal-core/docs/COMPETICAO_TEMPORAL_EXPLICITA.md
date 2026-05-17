# Competição Temporal Explícita

## Objetivo

Documentar a integração da competição espacial ao simulador temporal sintético.

## Conceito

O crescimento e a mortalidade não devem ser independentes entre árvores.

A competição deve variar a cada ciclo anual conforme:

- densidade;
- DAP das vizinhas;
- distância;
- sobrevivência;
- crescimento acumulado.

## Fluxo

árvores no ano t -> competição -> crescimento ajustado -> mortalidade ajustada -> ano t+1.

## Variáveis Usadas

- DAP;
- coordenadas x/y;
- distância entre árvores;
- índice competitivo;
- perfil silvicultural.

## Efeitos Esperados

A competição elevada deverá:

- reduzir crescimento individual;
- aumentar mortalidade;
- intensificar diferenciação entre árvores;
- alterar estrutura residual.

## Critérios de Validação

A simulação deverá manter:

- DAP positivo;
- mortalidade entre 0 e 1;
- crescimento dentro dos guardrails;
- população não negativa.

## Conclusão

A competição temporal explícita representa a primeira etapa da dinâmica ecológica emergente da plataforma.
