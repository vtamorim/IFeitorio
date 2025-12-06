from dao import AbstractDAO
from models import Restricao

class RestricaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Restricao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO restricao (aluno_matricula, nome) VALUES (?, ?)"
        cursor.execute(sql_code, (obj.get_aluno_matricula(), obj.get_nome()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Restricao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM restricao"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Restricao(row["aluno_matricula"], row["nome"])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Restricao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE restricao SET nome = ? WHERE aluno_matricula = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_aluno_matricula()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: str) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM restricao WHERE aluno_matricula = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()

    @classmethod
    def get_aluno_matricula(cls, searched_aluno_matricula: str) -> Restricao:
        """Retorna a Restrição Alimentar de um determinado aluno pela sua matrícula."""
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM restricao WHERE aluno_matricula = ?"
        cursor.execute(sql_code, (searched_aluno_matricula,))

        row = cursor.fetchone()
        conn.close()

        return Restricao(row["aluno_matricula"], row["nome"])
