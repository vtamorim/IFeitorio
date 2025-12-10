from dao import AbstractDAO
from models import Aluno, Restricao

class AlunoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Aluno) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO alunos (id, matricula, nome, senha) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_matricula(), obj.get_nome(), obj.get_senha()))

        sql_code = "INSERT INTO aluno_restricao (aluno_id, restricao_id) VALUES (?, ?)"
        for aluno_restricao in obj.get_restricoes():
            cursor.execute(sql_code, (obj.get_id(), aluno_restricao.get_id()))
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Aluno]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                a.id, a.matricula, a.nome, a.senha,
                r.id AS ra_id, r.nome AS ra_nome
            FROM
                alunos a
            LEFT JOIN aluno_restricao ar ON a.id = ar.aluno_id
            LEFT JOIN restricoes_alimentares r ON ar.restricao_id = r.id
            ORDER BY a.id
        """
        cursor.execute(sql_code)
        rows = cursor.fetchall()

        conn.close()

        alunos_restricoes: dict[int, list[Restricao]] = {}

        for row in rows: # Cria os objetos "Restricao" do Banco de Dados
            if row.ra_id is not None:
                if alunos_restricoes.get(row.id) is None:
                    alunos_restricoes[row.id] = []

                alunos_restricoes[row.id].append(Restricao(row.ra_id, row.ra_nome))

        return [
            Aluno(row.id, row.matricula, row.nome, row.senha, alunos_restricoes.get(row.id, []))
            for row in rows
        ]

    @classmethod
    def get(cls, id: int) -> Aluno:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                a.id, a.matricula, a.nome, a.senha,
                r.id AS ra_id, r.nome AS ra_nome
            FROM
                alunos a
            LEFT JOIN aluno_restricao ar ON a.id = ar.aluno_id
            LEFT JOIN restricoes_alimentares r ON ar.restricao_id = r.id
            WHERE a.id = ?
        """
        cursor.execute(sql_code, (id,))
        rows = cursor.fetchall()

        conn.close()

        restricoes: list[Restricao] = []

        for row in rows: # Cria os objetos "Restricao" do Banco de Dados
            if row.ra_id is not None:
                restricoes.append(Restricao(row.ra_id, row.ra_nome))
            
        return Aluno(rows[0].id, rows[0].matricula, rows[0].nome, rows[0].senha, restricoes)

    @classmethod
    def update(cls, new_obj: Aluno) -> None:
        id_restricoes = set([ restricao.get_id() for restricao in new_obj.get_restricoes() ])
        
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE aluno SET matricula = ?, nome = ?, senha = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_matricula(), new_obj.get_nome(), new_obj.get_senha(), new_obj.get_id()))

        sql_code = "SELECT restricao_id FROM aluno_restricao WHERE aluno_id = ?"
        cursor.execute(sql_code, (new_obj.get_id(),))
        restricoes_antigas = set([row.restricao_id for row in cursor.fetchall()])

        restricoes_novas = id_restricoes - restricoes_antigas # Adiciona as restrições novas adicionadas ao aluno
        amount_values = ", ".join([ "(?, ?)" for _ in range(len(restricoes_novas)) ])
        sql_code = f"INSERT INTO aluno_restricao (aluno_id, restricao_id) VALUES {amount_values}"
        values = [ ]
        for i in restricoes_novas:
            values.append(new_obj.get_id())
            values.append(i)
        cursor.execute(sql_code, tuple(values))

        restricoes_removidas = restricoes_antigas - id_restricoes # Remove as restrições antigas que foram removidas do aluno
        sql_code = "DELETE FROM aluno_restricao WHERE aluno_id = ? AND restricao_id IN ?"
        values = [ new_obj.get_id(), tuple(restricoes_removidas) ]
        cursor.execute(sql_code, tuple(values))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM alunos WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
