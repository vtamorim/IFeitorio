from dao import AbstractDAO
from models import Restricao

class RestricaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Restricao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO restricoes_alimentares (id, nome) VALUES (?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_nome()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Restricao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM restricoes_alimentares"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Restricao(row["id"], row["nome"])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Restricao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE restricoes_alimentares SET nome = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_id()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM restricoes_alimentares WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
