from dao import AbstractDAO, AlunoDAO
from models import Notificacao, Aluno

class NotificacaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Notificacao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO notificacoes (titulo, conteudo) VALUES (?, ?) RETURNING id"
        cursor.execute(sql_code, (obj.get_titulo(), obj.get_conteudo()))

        notificacao_id = cursor.fetchone().id

        sql_code = "INSERT INTO notificacao_aluno (notificacao_id, aluno_matricula) VALUES (?, ?)"
        cursor.executemany(sql_code, [ (notificacao_id, aluno.get_matricula()) for aluno in obj.get_alunos_destinatarios() ])
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Notificacao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                n.id, n.titulo, n.conteudo
                na.aluno_matricula
            FROM
                notificacoes n
            LEFT JOIN notificacao_aluno na ON na.notificacao_id = n.id
            ORDER BY n.id
        """
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        notificacoes_alunos: dict[int, list[Aluno]] = {}
        for row in rows:
            if row.aluno_id is not None:
                if notificacoes_alunos.get(row.id) is None:
                    notificacoes_alunos[row.id] = []
                
                notificacoes_alunos[row.id].append(AlunoDAO.get(row.aluno_id))

        return [
            Notificacao(row.id, row.titulo, row.conteudo, notificacoes_alunos[row.aluno_id])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Notificacao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE notificacoes SET titulo = ?, conteudo = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_titulo(), new_obj.get_conteudo(), new_obj.get_id()))

        sql_code = "DELETE FROM notificacao_aluno WHERE notificacao_id = ? AND aluno_matricula NOT IN ?"
        cursor.execute(sql_code, (new_obj.get_id(), [ aluno.get_matricula() for aluno in new_obj.get_alunos_destinatarios() ]))

        sql_code = "INSERT INTO notificacao_aluno (notificacao_id, aluno_matricula) VALUES (?) ON CONFLICT (notificacao_id, aluno_matricula) DO NOTHING" # Adiciona as novas relações de notificação-aluno_destinatário, ignora caso já esteja no banco de dados.
        cursor.executemany(sql_code, [ (new_obj.get_id(), aluno.get_matricula()) for aluno in new_obj.get_alunos_destinatarios() ])

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM notificacoes WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
