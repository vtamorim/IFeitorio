class Avaliacao:
    def __init__(self, id: int, nota: float, conteudo: str, titulo: str, ref_id: int) -> None:
        self.set_id(id)
        self.set_nota(nota)
        self.set_conteudo(conteudo)
        self.set_titulo(titulo)
        self.set_ref_id(ref_id)
    
    def get_id(self) -> int:
        return self.__id 
    def get_nota(self) -> float:
        return self.__nota
    def get_conteudo(self) -> str:
        return self.__conteudo
    def get_titulo(self) -> str:
        return self.__titulo
    def get_ref_id(self) -> int:
        return self.__ref_id
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_nota(self, nota: float) -> None: 
        if not isinstance(nota, (float)): raise ValueError
        self.__nota = nota
    def set_conteudo(self, conteudo: str) -> None: 
        conteudo = conteudo.strip() # retira "espaços" dos lados da string
        if conteudo == "": raise ValueError
        self.__conteudo = conteudo
    def set_titulo(self, titulo: str) -> None: 
        titulo = titulo.strip() # retira "espaços" dos lados da string
        if titulo == "": raise ValueError
        self.__titulo = titulo
    def set_ref_id(self, ref_id: int) -> None: 
        if not isinstance(ref_id, (int)): raise ValueError
        self.__ref_id = ref_id

    def __str__(self) -> str:
           return f"{self.__id} - {self.__conteudo} - {self.__nota} - {self.__titulo} - {self.__ref_id}"