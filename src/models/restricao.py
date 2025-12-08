class Restricao:
    def __init__(self, id: int, nome: str) -> None:
        self.set_id(id)
        self.set_nome(nome)
    
    def get_id(self) -> str:
        return self.__id
    def get_nome(self) -> str:
        return self.__nome
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, int): raise ValueError

        self.__id = id
    def set_nome(self, nome: str) -> None:
        nome = nome.strip()
        if nome == "": raise ValueError

        self.__nome = nome

    def __str__(self) -> str:
        return f"{self.__id}: {self.__nome}"
