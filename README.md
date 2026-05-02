# VBA Inventário Florestal

Repositório destinado ao desenvolvimento, organização e versionamento de rotinas computacionais aplicadas ao inventário florestal, modelagem biométrica, sortimento de madeira, distribuição diamétrica e automações associadas em VBA e Python.

## Objetivo

Organizar uma base técnica e computacional para:

- processar dados de inventário florestal;
- ajustar modelos hipsométricos, volumétricos e diamétricos;
- calcular estatísticas dendrométricas;
- simular sortimento de madeira;
- apoiar rotinas de automação em Excel/VBA;
- integrar futuramente módulos Python para análise, validação e geração de relatórios.

## Estrutura prevista

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── docs/
│   └── README.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── src/
│   └── inventario_florestal/
│       ├── __init__.py
│       ├── main.py
│       ├── biometria/
│       │   └── __init__.py
│       ├── distribuicao_diametrica/
│       │   └── __init__.py
│       ├── hipsometria/
│       │   └── __init__.py
│       ├── sortimento/
│       │   └── __init__.py
│       └── utils/
│           └── __init__.py
├── tests/
│   └── README.md
└── vba/
    └── README.md
```

## Módulos planejados

| Pasta | Finalidade |
|---|---|
| `src/inventario_florestal/biometria` | Cálculos dendrométricos básicos: DAP, área basal, volume, fatores de forma e estatísticas por parcela/talhão. |
| `src/inventario_florestal/distribuicao_diametrica` | Ajuste e comparação de distribuições diamétricas: Normal, Lognormal, Weibull e outras funções aplicáveis. |
| `src/inventario_florestal/hipsometria` | Ajuste, seleção e diagnóstico de modelos hipsométricos. |
| `src/inventario_florestal/sortimento` | Simulação de sortimentos, toras, classes de uso e prognose de produtos. |
| `src/inventario_florestal/utils` | Funções auxiliares, leitura de arquivos, validações e padronização de dados. |
| `vba` | Armazenamento dos módulos VBA exportados do Excel. |
| `data` | Dados brutos e processados. Evitar subir dados sensíveis ou bases pesadas. |
| `docs` | Documentação técnica, premissas biométricas, fórmulas e fluxos de uso. |
| `tests` | Testes automatizados dos módulos Python. |

## Convenções iniciais

- Código Python em `src/inventario_florestal/`.
- Módulos VBA exportados como `.bas`, `.cls` ou `.frm` em `vba/`.
- Dados originais em `data/raw/` e dados tratados em `data/processed/`.
- Não versionar arquivos grandes, sensíveis ou temporários.
- Documentar fórmulas, premissas e referências técnicas em `docs/`.

## Próximos passos

1. Inserir o primeiro código Python no módulo correspondente.
2. Separar funções por domínio técnico: biometria, hipsometria, distribuição diamétrica ou sortimento.
3. Criar testes mínimos em `tests/`.
4. Documentar entradas, saídas, unidades e premissas biométricas.
