# Diretrizes Técnicas de Manejo e Desbaste de Pinus

## Objetivo

Registrar as diretrizes técnicas preliminares para implementação futura do simulador dinâmico de manejo e desbaste.

Este documento serve como base de auditoria para as próximas camadas:

- `EventoManejo`;
- `RegimeManejoTemporal`;
- simulador de desbaste;
- redistribuição diamétrica pós-desbaste;
- crescimento pós-intervenção;
- receitas intermediárias.

---

# 1. Conceito Central

O desbaste é uma intervenção silvicultural destinada a reduzir a densidade do povoamento, redistribuindo recursos de crescimento para as árvores remanescentes.

Objetivos principais:

- reduzir competição;
- aumentar crescimento diamétrico individual;
- melhorar qualidade final;
- gerar receitas intermediárias;
- direcionar produção para sortimentos de maior valor.

---

# 2. Manejo sem Desbaste

O manejo sem desbaste deve ser tratado como regime válido, especialmente quando o objetivo principal for:

- maximizar volume total;
- produzir biomassa;
- produzir celulose;
- produzir energia;
- operar com rotações mais curtas.

Observação técnica:

Manejo sem desbaste pode maximizar volume bruto, mas não necessariamente maximiza receita líquida ou produção de sortimentos nobres.

---

# 3. Classes de Desbaste

## 3.1 Desbaste Sistemático

Remoção com padrão geométrico.

Exemplos:

- retirada de linha;
- abertura de corredor;
- remoção periódica por fileira.

Uso principal:

- primeiro desbaste;
- acesso mecanizado;
- redução de custo operacional.

Limitação:

- pode remover árvores boas;
- pode manter árvores ruins.

---

## 3.2 Desbaste Seletivo por Baixo

Remove preferencialmente:

- dominadas;
- suprimidas;
- tortas;
- bifurcadas;
- doentes;
- árvores de baixo vigor.

Uso principal:

- melhoria qualitativa;
- redução de competição inferior;
- formação de fustes comerciais de maior valor.

---

## 3.3 Desbaste Seletivo pelo Alto

Remove árvores competidoras no estrato dominante ou codominante, principalmente quando competem com árvores elite.

Uso principal:

- manejo de qualidade;
- liberação de copa;
- maximização de árvores potenciais.

Observação:

Deve ser implementado com cuidado, pois pode remover volume de alto valor se mal parametrizado.

---

## 3.4 Desbaste Misto

Combinação de:

- sistemático;
- seletivo;
- sanitário;
- operacional.

Exemplo:

```text
remoção de linha + seleção nas linhas remanescentes
```

---

# 4. Intensidade de Desbaste

A intensidade poderá ser expressa por:

- percentual de árvores removidas;
- percentual de área basal removida;
- percentual de volume removido;
- regras por classe diamétrica.

Faixas operacionais preliminares:

| Intensidade | Interpretação |
|---|---|
| até 30% | leve/moderado |
| 30–40% | moderado |
| 40–50% | pesado |
| acima de 50% | exige justificativa técnica |

Observação crítica:

Essas faixas não devem ser hardcoded como regra universal. Devem ser configuráveis por espécie, sítio, idade, densidade inicial, risco fitossanitário e objetivo industrial.

---

# 5. Riscos de Desbaste Excessivo

Desbastes excessivos podem:

- reduzir volume total acumulado;
- abrir clareiras;
- aumentar matocompetição;
- favorecer galhos grossos;
- aumentar conicidade;
- aumentar instabilidade ao vento;
- afetar qualidade de madeira sólida.

---

# 6. Riscos de Ausência de Desbaste

Povoamentos superadensados podem apresentar:

- competição excessiva;
- mortalidade natural;
- redução de crescimento individual;
- maior suscetibilidade a estresse;
- maior risco fitossanitário.

---

# 7. Vespa-da-madeira

A ocorrência de `Sirex noctilio` deve ser considerada em módulos futuros de risco fitossanitário.

Premissas operacionais:

- povoamentos estressados e superadensados devem receber alerta;
- desbaste sanitário pode ser recomendado como evento especial;
- árvores atacadas devem ser removidas conforme critério sanitário.

---

# 8. Densidade Básica da Madeira

A afirmação de que múltiplos desbastes não alteram significativamente a densidade básica ponderada deve ser tratada como hipótese técnica dependente de fonte e região.

No código, isso NÃO deve ser assumido como regra universal.

Diretriz:

- manter tabela de conversão m3 → ton por idade;
- permitir ajustes por espécie/material genético;
- permitir calibração por dados locais.

---

# 9. Diretriz para Implementação no Código

O manejo deve ser implementado em três níveis:

## Nível 1 — Estrutural

- representar eventos;
- representar regimes;
- validar sequência temporal.

## Nível 2 — Silvicultural

- aplicar remoção;
- recalcular N, G, Dg;
- recalcular distribuição diamétrica;
- diferenciar removido e remanescente.

## Nível 3 — Econômico

- calcular receita de desbaste;
- calcular receita do corte final;
- montar fluxo de caixa;
- comparar regimes.

---

# 10. Tipos de Evento de Manejo

Tipos previstos:

| Tipo | Uso |
|---|---|
| desbaste_sistematico | remoção por padrão |
| desbaste_por_baixo | remoção de classes inferiores |
| desbaste_pelo_alto | remoção seletiva superior |
| desbaste_misto | combinação |
| desbaste_sanitario | remoção fitossanitária |
| corte_final | encerramento da rotação |

---

# 11. Estado Atual

Este documento NÃO significa que o simulador de desbaste já esteja completo.

Ele registra as premissas para a próxima implementação:

```text
EventoManejo → RegimeManejoTemporal → Simulador Dinâmico
```

---

# 12. Referências Técnicas a Consultar/Consolidar

Fontes a incorporar na validação final:

- Embrapa Florestas — Pinus e manejo;
- literatura de crescimento e produção de Pinus no Sul do Brasil;
- SisPinus / SisEucalipto;
- Clutter;
- Bailey & Clutter;
- Pienaar & Shiver;
- Ferraz Filho;
- Viana;
- trabalhos sobre Sirex noctilio;
- estudos de densidade básica em Pinus taeda sob diferentes regimes.
