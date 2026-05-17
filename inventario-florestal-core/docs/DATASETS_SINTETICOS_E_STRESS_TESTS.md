# Datasets Sintéticos e Stress Tests

## Objetivo

Definir a geração de datasets sintéticos científicos para validação inicial da plataforma.

## Conceito

Datasets sintéticos devem ser usados antes de dados reais para testar estabilidade matemática, plausibilidade biológica e robustez operacional.

## Finalidade

- testar crescimento extremo;
- testar mortalidade extrema;
- testar competição extrema;
- testar desbastes intensos;
- testar drift adaptativo;
- testar estabilidade temporal.

## Cenários Sintéticos

| Cenário | Objetivo |
|---|---|
| povoamento normal | baseline |
| crescimento alto | genética superior |
| competição alta | superlotação |
| mortalidade alta | estresse |
| desbaste pesado | recuperação estrutural |
| baixa densidade | subutilização do sítio |

## Variáveis Mínimas

- id_arvore;
- parcela;
- dap_cm;
- altura_m;
- idade;
- qualidade;
- x;
- y;
- volume_m3;
- area_basal_m2.

## Regras de Validação

Os datasets deverão respeitar:

- DAP positivo;
- altura positiva;
- volume não negativo;
- área basal não negativa;
- coordenadas consistentes;
- distribuição diamétrica plausível.

## Conclusão

Os datasets sintéticos são a primeira camada experimental para validar a estabilidade da plataforma antes da conexão com datasets reais.
