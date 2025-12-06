from dao import AbstractDAO
from models import Cardapio
from datetime import datetime
# É necessário ver como será armazenado os "datetime", pois eles devem ser convertidos para uma string (usar o strptime e strftime de forma consistente).
class CardapioDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Cardapio) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO cardapio (data_inicial, data_final) VALUES (?, ?)"
        cursor.execute(sql_code, (obj.get_di(), obj.get_df()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Cardapio]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM cardapio"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Cardapio(i, rows[i]["data_inicial"], rows[i]["data_final"])
            for i in range(len(rows))
        ]

    @classmethod
    def update(cls, new_obj: Cardapio) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE cardapio SET data_final = ? WHERE data_inicial = ?" # Melhorar isso depois...
        cursor.execute(sql_code, (new_obj.get_df(), new_obj.get_di()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: datetime) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM cardapio WHERE data_inicial = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
