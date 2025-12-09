from dao import AbstractDAO, RefeicaoDAO
from models import Cardapio, Refeicao

class CardapioDAO(AbstractDAO):
    @classmethod
    def add(cls, obj: Cardapio) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "INSERT INTO cardapios (id, data_inicial, data_final) VALUES (?, ?, ?)"
        cursor.execute(sql_code, (obj.get_id(), obj.get_data_formatada(obj.get_data_inicial()), obj.get_data_formatada(obj.get_data_final())))
        
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
        cardapios_refeicoes: dict[int, list[Refeicao]] = {} # Dicionário de "id do cardápio" para "list de suas Refeições"
        cardapios_refeicoes_id: dict[int, set[int]] = {} # Dicionário de "id do cardápio" para "conjunto de ids de suas Refeições"
        refeicoes_datatipo: dict[int, dict[str, str]] = {} # Dicionário de "id da refeição" para "data e tipo dela"
        for row in rows: # De todos os dados pegos dos cardápios, preenche os dados acima
            if row.refeicao_id is not None:
                if cardapios_refeicoes_id.get(row.id) is None:
                    cardapios_refeicoes_id[row.id] = set()

                cardapios_refeicoes_id[row.id].add(row.refeicao_id)
                refeicoes_datatipo[row.refeicao_id] = {
                    "data": row.data,
                    "tipo": row.tipo
                }
        
        for k in cardapios_refeicoes_id.keys(): # Separa os objetos "Refeição" e adiciona suas datas e tipos
            cardapios_refeicoes[k] = [ ref for ref in refeicoes if ref.get_id() in cardapios_refeicoes_id[k] ]
            for ref in cardapios_refeicoes[k]:
                ref.set_data(refeicoes_datatipo[ref.get_id()].data)
                ref.set_tipo(refeicoes_datatipo[ref.get_id()].tipo)

        return [
            Cardapio(row.id, row.data_inicial, row.data_final, cardapios_refeicoes[row.id])
            for row in rows
        ]

    @classmethod
    def update(cls, new_obj: Cardapio) -> None:
        conn = cls._get_db_connection()
        cursor = conn.cursor()

        sql_code = "UPDATE cardapios SET data_inicial = ?, data_final = ? WHERE id = ?"
        cursor.execute(sql_code, (new_obj.get_data_formatada(new_obj.get_data_inicial()), new_obj.get_data_formatada(new_obj.get_data_final()), new_obj.get_id()))

        sql_code = "DELETE FROM vincula_cardapio_refeicao WHERE cardapio_id = ? AND refeicao_id NOT IN ?" # Deleta as refeições que não estão mais no cardápio
        cursor.execute(sql_code, (new_obj.get_id(), [ ref.get_id() for ref in new_obj.get_refeicoes() ]))

        sql_code = "INSERT INTO vincula_cardapio_refeicao (cardapio_id, refeicao_id, data, tipo) VALUES (?, ?, ?, ?)"

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
