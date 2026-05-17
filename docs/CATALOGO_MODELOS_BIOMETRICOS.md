# Catálogo Inicial de Modelos Biométricos

## Objetivo

Este documento registra o catálogo bruto inicial de equações e parâmetros biométricos indicados para o sistema de inventário, prognose e sortimento florestal.

O conteúdo deve ser tratado como base inicial de trabalho, e não como validação científica definitiva.

---

# Status do Catálogo

Status: **catálogo bruto pendente de validação**

Antes da implementação operacional, cada equação deverá passar por:

1. conferência bibliográfica;
2. conferência dimensional;
3. conferência algébrica;
4. definição da escala correta de logaritmo;
5. identificação da variável dependente real;
6. teste com dados sintéticos;
7. teste com dados reais;
8. análise de resíduos;
9. validação estatística;
10. documentação final.

---

# Grupos de Modelos Identificados

## Hipsometria

Quantidade inicial indicada: 32 modelos.

Aplicação:

- estimativa de altura total;
- preenchimento de alturas faltantes;
- modelagem altura-DAP;
- suporte à volumetria.

## Volumetria

Quantidade inicial indicada: 12 modelos.

Aplicação:

- volume individual;
- volume por hectare;
- volume comercial;
- suporte à prognose;
- suporte ao sortimento.

## Índice de Sítio

Quantidade inicial indicada: 11 modelos.

Aplicação:

- classificação produtiva;
- curvas de sítio;
- projeção de altura dominante;
- prognose.

## Taper / Afilamento

Quantidade inicial indicada: 8 modelos.

Aplicação:

- diâmetro ao longo do fuste;
- volume por seção;
- sortimento multiproduto;
- otimização econômica.

## Weibull

Quantidade inicial indicada: 5 métodos.

Aplicação:

- distribuição diamétrica;
- recuperação de parâmetros;
- prognose estrutural;
- simulação de desbastes.

## Sobrevivência / Mortalidade

Quantidade inicial indicada: 6 modelos.

Aplicação:

- projeção do número de árvores;
- mortalidade natural;
- densidade futura;
- prognose.

## Prognose

Componentes identificados:

- área basal;
- volume total;
- atributos diamétricos;
- distribuição diamétrica;
- sobrevivência.

## Sortimento

Cenários identificados:

- pessimista;
- realista;
- otimista.

---

# Espécies de Interesse

## Pinus

- Pinus taeda;
- Pinus elliottii.

## Eucalyptus

- Eucalyptus dunnii;
- Eucalyptus benthamii;
- Eucalyptus viminalis.

---

# Região de Interesse

- Santa Catarina;
- Paraná;
- Rio Grande do Sul;
- Sul do Brasil.

---

# Regras de Implementação

## Regra 1 — Nenhum modelo é fixo

Todos os modelos devem competir em torneio estatístico.

## Regra 2 — Modelos logarítmicos exigem correção de viés

Sempre que houver retransfomação de ln(Y) ou log10(Y) para a escala original, o sistema deve aplicar fator de correção apropriado.

## Regra 3 — Modelos com dependências adicionais exigem validação de variáveis

Exemplos:

- hdom;
- d_med;
- dg;
- G;
- idade;
- índice de sítio;
- densidade.

## Regra 4 — Modelos redundantes devem ser mantidos, mas marcados

Modelos matematicamente equivalentes ou quase equivalentes devem ser preservados no catálogo, porém com observação de redundância.

## Regra 5 — Fórmulas suspeitas não devem ser implementadas diretamente

Equações com inconsistência algébrica, dimensional ou bibliográfica devem ser classificadas como:

- `pendente_validacao`;
- `corrigir_formula`;
- `validar_fonte`;
- `nao_implementar_ainda`.

---

# Pontos Críticos Identificados no Catálogo Bruto

## Mistura de ln e log10

Alguns modelos misturam logaritmo natural e logaritmo decimal. Isso deve ser tratado explicitamente no motor estatístico.

## Equações com inversão não trivial

Modelos não lineares devem usar métodos iterativos quando necessário:

- Newton-Raphson;
- bissecção;
- secante.

## Modelos com alta colinearidade

Modelos polinomiais de alto grau e modelos com termos redundantes devem ser penalizados no ranking por instabilidade.

## Parâmetros econômicos

Valores de sortimento e conversão m³/t devem ser tratados como parâmetros de cenário, não como constantes científicas.

## Carbono e CO₂

Estimativas de carbono devem ser parametrizadas por espécie, densidade básica, casca, umidade e biomassa. Valores genéricos não devem ser usados como premissa universal.

---

# Próxima Conversão Recomendada

O catálogo deve ser migrado para um arquivo estruturado em:

`data/modelos/modelos_biometricos.yaml`

Com os campos mínimos:

```yaml
id:
grupo:
nome:
formula:
variavel_dependente:
variaveis_independentes:
tipo_regressao:
linearizavel:
eh_logaritmico:
base_logaritmo:
num_parametros:
fonte:
especie:
regiao:
status_validacao:
observacoes:
```

---

# Uso Futuro

Este catálogo servirá de base para:

- motor universal de ranking;
- validação automática de fórmulas;
- geração de regressões;
- documentação científica;
- testes automatizados;
- interface futura de seleção de modelos.
