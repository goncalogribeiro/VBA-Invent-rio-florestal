# Dominância Dinâmica e Estratificação Sociológica

## Objetivo

Documentar a inclusão de dominância dinâmica e estratificação sociológica no simulador temporal.

## Conceito

A posição sociológica da árvore não deve ser fixa. Ela pode mudar ao longo do tempo conforme crescimento, competição, mortalidade e manejo.

## Classes Iniciais

| Classe | Interpretação |
|---|---|
| dominante | árvore acima da estrutura média |
| codominante | árvore próxima da estrutura média |
| dominada | árvore abaixo da estrutura média |
| suprimida | árvore fortemente inferior e sob competição |

## Variáveis Usadas

- DAP individual;
- DAP médio do povoamento;
- altura individual;
- altura média;
- índice de competição;
- distribuição estrutural.

## Aplicações

A dominância dinâmica deverá alimentar:

- crescimento individual;
- mortalidade;
- competição de copa;
- interceptação luminosa;
- sucessão espacial;
- resposta ao desbaste.

## Fluxo

ano t -> estrutura do povoamento -> classe sociológica -> crescimento/mortalidade -> ano t+1.

## Conclusão

A dominância dinâmica representa a transição do simulador para uma dinâmica estrutural de dossel mais realista.
