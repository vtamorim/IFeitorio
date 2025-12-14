from .refeicao import Refeicao
from datetime import date
from typing import Optional

class Cardapio:
    def __init__(self, id: int, data_inicial: date | str, data_final: date | str, refeicoes: Optional[list[Refeicao]] = None) -> None:
        self.set_id(id)
        self.set_data_inicial(data_inicial)
        self.set_data_final(data_final)
        self.set_refeicoes(refeicoes if refeicoes else [])

    def get_id(self) -> int:
        return self.__id
    def get_data_inicial(self) -> date:
        return self.__data_inicial
    def get_data_final(self) -> date:
        return self.__data_final
    def get_refeicoes(self) -> list[Refeicao]:
        return self.__refeicoes

    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError

        self.__id = id
    def set_data_inicial(self, data_inicial: date | str) -> None:
        if isinstance(data_inicial, str):
            data_inicial = date.strptime(data_inicial, "%d/%m/%Y")
        if not isinstance(data_inicial, date): raise ValueError

        self.__data_inicial = data_inicial
    def set_data_final(self, data_final: date | str) -> None:
        if isinstance(data_final, str):
            data_final = date.strptime(data_final, "%d/%m/%Y")
        if not isinstance(data_final, date): raise ValueError

        self.__data_final = data_final
    def set_refeicoes(self, refeicoes: list[Refeicao]) -> None:
        if not isinstance(refeicoes, list): raise ValueError
        if any(ref.get_data() is None or ref.get_tipo() is None for ref in refeicoes):
            raise ValueError("Todas as Refeições de um Cardápio devem ter data e tipo.")

        self.__refeicoes = refeicoes

    def add_refeicao(self, refeicao: Refeicao) -> None:
        """Adiciona uma refeição no cardápio."""
        if refeicao.get_data() is None or refeicao.get_tipo() is None: raise ValueError("Todas as Refeições de um Cardápio devem ter data e tipo.")
        elif self.__data_inicial > refeicao.get_data() or refeicao.get_data() > self.__data_final: raise ValueError # Data da refeição não está entre o período do cardápio

        self.__refeicoes.append(refeicao)

    @staticmethod
    def get_data_formatada(data: date) -> str:
        """Retorna a data de forma formatada (função "strftime") para uma string."""
        return data.strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return f"Cardápio {self.__id}: {self.get_data_formatada(self.__data_inicial)} - {self.get_data_formatada(self.__data_final)}"
