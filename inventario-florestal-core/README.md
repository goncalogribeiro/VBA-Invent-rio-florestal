# Inventário Florestal Core

Subprojeto limpo para evolução do software técnico-científico de inventário, biometria, prognose e sortimento florestal.

## Objetivo

Organizar uma base independente dentro do repositório para desenvolvimento controlado do sistema, evitando conflitos com arquivos antigos, integrações externas ou estruturas experimentais existentes na raiz.

## Escopo

O projeto contempla inicialmente:

- inventário florestal de Pinus e Eucalyptus;
- biometria florestal;
- equações hipsométricas;
- equações volumétricas;
- cubagem rigorosa;
- taper / afilamento;
- índice de sítio;
- distribuição diamétrica;
- sobrevivência e mortalidade;
- prognose;
- sortimento;
- ranking universal de modelos;
- integração futura VBA + Python.

## Espécies prioritárias

- Pinus taeda;
- Pinus elliottii;
- Eucalyptus dunnii;
- Eucalyptus benthamii;
- Eucalyptus viminalis.

## Região prioritária

Sul do Brasil, com foco em Santa Catarina, Paraná e Rio Grande do Sul.

## Arquitetura

- `docs/`: documentação técnica e científica;
- `data/modelos/`: catálogo estruturado de modelos biométricos;
- `src/inventario_florestal/`: pacote Python;
- `tests/`: testes automatizados;
- `vba/`: módulos VBA exportados da planilha operacional.

## Diretriz central

Nenhuma equação biométrica deve ser tratada como fixa. O sistema deve operar por torneio de modelos, com ajuste, diagnóstico, análise residual, correção de viés quando aplicável, ranking e seleção automática do melhor modelo aprovado.
