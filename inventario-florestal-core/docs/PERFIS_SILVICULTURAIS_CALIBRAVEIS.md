# Perfis Silviculturais Calibráveis

## Objetivo

Definir a arquitetura de perfis silviculturais calibráveis da plataforma.

## Conceito

Os parâmetros esperados de crescimento e mortalidade devem ser separados dos limites matemáticos de segurança.

## Perfis Iniciais

| Perfil | Aplicação |
|---|---|
| conservador | povoamentos médios, degradados ou com baixa informação |
| operacional | povoamentos comerciais padrão |
| elite genética | materiais superiores e sítios excelentes |
| calibrado | parâmetros derivados de dados reais ou remedições |

## Variáveis por Perfil

Cada perfil deverá armazenar:

- incremento esperado em DAP;
- intervalo plausível de incremento;
- mortalidade anual esperada;
- faixa de mortalidade plausível;
- resposta ao desbaste;
- resposta à competição;
- resposta ao sítio;
- nível de confiança.

## Diretriz Técnica

Perfis silviculturais não devem substituir os guardrails biológicos.

Eles orientam a expectativa do modelo, enquanto os guardrails impedem saídas impossíveis.

## WestRock e Genética Elite

Materiais genéticos de alto desempenho devem ser representados como perfil calibrável, não como limite universal do simulador.

## Mortalidade

A mortalidade deverá ser dinâmica e dependente de:

- idade;
- densidade;
- competição;
- sítio;
- manejo;
- sanidade;
- material genético.

## Conclusão

Os perfis silviculturais calibráveis permitem regionalizar e adaptar a plataforma sem comprometer a estabilidade matemática.
