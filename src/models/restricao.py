class Restricao:
    def __init__(self, id: int, nome: str) -> None:
        self.set_id(id)
        self.set_nome(nome)
    
    def get_id(self) -> int:
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

    def __eq__(self, value: object) -> bool: # Métodos "__eq__" e "__hash__" servem para comparar objetos de "Restricao"
        if not isinstance(value, Restricao): return False

        return hash(self) == hash(value)
    
    def __hash__(self) -> int:
        return hash((self.__id, self.__nome))

    def __str__(self) -> str:
        return f"{self.__id}: {self.__nome}"
