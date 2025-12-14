from dao import *
from models import *
from typing import Any, Type, Optional

class View:
    # Métodos Abstratos - Todos os DAOs tem um "padrão", esses métodos recebem o DAO e chamam o método apropriado.
    @staticmethod
    def get_all(dao_class: Type[AbstractDAO]) -> list[Any]: return dao_class.get_all()
    
    @staticmethod
    def add(dao_class: Type[AbstractDAO], obj: Any) -> None:
        dao_class.add(obj)
    
    @staticmethod
    def update(dao_class: Type[AbstractDAO], obj: Any) -> None:
        dao_class.update(obj)
    
    @staticmethod
    def delete(dao_class: Type[AbstractDAO], obj: Any) -> None:
        dao_class.delete(obj)

    # Métodos - Aluno
    @staticmethod
    def aluno_get_all() -> list[Aluno]:
        return View.get_all(AlunoDAO)
    
    @staticmethod
    def aluno_get_matricula(matricula: str) -> Aluno:
        return AlunoDAO.get(matricula)
    
    @staticmethod
    def aluno_add(matricula: str, nome: str, senha: str, restricoes: list[Restricao]) -> None:
        novo_aluno = Aluno(matricula, nome, senha, restricoes)
        View.add(AlunoDAO, novo_aluno)
    
    @staticmethod
    def aluno_update(matricula: str, nome: str, senha: str, restricoes: list[Restricao]) -> None:
        novo_aluno = Aluno(matricula, nome, senha, restricoes)
        View.update(AlunoDAO, novo_aluno)
    
    @staticmethod
    def aluno_delete(matricula: str) -> None:
        View.delete(AlunoDAO, matricula)

    # Métodos - Coordenador
    @staticmethod
    def coordenador_get_all() -> list[Coordenador]:
        return View.get_all(CoordenadorDAO)
    
    @staticmethod
    def coordenador_get_matricula(matricula: str) -> Coordenador:
        return CoordenadorDAO.get(matricula)
    
    @staticmethod
    def coordenador_add(matricula: str, nome: str, senha: str) -> None:
        novo_coordenador = Coordenador(matricula, nome, senha)
        View.add(CoordenadorDAO, novo_coordenador)
    
    @staticmethod
    def coordenador_update(matricula: str, nome: str, senha: str) -> None:
        novo_coordenador = Coordenador(matricula, nome, senha)
        View.update(CoordenadorDAO, novo_coordenador)
    
    @staticmethod
    def coordenador_delete(matricula: str) -> None:
        View.delete(CoordenadorDAO, matricula)

    # Métodos - Refeicao
    @staticmethod
    def refeicao_get_all() -> list[Refeicao]:
        return View.get_all(RefeicaoDAO)
    
    @staticmethod
    def refeicao_get_id(refeicao_id: int) -> Refeicao:
        return RefeicaoDAO.get(refeicao_id)
    
    @staticmethod
    def refeicao_add(nome: str, descricao: str, restricoes_compativeis: list[Restricao]) -> None:
        nova_refeicao = Refeicao(0, nome, descricao, restricoes_compativeis)
        View.add(RefeicaoDAO, nova_refeicao)
    
    @staticmethod
    def refeicao_update(refeicao_id: int, nome: str, descricao: str, restricoes_compativeis: list[Restricao]) -> None:
        nova_refeicao = Refeicao(refeicao_id, nome, descricao, restricoes_compativeis)
        View.update(RefeicaoDAO, nova_refeicao)
    
    @staticmethod
    def refeicao_delete(refeicao_id: int) -> None:
        View.delete(RefeicaoDAO, refeicao_id)

    # Métodos - Restrição
    @staticmethod
    def restricao_get_all() -> list[Restricao]:
        return View.get_all(RestricaoDAO)
    
    @staticmethod
    def restricao_add(nome: str) -> None:
        nova_restricao = Restricao(0, nome)
        View.add(RestricaoDAO, nova_restricao)
    
    @staticmethod
    def restricao_update(restricao_id: int, nome: str) -> None:
        nova_restricao = Restricao(restricao_id, nome)
        View.update(RestricaoDAO, nova_restricao)
    
    @staticmethod
    def restricao_delete(restricao_id: int) -> None:
        View.delete(RestricaoDAO, restricao_id)
    
