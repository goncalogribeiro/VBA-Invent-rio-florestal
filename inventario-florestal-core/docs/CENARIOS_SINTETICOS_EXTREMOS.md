# Cenários Sintéticos Extremos

## Objetivo

Documentar os cenários sintéticos extremos usados para stress test da prognose.

## Conceito

Os cenários extremos têm a função de pressionar o motor da plataforma e identificar instabilidades matemáticas, ecológicas e temporais.

## Cenários Prioritários

| Cenário | Objetivo |
|---|---|
| normal | baseline operacional |
| superlotado | testar competição extrema |
| baixa densidade | testar subutilização do sítio |
| elite genética | testar alto incremento |
| sítio ruim | testar crescimento limitado |
| mortalidade alta | testar colapso populacional |
| desbaste pesado | testar recuperação estrutural |

## Variáveis Controladas

- número de árvores;
- faixa de DAP;
- faixa de altura;
- idade;
- espaçamento espacial;
- pressão competitiva;
- perfil silvicultural.

## Critérios de Aceitação

A plataforma deverá impedir:

- crescimento explosivo;
- mortalidade impossível;
- volume negativo;
- área basal negativa;
- LAI impossível;
- drift adaptativo.

## Conclusão

Os cenários sintéticos extremos representam a primeira etapa prática da validação dinâmica da plataforma.
