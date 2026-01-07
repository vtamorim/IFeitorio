from datetime import datetime, date
from .restricao import Restricao
from typing import Optional

class Refeicao:
    def __init__(self, id: int, nome: str, descricao: Optional[str], restricoes_compativeis: list[Restricao], data: Optional[date] = None, tipo: Optional[str] = None) -> None: # tipo = lanche / almoço / jantar
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_restricoes_compativeis(restricoes_compativeis)
        self.set_data(data) # "data" é opcional, pois ele será atribuído caso esse objeto "Refeição" seja colocado em um cardápio, pois é ele quem decidirá o seu horário e dia.
        self.set_tipo(tipo) # Mesma coisa com "tipo".
    
    def get_id(self) -> int: 
        return self.__id
    def get_nome(self) -> str: 
        return self.__nome
    def get_descricao(self) -> Optional[str]: 
        return self.__descricao
    def get_restricoes_compativeis(self) -> list[Restricao]: 
        return self.__restricoes_compativeis
    def get_data(self) -> Optional[date]: 
        return self.__data
    def get_tipo(self) -> Optional[str]: 
        return self.__tipo

    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError

        self.__id = id
    def set_nome(self, nome: str) -> None:
        nome = nome.strip()
        if nome == "": raise ValueError

        self.__nome = nome
    def set_descricao(self, descricao: Optional[str]) -> None:
        if descricao is None:
            self.__descricao = None
            return
        descricao = descricao.strip()
        if descricao == "": raise ValueError

        self.__descricao = descricao
    def set_restricoes_compativeis(self, restricoes_compativeis: list[Restricao]) -> None:
        if not isinstance(restricoes_compativeis, list): raise ValueError

        self.__restricoes_compativeis = restricoes_compativeis
    def set_data(self, data: Optional[date | str]) -> None:
        if isinstance(data, str):
            data = datetime.strptime(data, "%d/%m/%Y").date()
        if data is not None and not isinstance(data, date): raise ValueError

        self.__data = data
    def set_tipo(self, tipo: Optional[str]) -> None:
        if tipo is None:
            self.__tipo = None
            return
        if not isinstance(tipo, str): raise ValueError

        self.__tipo = tipo
    
    def add_restricao_compativel(self, restricao: Restricao) -> None:
        if not isinstance(restricao, Restricao): raise ValueError

        self.__restricoes_compativeis.append(restricao)
    
    def get_data_formatada(self) -> Optional[str]:
        """Retorna a data da Refeição de forma formatada (função "strftime") para uma string."""
        return self.__data.strftime("%d/%m/%Y") if self.__data is not None else None
    
    def __str__(self) -> str:
        restricoes = " ".join([ rc.get_nome() for rc in self.__restricoes_compativeis ]) # Junta os nomes de todas as restrições
        if restricoes == "": restricoes = "Nenhuma Restrição"
        data_tipo = f" | {self.get_data_formatada()} - {self.__tipo}" if self.get_data_formatada() is not None and self.__tipo is not None else "" # Escreve a data e tipo se eles não forem nulos.
        return f"{self.__id}: {self.__nome} - {self.__descricao} - {restricoes}{data_tipo}"
