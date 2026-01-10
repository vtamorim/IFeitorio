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
        if not isinstance(id, int): raise ValueError("ID Inválido")

        self.__id = id
    def set_nome(self, nome: str) -> None:
        nome = nome.strip()
        if nome == "": raise ValueError("Nome não pode ser vazio")

        self.__nome = nome
    def set_descricao(self, descricao: Optional[str]) -> None:
        if descricao is None or descricao.strip() == "":
            self.__descricao = None
            return
        descricao = descricao.strip()

        self.__descricao = descricao
    def set_restricoes_compativeis(self, restricoes_compativeis: list[Restricao]) -> None:
        if not isinstance(restricoes_compativeis, list): raise ValueError("Restrições Compatíveis Inválidas")

        self.__restricoes_compativeis = restricoes_compativeis
    def set_data(self, data: Optional[date | str]) -> None:
        if isinstance(data, str):
            data = datetime.strptime(data, "%d/%m/%Y").date()
        if data is not None and not isinstance(data, date): raise ValueError("Data Inválida")

        self.__data = data
    def set_tipo(self, tipo: Optional[str]) -> None:
        if tipo is None:
            self.__tipo = None
            return
        if not isinstance(tipo, str): raise ValueError("Tipo Inválido")

        self.__tipo = tipo
    
    def add_restricao_compativel(self, restricao: Restricao) -> None:
        if not isinstance(restricao, Restricao): raise ValueError("Restrição Inválida")

        self.__restricoes_compativeis.append(restricao)
    
    def get_data_formatada(self) -> Optional[str]:
        """Retorna a data da Refeição de forma formatada (função "strftime") para uma string."""
        return self.__data.strftime("%d/%m/%Y") if self.__data is not None else None
    
    def __eq__(self, value: object) -> bool: # Métodos "__eq__" e "__hash__" servem para comparar objetos de "Refeicao"
        if not isinstance(value, Refeicao): return False

        return hash(self) == hash(value)
    
    def __hash__(self) -> int:
        components = []
        components.append(self.__id)
        components.append(self.__nome)
        components.append(self.__descricao)
        for r in self.__restricoes_compativeis:
            components.append(hash(r))
        components.append(self.get_data_formatada())
        components.append(self.__tipo)
        
        return hash(tuple(components))
    
    def __str__(self) -> str:
        desc = self.__descricao if self.__descricao is not None else "Sem Descrição"
        if not self.__data:
            return f"{self.__id}: {self.__nome} - {desc} - {len(self.__restricoes_compativeis)} Restrições"
        return f"{self.__id}: {self.__nome} - {desc} - {len(self.__restricoes_compativeis)} Restrições | {self.get_data_formatada()} - {self.__tipo}"
