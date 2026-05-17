from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import sqlite3


@dataclass(frozen=True)
class PrognoseVersionada:
    identificador: str
    data_execucao: datetime
    modelo: str
    cenario: str
    resultado: float


class ErroPersistenciaSQL(Exception):
    pass



def inicializar_banco(
    caminho_banco: str,
) -> None:
    """
    Inicializa infraestrutura SQL simplificada.
    """

    conexao = sqlite3.connect(caminho_banco)

    cursor = conexao.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prognoses (
            identificador TEXT,
            data_execucao TEXT,
            modelo TEXT,
            cenario TEXT,
            resultado REAL
        )
        """
    )

    conexao.commit()
    conexao.close()



def salvar_prognose(
    caminho_banco: str,
    prognose: PrognoseVersionada,
) -> None:
    """
    Salva prognose versionada.
    """

    conexao = sqlite3.connect(caminho_banco)

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO prognoses (
            identificador,
            data_execucao,
            modelo,
            cenario,
            resultado
        ) VALUES (?, ?, ?, ?, ?)
        """,
        (
            prognose.identificador,
            prognose.data_execucao.isoformat(),
            prognose.modelo,
            prognose.cenario,
            prognose.resultado,
        ),
    )

    conexao.commit()
    conexao.close()



def listar_prognoses(
    caminho_banco: str,
) -> list[tuple]:
    """
    Lista prognoses persistidas.
    """

    conexao = sqlite3.connect(caminho_banco)

    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM prognoses"
    )

    resultados = cursor.fetchall()

    conexao.close()

    return resultados
