from typing import Optional

class Notificacao:
    def __init__(self, id: int, titulo : str, conteudo : Optional[str]) -> None:
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_conteudo(conteudo)
    
    def get_id(self) -> int:
        return self.__id 
    def get_titulo(self) -> str:
        return self.__titulo
    def get_conteudo(self) -> Optional[str]:
        return self.__conteudo
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_titulo(self, titulo: str) -> None: 
        titulo = titulo.strip()
        if not isinstance(titulo, (str)): raise ValueError
        self.__titulo = titulo
    def set_conteudo(self, conteudo: Optional[str]) -> None: 
        if not isinstance(conteudo, (str)): raise ValueError
        self.__conteudo = conteudo

    def __str__(self) -> str:
           return f"{self.__id} - {self.__titulo} - {self.__conteudo}"