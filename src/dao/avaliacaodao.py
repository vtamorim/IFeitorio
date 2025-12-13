from dao import AbstractDAO, AlunoDAO, RefeicaoDAO
from models import Avaliacao

class AvaliacaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Avaliacao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO avaliacoes (nota, aluno_matricula, refeicao_id, conteudo, titulo) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_nota(), obj.get_aluno().get_matricula(), obj.get_refeicao().get_id(), obj.get_conteudo(), obj.get_titulo()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Avaliacao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "SELECT * FROM avaliacoes"
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        return [
            Avaliacao(row.id, row.nota, AlunoDAO.get(row.aluno_matricula), RefeicaoDAO.get(row.refeicao_id), row.conteudo, row.titulo)
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Avaliacao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE avaliacoes SET nota = ?, aluno_matricula = ?, refeicao_id = ?, conteudo = ? titulo = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_nota(), new_obj.get_aluno().get_matricula(), new_obj.get_refeicao().get_id(), new_obj.get_conteudo(), new_obj.get_titulo(), new_obj.get_id()))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM avaliacoes WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
