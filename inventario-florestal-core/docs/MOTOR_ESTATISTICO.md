# Motor Estatístico e Procedimentos de Auditoria

## Objetivo

Este documento registra os procedimentos estatísticos implementados no núcleo `inventario-florestal-core`, com finalidade de auditoria técnica, rastreabilidade científica e manutenção futura do sistema.

O motor estatístico tem como objetivo ajustar, diagnosticar, corrigir, comparar e ranquear modelos biométricos utilizados em inventário florestal, volumetria, hipsometria, taper, índice de sítio, prognose e sortimento.

---

# Diretriz central

O sistema deve utilizar preferencialmente o **R² ajustado**, e não o R² simples, como critério positivo principal de seleção.

O R² simples tende a aumentar com a inclusão de novas variáveis, mesmo que essas variáveis não melhorem efetivamente a capacidade explicativa do modelo. O R² ajustado penaliza o excesso de parâmetros e é mais adequado para torneios de modelos biométricos com diferentes estruturas matemáticas.

---

# Fluxo geral do motor

```text
Catálogo YAML
    ↓
Validação via schema
    ↓
Interpretação da fórmula
    ↓
Ajuste OLS
    ↓
Diagnóstico residual
    ↓
Correção de viés, quando aplicável
    ↓
Detecção de heterocedasticidade
    ↓
WLS, quando tecnicamente indicado
    ↓
Ranking robusto
    ↓
Seleção do melhor modelo aprovado
```

---

# 1. Catálogo de modelos

## Arquivo

```text
data/modelos/modelos_biometricos.yaml
```

## Finalidade

Armazenar as equações biométricas de forma estruturada, evitando que os modelos fiquem fixos diretamente no código.

## Campos principais

- `id`;
- `grupo`;
- `nome`;
- `formula`;
- `variavel_dependente`;
- `variaveis_independentes`;
- `tipo_regressao`;
- `eh_logaritmico`;
- `base_logaritmo`;
- `metodo_correcao_vies`;
- `fonte`;
- `status_validacao`.

## Finalidade de auditoria

Permite rastrear qual equação foi testada, qual fonte bibliográfica foi indicada, qual grupo biométrico a equação pertence e se ela ainda está pendente de validação.

---

# 2. Schema de validação

## Arquivo

```text
src/inventario_florestal/modelos/schema.py
```

## Finalidade

Validar a estrutura dos modelos biométricos lidos do YAML.

## Função técnica

Evita que modelos incompletos, com grupo inválido, tipo de regressão inválido ou estrutura inconsistente sejam processados pelo motor estatístico.

---

# 3. Parser YAML

## Arquivo

```text
src/inventario_florestal/utils/model_parser.py
```

## Finalidade

Carregar o catálogo YAML e converter seu conteúdo em objetos validados.

## Procedimento

1. recebe o caminho do YAML;
2. verifica se o arquivo existe;
3. lê o conteúdo;
4. valida com `CatalogoModelos`;
5. retorna o catálogo estruturado.

---

# 4. Interpretação de fórmulas lineares

## Arquivo

```text
src/inventario_florestal/ajuste/formula_linear.py
```

## Finalidade

Converter fórmulas biométricas lineares ou linearizadas em matriz de resposta `y` e matriz de preditores `X`.

## Exemplos suportados

```text
h = beta0 + beta1*d
ln(V) = beta0 + beta1*ln(DAP) + beta2*ln(H)
V = beta1*DAP^2*H
```

## Procedimentos executados

- identifica a variável dependente;
- identifica transformações logarítmicas;
- interpreta termos independentes;
- gera `y` transformado, quando necessário;
- gera matriz `X` para regressão.

## Finalidade de auditoria

Permite verificar como a fórmula declarada no catálogo foi convertida para ajuste estatístico.

---

# 5. Regressão OLS

## Arquivo

```text
src/inventario_florestal/ajuste/linear_regression.py
```

## Finalidade

Ajustar modelos lineares e linearizados por mínimos quadrados ordinários.

## Saídas principais

- coeficientes;
- valores estimados;
- resíduos;
- matriz de projeto `X`;
- AIC;
- BIC;
- R²;
- R² ajustado;
- Syx;
- Syx%;
- RMSE;
- MAE;
- Bias.

## Finalidade de auditoria

Permite reproduzir o ajuste e rastrear os coeficientes, métricas e resíduos de cada modelo testado.

---

# 6. Correção de viés

## Arquivo

```text
src/inventario_florestal/ranking/bias.py
```

## Finalidade

Corrigir a retransfomação de modelos ajustados em escala logarítmica.

## Método inicial implementado

Fator de Meyer:

```text
FM = exp(0,5 × QM_res)
```

## Aplicação

```text
Y_corrigido = exp(Y_log_estimado) × FM
```

ou, para logaritmo decimal:

```text
Y_corrigido = 10^(Y_log_estimado) × FM
```

## Finalidade de auditoria

