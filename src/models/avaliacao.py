from typing import Optional
from .aluno import Aluno
from .refeicao import Refeicao

class Avaliacao:
    def __init__(self, id: int, nota: float, aluno: Aluno, refeicao: Refeicao, conteudo: Optional[str], titulo: Optional[str]) -> None:
        self.set_id(id)
        self.set_nota(nota)
        self.set_aluno(aluno)
        self.set_refeicao(refeicao)
        self.set_conteudo(conteudo)
        self.set_titulo(titulo)
    
    def get_id(self) -> int:
        return self.__id 
    def get_nota(self) -> float:
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
    def set_nota(self, nota: float) -> None: 
        if not isinstance(nota, (float)): raise ValueError
        self.__nota = nota
    def set_aluno(self, aluno: Aluno) -> None: 
        if not isinstance(aluno, (Aluno)): raise ValueError
        self.__aluno = aluno
    def set_refeicao(self, refeicao: Refeicao) -> None: 
        if not isinstance(refeicao, (Refeicao)): raise ValueError
        self.__refeicao = refeicao
    def set_conteudo(self, conteudo: str) -> None: 
        conteudo = conteudo.strip() # retira "espaços" dos lados da string
        if conteudo == "": raise ValueError
        self.__conteudo = conteudo
    def set_titulo(self, titulo: str) -> None: 
        titulo = titulo.strip() # retira "espaços" dos lados da string
        if titulo == "": raise ValueError
        self.__titulo = titulo

    def __str__(self) -> str:
           return f"Avaliação {self.__id} - {self.__nota}: {self.__aluno.get_nome()} - {self.__refeicao.get_nome()} | {self.__titulo} - {self.__conteudo}"
