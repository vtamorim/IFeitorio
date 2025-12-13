from dao import AbstractDAO
from models import Aluno, Restricao

class AlunoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Aluno) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO alunos (matricula, nome, senha) VALUES (?, ?, ?)"
        cursor.execute(sql_code, (obj.get_matricula(), obj.get_nome(), obj.get_senha()))

        sql_code = "INSERT INTO aluno_restricao (aluno_matricula, restricao_id) VALUES (?, ?)"
        cursor.executemany(sql_code, [ (obj.get_matricula(), rest.get_id()) for rest in obj.get_restricoes() ])
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Aluno]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                a.matricula, a.nome, a.senha,
                r.id AS ra_id, r.nome AS ra_nome
            FROM
                alunos a
            LEFT JOIN aluno_restricao ar ON a.matricula = ar.aluno_matricula
            LEFT JOIN restricoes_alimentares r ON ar.restricao_id = r.id
            ORDER BY a.matricula
        """
        cursor.execute(sql_code)
        rows = cursor.fetchall()

        conn.close()

        alunos_restricoes: dict[str, list[Restricao]] = {}

        for row in rows: # Cria os objetos "Restricao" do Banco de Dados
            if row["ra_id"] is not None:
                if alunos_restricoes.get(row["matricula"]) is None:
                    alunos_restricoes[row["matricula"]] = []

                alunos_restricoes[row["matricula"]].append(Restricao(row["ra_id"], row["ra_nome"]))

        return [
            Aluno(row["matricula"], row["nome"], row["senha"], alunos_restricoes.get(row["matricula"], []))
            for row in rows
        ]

    @classmethod
    def get(cls, matricula: str) -> Aluno:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                a.matricula, a.nome, a.senha,
                r.id AS ra_id, r.nome AS ra_nome
            FROM
                alunos a
            LEFT JOIN aluno_restricao ar ON a.matricula = ar.aluno_matricula
            LEFT JOIN restricoes_alimentares r ON ar.restricao_id = r.id
            WHERE a.matricula = ?
        """
        cursor.execute(sql_code, (matricula,))
        rows = cursor.fetchall()

        conn.close()

        restricoes: list[Restricao] = []

        for row in rows: # Cria os objetos "Restricao" do Banco de Dados
            if row["ra_id"] is not None:
                restricoes.append(Restricao(row["ra_id"], row["ra_nome"]))
            
        return Aluno(rows[0]["matricula"], rows[0]["nome"], rows[0]["senha"], restricoes)

    @classmethod
    def update(cls, new_obj: Aluno) -> None:
        id_restricoes = set([ restricao.get_id() for restricao in new_obj.get_restricoes() ])
        
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE alunos SET nome = ?, senha = ? WHERE matricula = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_senha(), new_obj.get_matricula()))

        sql_code = "DELETE FROM aluno_restricao WHERE aluno_matricula = ? AND restricao_id NOT IN ?"
        cursor.execute(sql_code, (new_obj.get_matricula(), tuple(id_restricoes)))

        sql_code = "INSERT INTO aluno_restricao VALUES (?, ?) ON CONFLICT (aluno_matricula, restricao_id) DO NOTHING"
        cursor.executemany(sql_code, [ (new_obj.get_matricula(), id_rest) for id_rest in id_restricoes ])

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: str) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM alunos WHERE matricula = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
