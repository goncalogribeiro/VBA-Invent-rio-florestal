# Arquitetura do Sistema

## Objetivo

Sistema técnico-científico para inventário florestal de Pinus e Eucalyptus no Sul do Brasil, utilizando arquitetura híbrida:

- Excel/VBA para operação florestal e automação operacional;
- Python para processamento biométrico avançado, regressões, ranking estatístico e expansão científica.

O sistema deve operar com rastreabilidade matemática, auditoria estatística e seleção automática de modelos biométricos.

---

# Filosofia do Projeto

O software não deve utilizar modelos fixos.

Toda modelagem biométrica deverá operar por meio de:

1. ajuste simultâneo de múltiplas equações;
2. avaliação estatística completa;
3. análise de resíduos;
4. correção de viés quando aplicável;
5. ranqueamento técnico;
6. seleção automática do melhor modelo aprovado.

Esta filosofia deve ser aplicada para:

- equações hipsométricas;
- equações volumétricas;
- funções taper;
- índice de sítio;
- prognose;
- sortimento;
- distribuições diamétricas;
- futuros módulos biométricos.

---

# Arquitetura Geral

## Camada VBA

Responsável por:

- entrada operacional de dados;
- integração com planilhas Excel;
- automação operacional;
- interface do usuário;
- relatórios rápidos;
- integração com tabelas e dashboards.

## Camada Python

Responsável por:

- regressões estatísticas;
- ranking de modelos;
- taper;
- prognose;
- distribuição diamétrica;
- auditoria matemática;
- validações científicas;
- processamento pesado;
- futuras integrações GIS e machine learning.

---

# Fluxo Operacional

Campo → Validação → Hipso → Volume → Taper → Sortimento → Estatísticas → Prognose → Relatórios

---

# Estrutura de Pastas

## docs/

Documentação técnica, premissas biométricas, fórmulas e arquitetura.

## data/

Armazenamento de dados brutos e processados.

### data/raw/

Dados originais de inventário.

### data/processed/

Dados tratados e padronizados.

## src/inventario_florestal/

Código Python principal.

## vba/

Módulos VBA exportados da planilha Excel.

## tests/

Testes automatizados.

---

# Motores Técnicos

## biometria

Cálculos dendrométricos fundamentais:

- DAP;
- CAP;
- área basal;
- volume;
- densidade;
- fatores de forma;
- estatísticas florestais.

## hipsometria

Ajuste, diagnóstico e ranking de modelos hipsométricos.

## volumetria

Modelagem volumétrica e regressões.

## taper

Funções de afilamento.

## sitio

Modelagem de índice de sítio.

## sortimento

Classificação industrial e econômica da madeira.

## vies

Correções estatísticas para modelos transformados.

## ranking

Motor genérico de competição de modelos biométricos.

---

# Regras Técnicas Obrigatórias

- Nunca utilizar equações sem validação estatística.
- Sempre gerar resíduos.
- Sempre avaliar heterocedasticidade.
- Sempre aplicar correção de viés em modelos logarítmicos.
- Sempre documentar unidade de entrada e saída.
- Sempre preservar rastreabilidade matemática.
- Sempre priorizar literatura científica regional.

---

# Espécies Prioritárias

## Pinus

- Pinus taeda
- Pinus elliottii

## Eucalyptus

- Eucalyptus dunnii
- Eucalyptus benthamii
- Eucalyptus viminalis

Foco geográfico prioritário:

- Santa Catarina;
- Paraná;
- Rio Grande do Sul.

---

# Fontes Científicas Prioritárias

- EMBRAPA
- IPEF
- UFPR
- UDESC
- UFSM
- Revistas científicas florestais
- Teses e dissertações
- Publicações técnicas regionais

---

# Compatibilidade

Toda evolução futura deve preservar:

- compatibilidade com a planilha operacional atual;
- compatibilidade dos módulos VBA;
- consistência das fórmulas históricas;
- rastreabilidade dos resultados.
