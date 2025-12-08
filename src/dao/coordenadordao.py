from dao import AbstractDAO
from models import Coordenador
from datetime import datetime

class CoordenadorDAO(AbstractDAO):
    @classmethod
    def add(cls, obj : Coordenador) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO cardapio (id, mat, n, s) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_di(), obj.get_df()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Coordenador]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM Cordenador"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Coordenador(i, rows[i]["id"], rows[i]["mat"], rows[i]["n"], rows[i]["s"])
            for i in range(len(rows))
        ]

    @classmethod
    def update(cls, new_obj: Coordenador) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code =  "UPDATE coordenador SET mat = ?, n = ?, s = ? WHERE id = ?" # Melhorar isso depois...
        cursor.execute(sql_code, (new_obj.get_df(), new_obj.get_di()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: datetime) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM coordenador WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
