# Revisão de Pipelines e Dependências

## Objetivo

Documentar a revisão estrutural dos pipelines da plataforma.

## Pipeline Principal

inventário -> biometria -> prognose -> manejo -> economia -> ecofisiologia -> aprendizado.

## Dependências Críticas

### Inventário

Responsável por:

- entrada de dados;
- remedições;
- persistência temporal.

### Biometria

Responsável por:

- hipsometria;
- volumetria;
- taper;
- sortimento.

### Prognose

Responsável por:

- crescimento;
- mortalidade;
- dinâmica ecológica.

### Manejo

Responsável por:

- desbaste;
- regimes;
- cenários.

### Economia

Responsável por:

- preços;
- conversões;
- receitas;
- Monte Carlo.

### Ecofisiologia

Responsável por:

- LAI;
- GPP;
- NPP;
- carbono.

### Aprendizado

Responsável por:

- recalibração;
- aprendizado;
- ajuste adaptativo.

## Pontos Críticos

Verificar:

- dependências circulares;
- pipelines quebrados;
- inconsistências temporais;
- ausência de persistência;
- duplicidade de cálculo.

## Conclusão

A revisão estrutural deverá validar a consistência operacional da plataforma antes da fase de testes.
