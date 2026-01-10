from .restricao import Restricao

class Aluno:
    def __init__(self, matricula: str, nome: str, senha: str, restricoes: list[Restricao]) -> None:
        self.set_matricula(matricula)
        self.set_nome(nome)
        self.set_senha(senha)
        self.set_restricoes(restricoes)

    def get_matricula(self) -> str:
        return self.__matricula
    def get_nome(self) -> str:
        return self.__nome
    def get_senha(self) -> str:
        return self.__senha
    def get_restricoes(self) -> list[Restricao]:
        return self.__restricoes
    
    def set_matricula(self, matricula: str) -> None: 
        if matricula == "": raise ValueError("Matrícula não pode ser Vazia")
        self.__matricula = matricula
    def set_nome(self, nome: str) -> None: 
        nome = nome.strip() # retira "espaços" dos lados da string
        if nome == "": raise ValueError("Nome não pode ser Vazio")
        self.__nome = nome
    def set_senha(self, senha: str) -> None: 
        senha = senha.strip() # retira "espaços" dos lados da string
        if senha == "": raise ValueError("Senha não pode ser Vazia")
        self.__senha = senha
    def set_restricoes(self, restricoes: list[Restricao]) -> None: 
        if not isinstance(restricoes, (list)): raise ValueError("Restrições Inválidas")
        self.__restricoes = restricoes
    
    def add_restricao(self, restricao: Restricao) -> None:
        if not isinstance(restricao, Restricao): raise ValueError("Restrição Inválida")

        self.__restricoes.append(restricao)

    def __str__(self) -> str:
        return f"{self.__matricula} - {self.__nome} - {self.__senha} - {len(self.__restricoes)} Restrições"
