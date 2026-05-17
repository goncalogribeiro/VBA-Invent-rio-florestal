# Machine Learning Ecofisiológico

## Objetivo

Documentar a camada de machine learning ecofisiológico da plataforma.

## Conceito

O machine learning ecofisiológico deverá usar dados biométricos, ambientais, espaciais e fisiológicos para melhorar a previsão de crescimento, vigor, mortalidade e carbono.

## Entradas Prioritárias

- DAP;
- altura;
- idade;
- LAI;
- radiação interceptada;
- GPP;
- NPP;
- respiração;
- índice de competição;
- vigor NDVI;
- sítio;
- mortalidade observada;
- crescimento observado.

## Saídas Prioritárias

- crescimento esperado;
- vigor ecofisiológico;
- risco de mortalidade;
- carbono estimado;
- ajuste de prognose.

## Fluxo

inventário -> ecofisiologia -> aprendizado -> previsão -> recalibração.

## Papel das Remedições

As remedições deverão alimentar o aprendizado, comparando valores projetados e observados.

## Integração com a Plataforma

A camada deverá se conectar com:

- prognose;
- manejo;
- competição;
- sensoriamento remoto;
- persistência temporal;
- risco;
- economia.

## Diretriz Técnica

A primeira implementação deverá ser simples, auditável e determinística.

Modelos complexos, como redes neurais, deverão ser implementados somente após validação do pipeline e disponibilidade de dados suficientes.

## Conclusão

Machine learning ecofisiológico representa a camada de fechamento do ciclo adaptativo da plataforma, permitindo que o sistema aprenda com dados observados e melhore a prognose ao longo do tempo.
