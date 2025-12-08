from datetime import datetime

class Refeicao:
    def __init__(self, id: int, n: str, d: str, t: str, dt: datetime) -> None:
        self.set_id(id)
        self.set_nome(n)
        self.set_descricao(d)
        self.set_tipo(t)
        self.set_data(dt)
        self.set_mat_alu()
        self.set_mat_coo()
    
    def get_id(self) -> int:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    def get_descricao(self) -> str:
        return self.__descricao
    def get_tipo(self) -> str:
        return self.__tipo
    def get_data(self) -> datetime:
        return self.__data

    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError

        self.__id = id
    def set_nome(self, nome: str) -> None:
        nome = nome.strip()
        if not isinstance(nome, (str)): raise ValueError

        self.__nome = nome
    def set_descricao(self, descricao: str) -> None:
        descricao = descricao.strip()
        if not isinstance(descricao, (str)): raise ValueError

        self.__descricao = descricao
    def set_tipo(self, tipo: str) -> None:
        tipo = tipo.strip()
        if not isinstance(tipo, (str)): raise ValueError

        self.__tipo = tipo
    def set_data(self, data: datetime) -> None:
        if not isinstance(data, (datetime)): raise ValueError
        self.__data = data
    def set_mat_alu(self) -> None:
        self.__mat_alu = None
    
    def __str__(self) -> str:
        return f"{self.__id}: {self.__nome} - {self.__descricao} - {self.__tipo} - {self.__data}"
