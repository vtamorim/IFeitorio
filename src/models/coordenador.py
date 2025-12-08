class Coordenador:
    def __init__(self, id : int, mat : str, n : str, s : str,):
        self.set_id(id)
        self.set_matricula(mat)
        self.set_nome(n)
        self.set_senha(s)

    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_matricula(self, matricula: str) -> None: 
        if matricula == "": raise ValueError
        self.__matricula = matricula
    def set_nome(self, nome: str) -> None: 
        nome = nome.strip() # retira "espaços" dos lados da string
        if nome == "": raise ValueError
        self.__nome = nome
    def set_senha(self, senha: str) -> None: 
        senha = senha.strip() # retira "espaços" dos lados da string
        if senha == "": raise ValueError
        self.__senha = senha

    def get_id(self) -> int:
        return self.__id 
    def get_matricula(self) -> str:
        return self.__matricula
    def get_nome(self) -> str:
        return self.__nome
    def get_senha(self) -> str:
        return self.__senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__matricula} - {self.__senha}"