from .refeicao import Refeicao
from datetime import date

class Cardapio:
    def __init__(self, data_inicial: date, data_final: date, refeicoes: list[Refeicao] = []) -> None:
        self.set_data_inicial(data_inicial)
        self.set_data_final(data_final)
        self.set_refeicoes(refeicoes)

    def get_data_inicial(self) -> date:
        return self.__data_inicial
    def get_data_final(self) -> date:
        return self.__data_final
    def get_refeicoes(self) -> list[Refeicao]:
        return self.__refeicoes

    def set_data_inicial(self, data_inicial: date) -> None:
        if not isinstance(data_inicial, date): raise ValueError

        self.__data_inicial = data_inicial
    def set_data_final(self, data_final: date) -> None:
        if not isinstance(data_final, date): raise ValueError

        self.__data_final = data_final
    def set_refeicoes(self, refeicoes: list[Refeicao]) -> None:
        if not isinstance(refeicoes, list): raise ValueError

        self.__refeicoes = refeicoes

    def add_refeicao(self, refeicao: Refeicao) -> None:
        """Adiciona uma refeição no cardápio."""
        if self.__data_inicial > refeicao.get_data() or refeicao.get_data() > self.__data_final: raise ValueError # Data da refeição não está entre o período do cardápio
        elif refeicao.get_data() is None or refeicao.get_tipo() is None: raise ValueError # Refeição precisa ter um tipo e uma data.

        self.__refeicoes.append(refeicao)

    @staticmethod
    def get_data_formatada(data: date) -> str:
        """Retorna a data de forma formatada (função "strftime") para uma string."""
        return data.strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return f"Cardápio {self.get_data_formatada(self.__data_inicial)} - {self.get_data_formatada(self.__data_final)}"
