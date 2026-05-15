# AGENTS.md — Inventário Florestal de Pinus

## Objetivo do projeto
Este repositório contém um software técnico-científico para inventário florestal de Pinus, com base operacional atual em Excel/VBA e evolução planejada para Python.

## Regras obrigatórias
- Não quebrar rotinas VBA já funcionais.
- Toda alteração deve preservar compatibilidade com a planilha Excel existente.
- Separar lógica técnica de interface/botões.
- Não misturar biometria, hipsometria, sortimento, taper e ranking no mesmo módulo.
- Toda equação deve ter unidade, entrada, saída e premissa documentada.
- Todo modelo ajustado deve gerar diagnóstico estatístico e ranking.
- Modelos logarítmicos devem prever correção de viés.
- Dados sensíveis ou bases reais pesadas não devem ser versionados.

## Estrutura
- Código VBA exportado em `vba/`.
- Código Python em `src/inventario_florestal/`.
- Documentação técnica em `docs/`.
- Dados brutos em `data/raw/`.
- Dados tratados em `data/processed/`.
- Testes em `tests/`.

## Prioridade técnica
1. Consolidar VBA atual.
2. Documentar fluxo operacional.
3. Criar motor genérico de ranking de modelos.
4. Implantar cubagem rigorosa.
5. Implantar regressões volumétricas.
6. Implantar correções de viés.
7. Implantar taper.
8. Integrar sortimento por taper.
9. Implantar índice de sítio.
10. Migrar gradualmente rotinas para Python.

## Padrão de resposta esperado
Ao alterar código:
1. explicar o problema;
2. indicar arquivos afetados;
3. preservar compatibilidade;
4. propor teste mínimo;
5. atualizar documentação quando necessário.
