from dao import AbstractDAO
from models import Notificacao

class NotificacaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Notificacao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO notificacao (id, titulo, conteudo) VALUES (?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_titulo(), obj.get_conteudo()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Notificacao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM notificacao"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Notificacao(row["id"], row["titulo"], row["conteudo"])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Notificacao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE notificacao SET titulo = ?, conteudo = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_titulo(), new_obj.get_conteudo(), new_obj.get_id()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM notificacao WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
