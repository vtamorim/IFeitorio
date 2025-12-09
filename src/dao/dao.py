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
    def delete(cls, searched_obj: Any) -> None: pass # Não sei qual poderia ser o tipo desse "searched_obj", pois nem todas as tabelas tem um id.

    # @classmethod
    # @abstractmethod
    # def get_id(cls, searched_obj: Any) -> Any: pass # Não sei qual poderia ser o tipo desse "searched_obj", pois nem todas as tabelas tem um id.
    # Não sei se deveríamos ter um "get_id" aqui, pois nem todas as classes tem "id",

    # Talvez um método para inicializar o banco de dados?
