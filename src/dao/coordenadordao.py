from dao import AbstractDAO
from models import Coordenador

class CoordenadorDAO(AbstractDAO):
    @classmethod
    def add(cls, obj : Coordenador) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO coordenadores (id, matricula, nome, senha) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_matricula(), obj.get_nome(), obj.get_senha()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Coordenador]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM coordenadores"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Coordenador(row.id, row.matricula, row.nome, row.senha)
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Coordenador) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE coordenadores SET matricula = ?, nome = ?, senha = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_matricula(), new_obj.get_nome(), new_obj.get_senha(), new_obj.get_id()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM coordenadores WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