Permite identificar se a estimativa final foi corrigida após a retransfomação para a escala original.

---

# 7. Diagnóstico residual

## Arquivo

```text
src/inventario_florestal/ranking/residual_analysis.py
```

## Finalidade

Avaliar a estabilidade estatística e biométrica dos modelos ajustados.

## Indicadores implementados

### Resíduo simples

```text
e_i = Y_i - Ŷ_i
```

### Resíduo percentual

```text
e% = 100 × (Y_i - Ŷ_i) / Y_i
```

### Resíduo padronizado

```text
e_pad = e_i / s_e
```

### Leverage

```text
H = X(X'X)^-1X'
```

O leverage é a diagonal da matriz hat.

### PRESS real

```text
PRESS = Σ(e_i / (1 - h_ii))²
```

### Cook Distance

```text
D_i = (e_i² / (p × MSE)) × [h_ii / (1 - h_ii)²]
```

### Observações influentes

Critério inicial:

```text
D_i > 4/n
```

## Finalidade de auditoria

Permite identificar se o modelo depende de observações influentes, outliers ou pontos de alta alavancagem.

---

# 8. Heterocedasticidade

## Arquivo

```text
src/inventario_florestal/ranking/residual_analysis.py
```

## Testes implementados

- Breusch-Pagan;
- White.

## Hipótese nula

```text
H0: variância constante dos resíduos
```

## Critério inicial

```text
p < 0,05 → heterocedasticidade detectada
```

## Finalidade

Identificar modelos nos quais a variância dos resíduos muda em função dos preditores.

## Importância biométrica

A heterocedasticidade é frequente em modelos de altura, volume e taper, especialmente quando há aumento da variância residual em árvores maiores.

---

# 9. Regressão WLS

## Arquivo

```text
src/inventario_florestal/ajuste/weighted_regression.py
```

## Finalidade

Ajustar modelos por mínimos quadrados ponderados quando houver evidência de heterocedasticidade.

## Condição técnica

Todos os pesos devem ser positivos.

```text
w_i > 0
```

## Saídas principais

- coeficientes ponderados;
- resíduos;
- métricas;
- AIC;
- BIC;
- matriz X;
- pesos utilizados.

---

# 10. Geração automática de pesos

## Arquivo

```text
src/inventario_florestal/ajuste/weights.py
```

## Estratégias implementadas

### Inverso da variável ao quadrado

```text
w_i = 1 / x_i²
```

### Inverso do estimado ao quadrado

```text
w_i = 1 / Ŷ_i²
```

### Inverso do resíduo absoluto

```text
w_i = 1 / |e_i|
```

### Inverso do resíduo ao quadrado

```text
w_i = 1 / e_i²
```

## Observação técnica

Pesos derivados diretamente dos resíduos devem ser usados com cautela, pois podem reduzir excessivamente a influência de observações importantes.

## Normalização

Os pesos são normalizados pela média:

```text
w_norm = w / média(w)
```

Isso reduz instabilidade numérica.

---

# 11. Ranking biométrico

## Arquivo

```text
src/inventario_florestal/ranking/ranking_engine.py
```

## Critério positivo principal

- R² ajustado.

## Penalizações iniciais

- Syx%;
- Bias absoluto;
- PRESS RMSE;
- erro percentual médio absoluto;
- erro percentual máximo absoluto;
- Cook Distance máximo;
- número de observações influentes.

## Finalidade

Ranquear modelos não apenas por ajuste médio, mas também por estabilidade, parcimônia e comportamento residual.

---

# 12. Torneio de modelos

## Arquivo

```text
src/inventario_florestal/ranking/tournament.py
```

## Finalidade

Executar competição entre modelos de um mesmo grupo biométrico.

## Procedimento

1. filtra os modelos por grupo;
2. ignora modelos não suportados pela etapa atual;
3. ajusta cada modelo;
4. calcula métricas;
5. agrega diagnóstico residual;
6. calcula pontuação;
7. ordena modelos;
8. retorna vencedor e modelos com erro.

---

# Estado atual do motor

## Implementado

- Catálogo YAML;
- schema de validação;
- parser YAML;
- interpretação de fórmulas lineares;
- OLS;
- R² ajustado;
- Syx e Syx%;
- correção de Meyer;
- resíduos percentuais;
- leverage;
- PRESS real;
- Cook Distance;
- Breusch-Pagan;
- White;
- WLS;
- geração automática de pesos;
- ranking robusto inicial;
- torneio linear.

## Ainda não implementado

- Auto-WLS completo;
- comparação automática OLS vs WLS;
- regressão não linear;
- modelos taper não lineares;
- Weibull;
- persistência de resultados;
- relatórios automáticos.

---

# Diretriz de auditoria

Todo novo método estatístico deve ser documentado neste arquivo, incluindo:

1. finalidade;
2. fórmula;
3. arquivo de implementação;
4. entrada;
5. saída;
6. limitações;
7. impacto no ranking.
