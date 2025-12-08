from .aluno import Aluno
from .cardapio import Cardapio
from .refeicao import Refeicao

class Falta:
    """Classe que representa a falta de um aluno em uma refeição de um cardápio."""
    def __init__(self, id: int, aluno: Aluno, cardapio: Cardapio, refeicao: Refeicao) -> None:
        self.set_id(id)
        self.set_aluno(aluno)
        self.set_cardapio(cardapio)
        self.set_refeicao(refeicao)
    
    def get_id(self) -> int:
        return self.__id
    def get_aluno(self) -> Aluno:
        return self.__aluno
    def get_cardapio(self) -> Cardapio:
        return self.__cardapio
    def get_refeicao(self) -> Refeicao:
        return self.__refeicao

    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError

        self.__id = id
    def set_aluno(self, aluno: Aluno) -> None:
        if not isinstance(aluno, Aluno): raise ValueError

        self.__aluno = aluno
    def set_cardapio(self, cardapio: Cardapio) -> None:
        if not isinstance(cardapio, Cardapio): raise ValueError

        self.__cardapio = cardapio
    def set_refeicao(self, refeicao: Refeicao) -> None:
        if not isinstance(refeicao, Refeicao): raise ValueError

        self.__refeicao = refeicao
    
    def __str__(self) -> str:
        return f"Falta {self.__id} - {self.__aluno.get_nome()} - {self.__cardapio.get_data_formatada(self.__cardapio.get_data_inicial())} - {self.__refeicao.get_data_formatada()}"
