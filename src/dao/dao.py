from abc import ABC, abstractmethod
import sqlite3 # Só para ter o tipo "Connection".
from typing import Any

class AbstractDAO(ABC):
    """Classe Abstrata de todos os DAOs contendo a 'generalização' de suas funções. Ela também padronizará os DAOs para facilitar os seus usos."""
    _db_path = "./data/database.db" # Caminho do arquivo do Banco de Dados. Esse caminho é em relação a pasta "src".

    @classmethod
    def _get_db_connection(cls) -> sqlite3.Connection: 
        """Retorna o objeto da conexão com o Banco de Dados."""
        conn = sqlite3.connect(cls._db_path)
        conn.row_factory = sqlite3.Row # Permite acessar o Banco de Dados como um dicionário ao invés de uma tupla.
        conn.execute("PRAGMA foreign_keys = ON") # Por algum motivo o SQLite não vem com as verificações de Foreign Keys ativadas por padrão...
        return conn

    @classmethod
    @abstractmethod
    def add(cls, obj: Any) -> None: pass

    @classmethod
    @abstractmethod
    def get_all(cls) -> list[Any]: pass

    @classmethod
    @abstractmethod
    def update(cls, new_obj: Any) -> None: pass

    @classmethod
    @abstractmethod
    def delete(cls, searched_obj: Any) -> None: pass

    @classmethod
    def init_db(cls) -> None:
        """Inicializa o Banco de Dados do sistema."""
        conn = cls._get_db_connection()
        cursor = conn.cursor()
        
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            matricula TEXT PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS restricoes_alimentares (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno_restricao (
            aluno_matricula TEXT NOT NULL,
            restricao_id INTEGER NOT NULL,
            FOREIGN KEY (aluno_matricula)
                REFERENCES alunos (matricula)
                ON DELETE CASCADE,
            FOREIGN KEY (restricao_id)
                REFERENCES restricoes_alimentares (id)
                ON DELETE CASCADE,
            PRIMARY KEY (aluno_matricula, restricao_id)
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coordenadores (
            matricula TEXT PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS refeicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS refeicao_restricao_alimentar (
            refeicao_id INTEGER NOT NULL,
            restricao_id INTEGER NOT NULL,
            FOREIGN KEY (refeicao_id)
                REFERENCES refeicoes (id)
                ON DELETE CASCADE,
            FOREIGN KEY (restricao_id)
                REFERENCES restricoes_alimentares (id)
                ON DELETE CASCADE,
            PRIMARY KEY (refeicao_id, restricao_id)
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cardapios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_inicial TEXT NOT NULL,
            data_final TEXT NOT NULL
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vincula_cardapio_refeicao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cardapio_id INTEGER NOT NULL,
            refeicao_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            tipo TEXT NOT NULL,
            FOREIGN KEY (cardapio_id)
                REFERENCES cardapios (id)
                ON DELETE CASCADE,
            FOREIGN KEY (refeicao_id)
                REFERENCES refeicoes (id)
                ON DELETE CASCADE
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno_falta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_matricula TEXT NOT NULL,
            cardapio_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            tipo TEXT NOT NULL,
            FOREIGN KEY (aluno_matricula)
                REFERENCES alunos (matricula)
                ON DELETE CASCADE,
            FOREIGN KEY (cardapio_id)
                REFERENCES cardapios (id)
                ON DELETE CASCADE
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS justificativas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_falta_id INTEGER NOT NULL,
            motivo TEXT NOT NULL,
            FOREIGN KEY (aluno_falta_id)
                REFERENCES aluno_falta (id)
                ON DELETE CASCADE
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS analise_justificativa (
            justificativa_id INTEGER PRIMARY KEY,
            aprovacao INTEGER NOT NULL,
            coordenador_matricula TEXT NOT NULL,
            FOREIGN KEY (justificativa_id)
                REFERENCES justificativas (id)
                ON DELETE CASCADE,
            FOREIGN KEY (coordenador_matricula)
                REFERENCES coordenadores (matricula)
                ON DELETE CASCADE
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nota REAL NOT NULL,
            aluno_matricula TEXT NOT NULL,
            refeicao_id INTEGER NOT NULL,
            conteudo TEXT,
            titulo TEXT,
            FOREIGN KEY (aluno_matricula)
                REFERENCES alunos (matricula)
                ON DELETE CASCADE,
            FOREIGN KEY (refeicao_id)
                REFERENCES refeicoes (id)
                ON DELETE CASCADE
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notificacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notificacao_aluno (
            notificacao_id INTEGER NOT NULL,
            aluno_matricula TEXT NOT NULL,
            FOREIGN KEY (notificacao_id)
                REFERENCES notificacoes (id)
                ON DELETE CASCADE,
            FOREIGN KEY (aluno_matricula)
                REFERENCES alunos (matricula)
                ON DELETE CASCADE,
            PRIMARY KEY (notificacao_id, aluno_matricula)
        );""")
        
        conn.commit()
        conn.close()

if __name__ == "__main__":
    AbstractDAO.init_db()
