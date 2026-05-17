# Premissas Operacionais de Desbaste

## Objetivo

Consolidar as premissas já definidas para o módulo de manejo/desbaste da plataforma.

## Diretriz Geral

O desbaste deve ser tratado como intervenção silvicultural estruturada, não apenas como remoção aleatória de árvores.

A seleção das árvores removidas deve respeitar:

- tipo de desbaste;
- gatilho de parada;
- critérios qualitativos;
- classe sociológica;
- DAP individual;
- área basal individual;
- estabilidade do remanescente.

---

## Tipos de Desbaste

### 1. Desbaste Seletivo

Remove árvores individualmente conforme critério técnico.

Pode ter gatilho por:

- número de árvores;
- área basal removida;
- percentual de árvores;
- percentual de área basal.

### 2. Desbaste Sistemático

Remove árvores por padrão geométrico ou operacional.

Exemplos:

- remoção de linha;
- remoção por posição;
- abertura de corredor operacional.

### 3. Desbaste Misto

Combina remoção sistemática com seleção individual.

Exemplo:

- remoção sistemática de uma linha para corredor;
- remoção seletiva nas linhas remanescentes.

---

## Critérios Qualitativos de Remoção Seletiva

A ordem técnica já definida para remoção seletiva é:

1. copa quebrada;
2. bifurcação baixa;
3. macacão/prego;
4. torta;
5. bifurcação alta;
6. demais árvores de menor posição sociológica ou menor vigor.

## Desbaste por Número de Árvores

O gatilho de parada é a quantidade de árvores a remover.

A seleção deve seguir a ordem de qualidade, mas cada árvore removida carrega seu DAP, altura e área basal individual.

Portanto, o efeito no remanescente não é apenas numérico; altera também:

- área basal remanescente;
- distribuição diamétrica;
- competição;
- dominância;
- prognose futura.

## Desbaste por Área Basal / G

O gatilho de parada é a área basal removida.

A seleção das árvores deve seguir os mesmos critérios qualitativos do desbaste por número de árvores.

A diferença é que o encerramento ocorre quando a soma da área basal individual removida atinge o alvo definido.

## Área Basal Individual

A área basal individual deverá ser calculada por:

```text
gi = pi * DAP^2 / 40000
```

com DAP em centímetros e gi em metros quadrados.

## Efeito no Remanescente

Após qualquer desbaste, a plataforma deverá recalcular:

- número de árvores remanescentes;
- área basal remanescente;
- DAP médio;
- altura média;
- competição;
- dominância;
- prognose temporal.

## Diretriz de Implementação Atual

Nesta fase de consolidação, o módulo deve implementar apenas o necessário para:

- aplicar desbaste seletivo por N;
- aplicar desbaste seletivo por G;
- manter rastreabilidade de removidas e remanescentes;
- permitir testes operacionais.

Desbaste sistemático e misto devem permanecer documentados e preparados para integração posterior, sem expansão desnecessária neste momento.

## Conclusão

O módulo de desbaste deve respeitar as premissas silviculturais definidas e não pode ser reduzido a uma simples remoção percentual sem critério técnico.
