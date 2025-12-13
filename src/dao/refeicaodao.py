from dao import AbstractDAO
from models import Refeicao, Restricao

class RefeicaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Refeicao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO refeicoes (nome, descricao) VALUES (?, ?) RETURNING id"
        cursor.execute(sql_code, (obj.get_nome(), obj.get_descricao()))

        refeicao_id = cursor.fetchone().id

        sql_code = "INSERT INTO refeicao_restricao_alimentar (refeicao_id, restricao_id) VALUES (?, ?)"
        cursor.executemany(sql_code, [ (refeicao_id, rest.get_id()) for rest in obj.get_restricoes_compativeis() ])
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Refeicao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT 
                r.id, r.nome, r.descricao,
                ra.id AS ra_id, ra.nome AS ra_nome
            FROM
                refeicoes r
            LEFT JOIN refeicao_restricao_alimentar rra ON rra.refeicao_id = r.id
            LEFT JOIN restricoes_alimentares ra ON ra.id = rra.restricao_id
            ORDER BY r.id
        """
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        refeicao_restricoes: dict[int, list[Restricao]] = {}

        for row in rows: # Cria os objetos "Restricao" do Banco de Dados
            if row.ra_id is not None:
                if refeicao_restricoes.get(row.id) is None:
                    refeicao_restricoes[row.id] = []

                refeicao_restricoes[row.id].append(Restricao(row.ra_id, row.ra_nome))

        return [
            Refeicao(row.id, row.nome, row.descricao, refeicao_restricoes.get(row.id, []))
            for row in rows
        ]

    @classmethod
    def get(cls, id: int) -> Refeicao:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT 
                r.id, r.nome, r.descricao,
                ra.id AS ra_id, ra.nome AS ra_nome
            FROM
                refeicoes r
            LEFT JOIN refeicao_restricao_alimentar rra ON rra.refeicao_id = r.id
            LEFT JOIN restricoes_alimentares ra ON ra.id = rra.restricao_id
            WHERE r.id = ?
        """
        cursor.execute(sql_code, (id,))

        rows = cursor.fetchall()
        conn.close()

        refeicao_restricoes: list[Restricao] = []

        for row in rows: # Cria os objetos "Restricao" do Banco de Dados
            if row.ra_id is not None:
                refeicao_restricoes.append(Restricao(row.ra_id, row.ra_nome))
        
        return Refeicao(rows[0].id, rows[0].nome, rows[0].descricao, refeicao_restricoes)

    @classmethod
    def update(cls, new_obj: Refeicao) -> None:
        id_restricoes = set([ restricao.get_id() for restricao in new_obj.get_restricoes_compativeis() ])
        
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE refeicoes SET nome = ?, descricao = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_descricao(), new_obj.get_id()))

        sql_code = "DELETE FROM refeicao_restricao_alimentar WHERE refeicao_id = ? AND restricao_id NOT IN ?"
        cursor.execute(sql_code, (new_obj.get_id(), tuple(id_restricoes)))

        sql_code = """
            INSERT INTO refeicao_restricao_alimentar (refeicao_id, restricao_id) 
            VALUES (?, ?)
            ON CONFLICT (refeicao_id, restricao_id) DO NOTHING
        """
        cursor.executemany(sql_code, [ (new_obj.get_id(), rest) for rest in id_restricoes ])

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM refeicoes WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
