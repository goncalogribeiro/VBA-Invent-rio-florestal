from __future__ import annotations

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS fazendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    area_ha REAL
);

CREATE TABLE IF NOT EXISTS talhoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fazenda_id INTEGER,
    codigo TEXT,
    especie TEXT,
    area_ha REAL,
    FOREIGN KEY (fazenda_id) REFERENCES fazendas(id)
);

CREATE TABLE IF NOT EXISTS parcelas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id INTEGER,
    codigo TEXT,
    area_m2 REAL,
    FOREIGN KEY (talhao_id) REFERENCES talhoes(id)
);

CREATE TABLE IF NOT EXISTS arvores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parcela_id INTEGER,
    numero_arvore INTEGER,
    especie TEXT,
    FOREIGN KEY (parcela_id) REFERENCES parcelas(id)
);

CREATE TABLE IF NOT EXISTS medicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    arvore_id INTEGER,
    data_medicao TEXT,
    dap_cm REAL,
    altura_m REAL,
    volume_m3 REAL,
    FOREIGN KEY (arvore_id) REFERENCES arvores(id)
);

CREATE TABLE IF NOT EXISTS prognoses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id INTEGER,
    data_execucao TEXT,
    modelo TEXT,
    cenario TEXT,
    resultado REAL,
    FOREIGN KEY (talhao_id) REFERENCES talhoes(id)
);

CREATE TABLE IF NOT EXISTS manejos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id INTEGER,
    data_operacao TEXT,
    tipo_manejo TEXT,
    intensidade REAL,
    FOREIGN KEY (talhao_id) REFERENCES talhoes(id)
);

CREATE TABLE IF NOT EXISTS economia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id INTEGER,
    data_referencia TEXT,
    receita REAL,
    custo REAL,
    vpl REAL,
    FOREIGN KEY (talhao_id) REFERENCES talhoes(id)
);
"""
