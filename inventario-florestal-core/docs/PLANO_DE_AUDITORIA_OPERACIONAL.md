# Plano de Auditoria Operacional

## Objetivo

Definir a auditoria operacional dos módulos já implementados, sem expansão de escopo.

## Diretriz

A auditoria deverá priorizar correção, integração, estabilidade e testes.

## Módulos Críticos

| Módulo | Prioridade |
|---|---|
| biological_constraints | alta |
| silvicultural_profiles | alta |
| temporal_competition | alta |
| dynamic_dominance | alta |
| temporal_simulator | alta |
| synthetic_dataset_generator | alta |

## Verificações Obrigatórias

### Limites Biológicos

Validar:

- crescimento limitado;
- mortalidade entre 0 e 1;
- LAI plausível;
- variáveis não negativas.

### Perfis Silviculturais

Validar:

- perfil existente;
- perfil inexistente;
- coerência dos parâmetros.

### Competição Temporal

Validar:

- distância positiva;
- índice de competição finito;
- fator de crescimento não negativo;
- fator de mortalidade positivo.

### Dominância Dinâmica

Validar:

- classificação sociológica;
- DAP médio;
- altura média.

### Simulador Temporal

Validar:

- crescimento anual;
- mortalidade;
- sobrevivência;
- ausência de valores negativos.

## Conclusão

A auditoria operacional deverá transformar os módulos existentes em componentes testáveis, estáveis e rastreáveis.
