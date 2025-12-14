from dao import AbstractDAO
from models import Coordenador

class CoordenadorDAO(AbstractDAO):
    @classmethod
    def add(cls, obj : Coordenador) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO coordenadores (matricula, nome, senha) VALUES (?, ?, ?)"
        cursor.execute(sql_code, (obj.get_matricula(), obj.get_nome(), obj.get_senha()))
        
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
            Coordenador(row["matricula"], row["nome"], row["senha"])
            for row in rows
        ]

    @classmethod
    def get(cls, matricula: str) -> Coordenador:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM coordenadores WHERE matricula = ?"
        cursor.execute(sql_code, (matricula,))

        row = cursor.fetchone()
        conn.close()

        return Coordenador(row["matricula"], row["nome"], row["senha"])

    @classmethod
    def update(cls, new_obj: Coordenador) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE coordenadores SET nome = ?, senha = ? WHERE matricula = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_senha(), new_obj.get_matricula()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: str) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM coordenadores WHERE matricula = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
