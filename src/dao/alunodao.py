from dao import AbstractDAO
from .restricaodao import RestricaoDAO
from models import Aluno

class AlunoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Aluno) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO aluno (matricula, nome, senha) VALUES (?, ?, ?)"
        cursor.execute(sql_code, (obj.get_matricula(), obj.get_nome(), obj.get_senha()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Aluno]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM aluno"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Aluno(i, rows[i]["matricula"], rows[i]["nome"], rows[i]["senha"], [ RestricaoDAO.get_aluno_matricula(rows[i]["matricula"]) ]) # Acho que dá pra melhorar esse código depois...
            for i in range(len(rows))
        ]

    @classmethod
    def update(cls, new_obj: Aluno) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE aluno SET nome = ?, senha = ? WHERE matricula = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_senha(), new_obj.get_matricula())) # Ver depois sobre como modificar as restrições. Sugiro criar uma tabela intermediária.

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: str) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM aluno WHERE matricula = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
