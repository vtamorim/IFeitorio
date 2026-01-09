from typing import Optional
from .aluno import Aluno
from .refeicao import Refeicao

class Avaliacao:
    def __init__(self, id: int, nota: int, aluno: Aluno, refeicao: Refeicao, conteudo: Optional[str], titulo: Optional[str]) -> None:
        self.set_id(id)
        self.set_nota(nota)
        self.set_aluno(aluno)
        self.set_refeicao(refeicao)
        self.set_conteudo(conteudo)
        self.set_titulo(titulo)
    
    def get_id(self) -> int:
        return self.__id 
    def get_nota(self) -> int:
        return self.__nota
    def get_aluno(self) -> Aluno:
        return self.__aluno
    def get_refeicao(self) -> Refeicao:
        return self.__refeicao
    def get_conteudo(self) -> Optional[str]:
        return self.__conteudo
    def get_titulo(self) -> Optional[str]:
        return self.__titulo
    
    def set_id(self, id: int) -> None:
        if not isinstance(id, (int)): raise ValueError
        self.__id = id
    def set_nota(self, nota: int) -> None: 
        if not isinstance(nota, int): raise ValueError
        self.__nota = nota
    def set_aluno(self, aluno: Aluno) -> None: 
        if not isinstance(aluno, (Aluno)): raise ValueError
        self.__aluno = aluno
    def set_refeicao(self, refeicao: Refeicao) -> None: 
        if not isinstance(refeicao, (Refeicao)): raise ValueError
        self.__refeicao = refeicao
    def set_conteudo(self, conteudo: Optional[str]) -> None: 
        if conteudo is None or conteudo.strip() == "":
            self.__conteudo = None
            return
        conteudo = conteudo.strip()

        self.__conteudo = conteudo
    def set_titulo(self, titulo: Optional[str]) -> None: 
        if titulo is None or titulo.strip() == "":
            self.__titulo = None
            return
        titulo = titulo.strip()

        self.__titulo = titulo

    def __str__(self) -> str:
           return f"Avaliação {self.__id}: {self.__aluno.get_nome()}"
