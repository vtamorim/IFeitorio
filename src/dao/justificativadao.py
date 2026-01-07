from dao import AbstractDAO, FaltaDAO
from models import Justificativa

class JustificativaDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Justificativa) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO justificativas (aluno_falta_id, motivo) VALUES (?, ?)"
        cursor.execute(sql_code, (obj.get_falta().get_id(), obj.get_motivo()))

        if obj.get_aprovada() is not None:
            sql_code = "INSERT INTO analise_justificativa (justificativa_id, aprovacao) VALUES (?, ?)"
            aprovacao_text = 1 if obj.get_aprovada() else 0 # SQLite não tem booleano, então representaremos como "0" e "1"
            cursor.execute(sql_code, (obj.get_id(), aprovacao_text))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Justificativa]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                j.id, j.aluno_falta_id, j.motivo,
                aj.aprovacao
            FROM
                justificativas j
            LEFT JOIN analise_justificativa aj ON aj.justificativa_id = j.id
            ORDER BY j.id
        """
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Justificativa(
                row["id"], 
                FaltaDAO.get(row["aluno_falta_id"]), 
                row["motivo"], 
                row["aprovacao"] == 1 if row["aprovacao"] is not None else None,
            )
            for row in rows
        ]

    @classmethod
    def get(cls, id: int) -> Justificativa:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                j.id, j.aluno_falta_id, j.motivo,
                aj.aprovacao
            FROM
                justificativas j
            LEFT JOIN analise_justificativa aj ON aj.justificativa_id = j.id
            WHERE j.id = ?
        """
        cursor.execute(sql_code, (id,))

        row = cursor.fetchone()
        conn.close()

        return Justificativa(row["id"], FaltaDAO.get(row["aluno_falta_id"]), row["motivo"], row["aprovacao"] == 1)

    @classmethod
    def update(cls, new_obj: Justificativa) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE justificativas SET aluno_falta_id = ?, motivo = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_falta().get_id(), new_obj.get_motivo(), new_obj.get_id()))

        if new_obj.get_aprovada() is None: # Tirar a análise dessa justificativa se ela não tiver análise
            sql_code = "DELETE FROM analise_justificativa WHERE justificativa_id = ?"
            cursor.execute(sql_code, (new_obj.get_id(),))
        else: # Atualizar a análise dessa justificativa se ela tiver análise
            sql_code = """
                INSERT INTO analise_justificativa (justificativa_id, aprovacao) 
                VALUES (?, ?)
                ON CONFLICT (justificativa_id) DO
                UPDATE
                SET 
                    aprovacao = excluded.aprovacao
            """
            aprovacao_text = 1 if new_obj.get_aprovada() else 0 # SQLite não tem booleano, então representaremos como "0" e "1"
            cursor.execute(sql_code, (new_obj.get_id(), aprovacao_text))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM justificativas WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
