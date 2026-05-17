# Pipeline Biométrico Universal

## Objetivo

Documentar a arquitetura estatística e biométrica do núcleo universal do sistema de inventário florestal.

O objetivo desta camada é permitir:

- ajuste automatizado de modelos;
- comparação científica entre equações;
- rastreabilidade completa;
- auditoria estatística;
- torneio universal de modelos biométricos.

---

# Arquitetura Geral

```text
YAML → Schema → Executor → Ajuste → Diagnóstico → Benchmark → Ranking
```

---

# Camadas do Sistema

## 1. Catálogo YAML

Responsável por armazenar:

- equações;
- parâmetros;
- variáveis;
- referências bibliográficas;
- classificação biométrica;
- configuração NLS.

Exemplo:

```yaml
id: H28
nome: Chapman-Richards
```

---

## 2. Schema Pydantic

Arquivo:

```text
modelos/schema.py
```

Responsável por:

- validação estrutural;
- integridade dos modelos;
- controle de tipos;
- classificação biométrica;
- configuração de modelos não lineares.

---

## 3. Ajuste Linear

Arquivos principais:

```text
ajuste/linear_regression.py
ajuste/fit_from_model.py
```

Recursos:

- OLS;
- modelos linearizados;
- intercepto opcional;
- métricas biométricas;
- PRESS;
- resíduos;
- Cook Distance;
- AIC/BIC.

---

## 4. Diagnóstico Residual

Arquivo:

```text
ranking/residual_analysis.py
```

Recursos:

- Breusch-Pagan;
- White;
- PRESS residual;
- Cook Distance;
- leverage;
- análise residual universal.

---

## 5. WLS Automático

Arquivos:

```text
ajuste/weighted_regression.py
ajuste/auto_wls.py
benchmark/ols_wls_benchmark.py
```

Fluxo:

```text
OLS → Diagnóstico → Heterocedasticidade → WLS → Comparação → Recomendação
```

Critérios principais:

- R² ajustado;
- Syx%;
- PRESS RMSE.

---

## 6. Ajuste Não Linear (NLS)

Arquivos:

```text
ajuste/nonlinear_regression.py
ajuste/fit_nonlinear_from_model.py
```

Base matemática:

```python
scipy.optimize.curve_fit
```

Características:

- chute inicial obrigatório;
- limites opcionais;
- convergência controlada;
- métricas biométricas;
- diagnóstico residual.

---

# Biblioteca de Funções Não Lineares

Arquivo:

```text
modelos/nonlinear_functions.py
```

Funções atualmente implementadas:

| Modelo | Status |
|---|---|
| Chapman-Richards | implementado |
| Näslund | implementado |
| Silva-Bailey | implementado |
| Granemann | experimental |

---

# Modelo Experimental Granemann

O modelo hipsométrico Granemann foi implementado como:

- modelo experimental;
- dependente de povoamento;
- não validado cientificamente ainda.

Equação:

```text
h = 1.3 + (hdom - 1.3)
    * [1 - exp(-β0 * (d/d_med)^β1 * sqrt(G/100))]
```

Variáveis:

| Variável | Descrição |
|---|---|
| d | DAP individual |
| d_med | DAP médio |
| hdom | altura dominante |
| G | área basal |

---

# Ranking Universal

Arquivo:

```text
ranking/tournament.py
```

O torneio universal executa:

| Tipo | Método |
|---|---|
| linear | OLS/WLS |
| linearizado | OLS |
| não linear | NLS |

Critérios:

- R² ajustado;
- Syx;
- Syx%;
- PRESS;
- penalizações residuais.

---

# Filosofia Científica do Sistema

O sistema NÃO deve:

- escolher modelos apenas por R²;
- aceitar parser matemático arbitrário;
- tratar NLS como caixa preta;
- ignorar resíduos;
- ignorar heterocedasticidade.

O sistema DEVE:

- priorizar estabilidade biométrica;
- manter auditabilidade;
- permitir rastreabilidade;
- registrar falhas de convergência;
- comparar modelos por múltiplos critérios.

---

# Situação Atual do Núcleo

| Camada | Status |
|---|---|
| YAML | operacional |
| Schema | operacional |
| OLS | operacional |
| WLS | operacional |
| NLS | operacional |
| Benchmark | operacional |
| Ranking | operacional |
| Torneio Universal | operacional |

---

# Próximas Etapas

## Prioridade Alta

- Weibull;
- taper avançado;
- prognose;
- modelos de sobrevivência;
- persistência de resultados.

## Prioridade Média

- gráficos automáticos;
- relatórios científicos;
- exportação auditável.

## Prioridade Futura

- Bayesian fitting;
- ensemble biométrico;
- machine learning auxiliar.
