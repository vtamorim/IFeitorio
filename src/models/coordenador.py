class Coordenador:
    def __init__(self, matricula : str, nome : str, senha : str,):
        self.set_matricula(matricula)
        self.set_nome(nome)
        self.set_senha(senha)

    def get_matricula(self) -> str:
        return self.__matricula
    def get_nome(self) -> str:
        return self.__nome
    def get_senha(self) -> str:
        return self.__senha

    def set_matricula(self, matricula: str) -> None: 
        if matricula == "": raise ValueError("Matrícula Inexistente")
        self.__matricula = matricula
    def set_nome(self, nome: str) -> None: 
        nome = nome.strip() # retira "espaços" dos lados da string
        if nome == "": raise ValueError("Nome não pode ser Nulo")
        self.__nome = nome
    def set_senha(self, senha: str) -> None: 
        senha = senha.strip() # retira "espaços" dos lados da string
        if senha == "": raise ValueError("Senha não pode ser Nula")
        self.__senha = senha

    def __str__(self):
        return f"{self.__matricula} - {self.__nome} - {self.__senha}"