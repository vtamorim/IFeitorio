from dao import AbstractDAO
from models import Refeicao

class RefeicaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Refeicao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO refeicao (id, nome, descricao, tipo, data) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_nome(), obj.get_descricao(), obj.get_tipo(), obj.get_data()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Refeicao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM refeicao"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Refeicao(row["id"], row["nome"], row["descricao"], row["tipo"], row["data"])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Refeicao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE refeicao SET nome = ?, descricao = ?, tipo = ?, data = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_descricao(), new_obj.get_tipo(), new_obj.get_data(), new_obj.get_id()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM refeicao WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
