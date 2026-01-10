from dao import AbstractDAO, AlunoDAO, CardapioDAO
from models import Falta

class FaltaDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Falta) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO aluno_falta (aluno_matricula, cardapio_id, data, tipo) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_aluno().get_matricula(), obj.get_cardapio().get_id(), obj.get_data_formatada(), obj.get_tipo()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Falta]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM aluno_falta"
        cursor.execute(sql_code)
        rows = cursor.fetchall()
        
        conn.close()

        return [
            Falta(row["id"], AlunoDAO.get(row["aluno_matricula"]), CardapioDAO.get(row["cardapio_id"]), row["data"], row["tipo"])
            for row in rows
        ]

    @classmethod
    def get(cls, id: int) -> Falta:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM aluno_falta WHERE id = ?"
        cursor.execute(sql_code, (id,))
        row = cursor.fetchone()
        
        conn.close()

        return Falta(row["id"], AlunoDAO.get(row["aluno_matricula"]), CardapioDAO.get(row["cardapio_id"]), row["data"], row["tipo"])
    
    @classmethod
    def get_sem_justificativas(cls, aluno_matricula: str) -> list[Falta]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT a.id, a.aluno_matricula, a.cardapio_id, a.data, a.tipo 
            FROM aluno_falta a 
            LEFT JOIN justificativas j ON a.id = j.aluno_falta_id
            WHERE j.id IS NULL AND a.aluno_matricula = ?
        """
        cursor.execute(sql_code, (aluno_matricula,))
        rows = cursor.fetchall()
        
        conn.close()

        return [
            Falta(row["id"], AlunoDAO.get(row["aluno_matricula"]), CardapioDAO.get(row["cardapio_id"]), row["data"], row["tipo"])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Falta) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE aluno_falta SET aluno_matricula = ?, cardapio_id = ?, data = ?, tipo = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_aluno().get_matricula(), new_obj.get_cardapio().get_id(), new_obj.get_data_formatada(), new_obj.get_tipo(), new_obj.get_id()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM aluno_falta WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
