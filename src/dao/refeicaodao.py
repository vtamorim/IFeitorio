from dao import AbstractDAO
from models import Refeicao, Restricao

class RefeicaoDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Refeicao) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO refeicao (id, nome, descricao, tipo) VALUES (?, ?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_nome(), obj.get_descricao(), obj.get_tipo()))

        if len(obj.get_restricoes_compativeis()) > 0: # Adiciona as relações entre refeição e restrições
            values_str = ", ".join(["(?, ?)" for _ in range(len(obj.get_restricoes_compativeis()))])
            values_parameter = []
            for rest in obj.get_restricoes_compativeis():
                values_parameter.append(obj.get_id())
                values_parameter.append(rest.get_id())
            sql_code = f"INSERT INTO refeicao_restricao_alimentar (refeicao_id, restricao_id) VALUES {values_str}"
            cursor.execute(sql_code, values_parameter)
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Refeicao]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT 
                r.id, r.nome, r.descricao, r.tipo,
                ra.id AS ra_id, ra.nome AS ra_nome
            FROM
                refeicao r
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
            Refeicao(row.id, row.nome, row.descricao, row.tipo, row.get(row.id, []))
            for row in rows
        ]

    @classmethod
    def get(cls, id: int) -> Refeicao:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT 
                r.id, r.nome, r.descricao, r.tipo,
                ra.id AS ra_id, ra.nome AS ra_nome
            FROM
                refeicao r
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
        
        return Refeicao(rows[0].id, rows[0].nome, rows[0].descricao, rows[0].tipo, refeicao_restricoes)

    @classmethod
    def update(cls, new_obj: Refeicao) -> None:
        id_restricoes = set([ restricao.get_id() for restricao in new_obj.get_restricoes_compativeis() ])
        
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE refeicao SET nome = ?, descricao = ?, tipo = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_nome(), new_obj.get_descricao(), new_obj.get_tipo(), new_obj.get_id()))

        sql_code = "SELECT restricao_id FROM refeicao_restricao_alimentar WHERE refeicao_id = ?"
        cursor.execute(sql_code, (new_obj.get_id(),))
        restricoes_antigas = set([row.restricao_id for row in cursor.fetchall()])

        restricoes_novas = id_restricoes - restricoes_antigas # Adiciona as restrições novas adicionadas a refeição
        amount_values = ", ".join([ "(?, ?)" for _ in range(len(restricoes_novas)) ])
        sql_code = f"INSERT INTO refeicao_restricao_alimentar (refeicao_id, restricao_id) VALUES {amount_values}"
        values = [ ]
        for i in restricoes_novas:
            values.append(new_obj.get_id())
            values.append(i)
        cursor.execute(sql_code, tuple(values))

        restricoes_removidas = restricoes_antigas - id_restricoes # Remove as restrições antigas que foram removidas da refeição
        sql_code = "DELETE FROM refeicao_restricao_alimentar WHERE refeicao_id = ? AND restricao_id IN ?"
        values = [ new_obj.get_id(), tuple(restricoes_removidas) ]
        cursor.execute(sql_code, tuple(values))

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM refeicao WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
