from dao import AbstractDAO, RefeicaoDAO
from models import Cardapio, Refeicao

class CardapioDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Cardapio) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO cardapios (data_inicial, data_final) VALUES (?, ?) RETURNING id"
        cursor.execute(sql_code, (obj.get_data_formatada(obj.get_data_inicial()), obj.get_data_formatada(obj.get_data_final())))

        cardapio_id = cursor.fetchone()["id"] # Pega o id do novo cardápio gerado pelo Banco de Dados

        sql_code = "INSERT INTO vincula_cardapio_refeicao (cardapio_id, refeicao_id, data, tipo) VALUES (?, ?, ?, ?)"
        cursor.executemany(sql_code, [ (cardapio_id, ref.get_id(), ref.get_data_formatada(), ref.get_tipo()) for ref in obj.get_refeicoes() ])
        
        conn.commit()
        conn.close()
    
    @classmethod
    def get_all(cls) -> list[Cardapio]:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                c.id, c.data_inicial, c.data_final,
                vcr.refeicao_id, vcr.data, vcr.tipo
            FROM
                cardapios c
            LEFT JOIN vincula_cardapio_refeicao vcr ON vcr.cardapio_id = c.id
            ORDER BY c.id
        """
        cursor.execute(sql_code)

        rows = cursor.fetchall()
        conn.close()

        refeicoes = RefeicaoDAO.get_all()
        cardapios: dict[int, Cardapio] = {}
        for row in rows:
            if row["id"] not in cardapios:
                cardapios[row["id"]] = Cardapio(row["id"], row["data_inicial"], row["data_final"])

            if row["refeicao_id"] is not None:
                refeicao_atual = next((ref for ref in refeicoes if ref.get_id() == row["refeicao_id"]))
                refeicao = Refeicao( # Cria um novo objeto em Refeicao para evitar compartilhamento de identidade (bug díficil de notar)
                    refeicao_atual.get_id(), 
                    refeicao_atual.get_nome(), 
                    refeicao_atual.get_descricao(), 
                    refeicao_atual.get_restricoes_compativeis(), 
                    row["data"], 
                    row["tipo"]
                )
                cardapios[row["id"]].add_refeicao(refeicao)
        
        return list(cardapios.values())
    
    @classmethod
    def get(cls, id: int) -> Cardapio:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = """
            SELECT
                c.id, c.data_inicial, c.data_final,
                vcr.refeicao_id, vcr.data, vcr.tipo
            FROM
                cardapios c
            LEFT JOIN vincula_cardapio_refeicao vcr ON vcr.cardapio_id = c.id
            WHERE c.id = ?
        """
        cursor.execute(sql_code, (id,))

        rows = cursor.fetchall()
        conn.close()

        refeicoes = RefeicaoDAO.get_all()
        cardapio = Cardapio(rows[0]["id"], rows[0]["data_inicial"], rows[0]["data_final"])
        for row in rows:
            if row["refeicao_id"] is not None:
                refeicao_atual = next((ref for ref in refeicoes if ref.get_id() == row["refeicao_id"]))
                refeicao = Refeicao( # Cria um novo objeto em Refeicao para evitar compartilhamento de identidade (bug díficil de notar)
                    refeicao_atual.get_id(), 
                    refeicao_atual.get_nome(), 
                    refeicao_atual.get_descricao(), 
                    refeicao_atual.get_restricoes_compativeis(), 
                    row["data"], 
                    row["tipo"]
                )
                cardapio.add_refeicao(refeicao)
        
        return cardapio

    @classmethod
    def update(cls, new_obj: Cardapio) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE cardapios SET data_inicial = ?, data_final = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_data_formatada(new_obj.get_data_inicial()), new_obj.get_data_formatada(new_obj.get_data_final()), new_obj.get_id()))

        sql_code = "DELETE FROM vincula_cardapio_refeicao WHERE cardapio_id = ?" # Limpa completamente a tabela de vínculos daquele cardapio.
        cursor.execute(sql_code, (new_obj.get_id(),))

        sql_code = "INSERT INTO vincula_cardapio_refeicao (cardapio_id, refeicao_id, data, tipo) VALUES (?, ?, ?, ?)"
        cursor.executemany(sql_code, [ (new_obj.get_id(), ref.get_id(), ref.get_data_formatada(), ref.get_tipo()) for ref in new_obj.get_refeicoes() ])

        conn.commit()
        conn.close()
    
    @classmethod
    def delete(cls, searched_obj: int) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "DELETE FROM cardapios WHERE id = ?"
        cursor.execute(sql_code, (searched_obj,))

        conn.commit()
        conn.close()
