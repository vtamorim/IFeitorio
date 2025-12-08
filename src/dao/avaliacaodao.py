from dao import AbstractDAO
from models import Refeicao
from datetime import datetime
class AvaliacaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj : Refeicao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO cardapio (id, nota, conteudo, titulo, ref_id) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_di(), obj.get_df()))
        
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
            Refeicao(i, rows[i]["id"], rows[i]["nota"], rows[i]["conteudo"], rows[i]["titulo"], rows[i]["ref_id"])
            for i in range(len(rows))
        ]

    @classmethod
    def update(cls, new_obj: Refeicao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code =  "UPDATE avaliacao SET nota = ?, conteudo = ?, titulo = ?, ref_id = ? WHERE id = ?" # Melhorar isso depois...
        cursor.execute(sql_code, (new_obj.get_df(), new_obj.get_di()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: datetime) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM cardapio WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
