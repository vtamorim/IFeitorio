from dao import AbstractDAO
from models import Justificativa

class JustificativaDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Justificativa) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO justificativa (id, data, motivo, aluno_matricula, refeicao_id) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_data(), obj.get_motivo(), obj.get_alu_mat(), obj.get_ref_id()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Justificativa]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM justificativa"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Justificativa(row["id"], row["data"], row["motivo"], row["aluno_matricula"], row["refeicao_id"])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Justificativa) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE justificativa SET data = ?, motivo = ?, aluno_matricula = ?, refeicao_id = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_data(), new_obj.get_motivo(), new_obj.get_alu_mat(), new_obj.get_ref_id(), new_obj.get_id()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM justificativa WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
