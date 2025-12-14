from .aluno import Aluno
from .cardapio import Cardapio
from datetime import date

class Falta:
    """Classe que representa a falta de um aluno em uma refeição de um cardápio."""
    def __init__(self, id: int, aluno: Aluno, cardapio: Cardapio, data: date | str, tipo: str) -> None:
        self.set_id(id)
        self.set_aluno(aluno)
        self.set_cardapio(cardapio)
        self.set_data(data)
        self.set_tipo(tipo)
    
    def get_id(self) -> int:
        return self.__id
    def get_aluno(self) -> Aluno:
        return self.__aluno
    def get_cardapio(self) -> Cardapio:
        return self.__cardapio
    def get_data(self) -> date:
        return self.__data
    def get_tipo(self) -> str:
        return self.__tipo

    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError

        self.__id = id
    def set_aluno(self, aluno: Aluno) -> None:
        if not isinstance(aluno, Aluno): raise ValueError

        self.__aluno = aluno
    def set_cardapio(self, cardapio: Cardapio) -> None:
        if not isinstance(cardapio, Cardapio): raise ValueError

        self.__cardapio = cardapio
    def set_data(self, data: date | str) -> None:
        if isinstance(data, str):
            data = date.strptime(data, "%d/%m/%Y")
        elif not isinstance(data, date): raise ValueError
        if self.__cardapio.get_data_inicial() > data or self.__cardapio.get_data_final() < data: raise ValueError

        self.__data = data
    def set_tipo(self, tipo: str) -> None:
        tipo = tipo.strip()
        if tipo == "": raise ValueError

        self.__tipo = tipo
    
    def get_data_formatada(self) -> str:
        return self.__data.strftime("%d/%m/%Y")
    
    def __str__(self) -> str:
        return f"Falta {self.__id}: {self.__aluno.get_matricula()} - Cardápio {self.__cardapio.get_id()} - {self.get_data_formatada()} - {self.__tipo}"
