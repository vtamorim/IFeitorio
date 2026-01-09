from .aluno import Aluno
from typing import Optional

class Notificacao:
    def __init__(self, id: int, titulo: str, conteudo: Optional[str], alunos_destinatarios: Optional[list[Aluno]] = None) -> None:
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_conteudo(conteudo)
        self.set_alunos_destinatarios(alunos_destinatarios if alunos_destinatarios else [])
    
    def get_id(self) -> int:
        return self.__id 
    def get_titulo(self) -> str:
        return self.__titulo
    def get_conteudo(self) -> Optional[str]:
        return self.__conteudo
    def get_alunos_destinatarios(self) -> list[Aluno]:
        return self.__alunos_destinatarios
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError

        self.__id = id
    def set_titulo(self, titulo: str) -> None: 
        titulo = titulo.strip()
        if titulo == "": raise ValueError

        self.__titulo = titulo
    def set_conteudo(self, conteudo: Optional[str]) -> None: 
        if conteudo is None or conteudo.strip() == "":
            self.__conteudo = None
            return
        conteudo = conteudo.strip()
        
        self.__conteudo = conteudo
    def set_alunos_destinatarios(self, alunos_destinatarios: list[Aluno]) -> None:
        if not isinstance(alunos_destinatarios, list): raise ValueError

        self.__alunos_destinatarios = alunos_destinatarios
    
    def add_aluno_destinatario(self, aluno: Aluno) -> None:
        if not isinstance(aluno, Aluno): raise ValueError

        self.__alunos_destinatarios.append(aluno)

    def __str__(self) -> str:
           return f"{self.__id} - {self.__titulo} - {self.__conteudo if self.__conteudo is not None else '(Sem Conteúdo)'}"
