class Restricao:
    def __init__(self, am: str, n: str) -> None:
        self.set_aluno_matricula(am)
        self.set_nome(n)
    
    def get_aluno_matricula(self) -> str:
        return self.__aluno_matricula
    def get_nome(self) -> str:
        return self.__nome
    
    def set_aluno_matricula(self, aluno_matricula: str) -> None:
        aluno_matricula = aluno_matricula.strip()
        if aluno_matricula == "": raise ValueError

        self.__aluno_matricula = aluno_matricula
    def set_nome(self, nome: str) -> None:
        nome = nome.strip()
        if nome == "": raise ValueError

        self.__nome = nome

    def __str__(self) -> str:
        return f"{self.__aluno_matricula}: {self.__nome}"
