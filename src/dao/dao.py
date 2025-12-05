from abc import ABC, abstractmethod
import sqlite3 # Só para ter o tipo "Connection".
from typing import Any

class AbstractDAO(ABC):
    """Classe Abstrata de todos os DAOs contendo a 'generalização' de suas funções. Ela também padronizará os DAOs para facilitar os seus usos."""
    _db_path = "../data/database.db" # Caminho do arquivo do Banco de Dados

    @classmethod
    @abstractmethod
    def _get_db_connection(cls) -> sqlite3.Connection: pass # Função que retorna o objeto da conexão com o Banco de Dados SQLite. Provavelmente será necessária.

    @classmethod
    @abstractmethod
    def add(cls, obj: Any) -> None: pass

    @classmethod
    @abstractmethod
    def get_all(cls) -> list[Any]: pass

    @classmethod
    @abstractmethod
    def get_id(cls, searched_id: int) -> Any: pass # Talvez devéssemos usar outra coisa ao invés de um "id de tipo inteiro", visto que há algumas classes que não possuem um "ID" de tipo inteiro.

    @classmethod
    @abstractmethod
    def update(cls, new_obj: Any) -> None: pass

    @classmethod
    @abstractmethod
    def delete(cls, searched_id: int) -> None: pass # Talvez devéssemos usar outra coisa ao invés de um "id de tipo inteiro", visto que há algumas classes que não possuem um "ID" de tipo inteiro.

    # Talvez um método para inicializar o banco de dados?
