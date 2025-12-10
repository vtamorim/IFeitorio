from dao import AbstractDAO, AlunoDAO, CardapioDAO, RefeicaoDAO
from models import Falta

class FaltaDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Falta) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT id FROM vincula_cardapio_refeicao WHERE cardapio_id = ? AND refeicao_id = ? AND data = ?"
        cursor.execute(sql_code, (obj.get_cardapio().get_id(), obj.get_refeicao().get_id(), obj.get_refeicao().get_data_formatada()))
        vcr_id = cursor.fetchone().id
        
        sql_code = "INSERT INTO aluno_falta (id, aluno_id, vincula_cardapio_refeicao_id) VALUES (?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_aluno().get_id(), vcr_id))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Falta]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                af.id, af.aluno_id,
                vcr.cardapio_id, vcr.refeicao_id, vcr.data
            FROM
                aluno_falta af
            LEFT JOIN vincula_cardapio_refeicao vcr ON vcr.id = af.vincula_cardapio_refeicao_id
            ORDER BY af.id
        """
        cursor.execute(sql_code)
        rows = cursor.fetchall()
        
        conn.close()

        refeicoes = { row.refeicao_id : RefeicaoDAO.get(row.refeicao_id) for row in rows }
        for row in rows:
            refeicoes[row.refeicao_id].set_data(row.data)

        return [
            Falta(row.id, AlunoDAO.get(row.aluno_id), CardapioDAO.get(row.cardapio_id), refeicoes[row.refeicao_id])
            for row in rows
        ]

    @classmethod
    def get(cls, id: int) -> Falta:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                af.id, af.aluno_id,
                vcr.cardapio_id, vcr.refeicao_id, vcr.data
            FROM
                aluno_falta af
            LEFT JOIN vincula_cardapio_refeicao vcr ON vcr.id = af.vincula_cardapio_refeicao_id
            WHERE af.id = ?
        """
        cursor.execute(sql_code, (id,))
        row = cursor.fetchone()
        
        conn.close()

        refeicao = RefeicaoDAO.get(row.refeicao_id)
        refeicao.set_data(row.data)

        return Falta(row.id, AlunoDAO.get(row.aluno_id), CardapioDAO.get(row.cardapio_id), refeicao)

    @classmethod
    def update(cls, new_obj: Falta) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT id FROM vincula_cardapio_refeicao WHERE cardapio_id = ? AND refeicao_id = ? AND data = ?"
        cursor.execute(sql_code, (new_obj.get_cardapio().get_id(), new_obj.get_refeicao().get_id(), new_obj.get_refeicao().get_data_formatada()))
        vcr_id = cursor.fetchone().id

        sql_code = "UPDATE aluno_falta SET aluno_id = ?, vincula_cardapio_refeicao_id = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_aluno().get_id(), vcr_id, new_obj.get_id()))
        
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
