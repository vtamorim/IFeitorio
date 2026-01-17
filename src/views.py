from dao import *
from models import *
from typing import Any, Type, Optional
import qrcode
from datetime import date, timedelta

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
        if View.verificar_matricula(matricula):
            raise ValueError("Matrícula já está sendo Utilizada.")
        
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
        if View.verificar_matricula(matricula):
            raise ValueError("Matrícula já está sendo Utilizada.")
        
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
    def refeicao_add(nome: str, descricao: Optional[str], restricoes_compativeis: list[Restricao]) -> None:
        nova_refeicao = Refeicao(0, nome, descricao, restricoes_compativeis)
        View.add(RefeicaoDAO, nova_refeicao)
    
    @staticmethod
    def refeicao_update(refeicao_id: int, nome: str, descricao: Optional[str], restricoes_compativeis: list[Restricao]) -> None:
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
    
    #Métodos - Notificação
    @staticmethod
    def notificacao_get_all() -> list[Notificacao]:
        return View.get_all(NotificacaoDAO)
    
    @staticmethod
    def notificacao_get_aluno_matricula(aluno_matricula: str) -> list[Notificacao]:
        return NotificacaoDAO.get_aluno_matricula(aluno_matricula)

    @staticmethod
    def notificacao_add(titulo : str, conteudo : Optional[str], aluno_destinatarios : Optional[list[Aluno]] = None) -> None:
        nova_notificacao = Notificacao(0, titulo, conteudo, aluno_destinatarios)
        View.add(NotificacaoDAO, nova_notificacao)


    @staticmethod
    def notificacao_update(notificacao_id : int, titulo : str, conteudo : Optional[str], aluno_destinatarios : Optional[list[Aluno]] = None) -> None:
        nova_notificacao = Notificacao(notificacao_id,titulo, conteudo, aluno_destinatarios)
        View.update(NotificacaoDAO, nova_notificacao)


    @staticmethod
    def notificacao_delete(notificacao_id : int) -> None:
        View.delete(NotificacaoDAO, notificacao_id)
    
    # Métodos - Justificativa 

    @staticmethod
    def justificativa_get_all() -> list[Justificativa]:
        return View.get_all(JustificativaDAO)
    
    @staticmethod
    def justificativa_get_id(justificativa_id) -> Justificativa:
        return JustificativaDAO.get(justificativa_id)

    @staticmethod
    def justificativa_get_aluno_matricula(aluno_matricula: str) -> list[Justificativa]:
        return JustificativaDAO.get_aluno_matricula(aluno_matricula)

    @staticmethod
    def justificativa_add(falta : Falta, motivo: str, aprovada : Optional[bool] = None) -> None:
        nova_justificativa = Justificativa(0, falta, motivo, aprovada)
        View.add(JustificativaDAO, nova_justificativa)


    @staticmethod
    def justificativa_update(justificativa_id : int, falta : Falta, motivo :str, aprovada : Optional[bool] = None) -> None:
        nova_justificativa = Justificativa(justificativa_id,falta, motivo, aprovada)
        View.update(JustificativaDAO, nova_justificativa)


    @staticmethod
    def justificativa_delete(justificativa_id : int) -> None:
        View.delete(JustificativaDAO, justificativa_id)
    
    # Métodos - Falta

    @staticmethod
    def falta_get_all() -> list[Falta]:
        return View.get_all(FaltaDAO)
    
    @staticmethod
    def falta_get_id(falta_id: int) -> Falta:
        return FaltaDAO.get(falta_id)

    @staticmethod
    def falta_get_sem_justificativas(aluno_matricula: str) -> list[Falta]:
        return FaltaDAO.get_sem_justificativas(aluno_matricula)
    
    @staticmethod
    def falta_add(aluno: Aluno, cardapio: Cardapio, data: date | str, tipo: str) -> None: 
        nova_falta = Falta(0, aluno, cardapio, data, tipo)
        View.add(FaltaDAO, nova_falta)

    @staticmethod
    def falta_update(falta_id : int, aluno : Aluno, cardapio :Cardapio, data : date | str, tipo: str) -> None:
        nova_falta = Falta(falta_id, aluno, cardapio, data, tipo)
        View.update(FaltaDAO, nova_falta)

    @staticmethod
    def falta_delete(falta_id : int) -> None:
        View.delete(FaltaDAO, falta_id)


    # Métodos - Avaliação
    @staticmethod 
    def avaliacao_get_all() -> list[Avaliacao]:
        return View.get_all(AvaliacaoDAO)

    @staticmethod 
    def avaliacao_get_refeicao_id(refeicao_id: int) ->  list[Avaliacao]:
        return AvaliacaoDAO.get_refeicao_id(refeicao_id)

    @staticmethod
    def avaliacao_add(nota : int, aluno : Aluno, refeicao : Refeicao, conteudo : Optional[str],titulo: Optional[str]) -> None:
        nova_avaliacao = Avaliacao(0, nota, aluno, refeicao,conteudo, titulo)
        View.add(AvaliacaoDAO, nova_avaliacao)

    @staticmethod
    def avaliacao_update(avaliacao_id : int, nota : int, aluno : Aluno, refeicao : Refeicao, conteudo : Optional[str], titulo : Optional[str]) -> None:
        nova_avaliacao = Avaliacao(avaliacao_id, nota, aluno, refeicao, conteudo, titulo)
        View.update(AvaliacaoDAO, nova_avaliacao)
    
    @staticmethod 
    def avaliacao_delete( avaliacao_id : int) -> None:
        View.delete(AvaliacaoDAO, avaliacao_id)


    # Métodos - Cardapio
    
    @staticmethod 
    def cardapio_get_all() -> list[Cardapio]:
        return View.get_all(CardapioDAO)
    

    @staticmethod 
    def cardapio_get_id(cardapio_id) ->  Cardapio:
        return CardapioDAO.get(cardapio_id)

    @staticmethod
    def cardapio_add(data_inicial: date | str, data_final: date | str, refeicoes: Optional[list[Refeicao]] = None) -> None:
        novo_cardapio = Cardapio(0, data_inicial , data_final, refeicoes)
        View.add(CardapioDAO, novo_cardapio)

    @staticmethod
    def cardapio_update(cardapio_id : int, data_inicial : date | str, data_final : date | str, refeicoes : Optional[list[Refeicao]]) -> None:
        novo_cardapio = Cardapio(cardapio_id,data_inicial, data_final, refeicoes)
        View.update(CardapioDAO, novo_cardapio)
    
    @staticmethod 
    def cardapio_delete(cardapio_id : int) -> None:
        View.delete(CardapioDAO, cardapio_id)

    # Métodos - Outros
    @staticmethod
    def calc_dias_da_semana(dia: date) -> tuple[date, date]:
        """Retorna a segunda-feira e a sexta-feira da semana do "dia" enviado."""
        dias_desde_domingo = (dia.weekday() + 1) % 7
        inicio_semana = dia - timedelta(days=dias_desde_domingo)
        primeira_segunda = inicio_semana + timedelta(days=1)
        primeira_sexta = inicio_semana + timedelta(days=5)
        return (primeira_segunda, primeira_sexta)

    @staticmethod
    def calc_dias_intermediarios(data_inicial: date, data_final: date) -> list[date]:
        datas = []
        data_atual = data_inicial
        while data_atual <= data_final:
            datas.append(data_atual)
            data_atual += timedelta(days=1)
        return datas

    @staticmethod
    def set_cardapio_dia_diferente(cardapio: Cardapio, refeicoes: list[Refeicao], data: date) -> None:
        card_refeicoes = cardapio.get_refeicoes()
        card_refeicoes = [ r for r in card_refeicoes if r.get_data() != data ]
        for ref in refeicoes:
            ref.set_data(data)
        card_refeicoes.extend(refeicoes)
        cardapio.set_refeicoes(card_refeicoes)
    
    @staticmethod
    def gerar_qrcode(texto: str):
        qr = qrcode.QRCode(border=3)
        qr.add_data(texto)
        img = qr.make_image(fill_color="black", back_color="#01BE64")
        return img.get_image()

    # Métodos - Autenticação
    @staticmethod
    def auth_user(matricula: str, senha: str) -> Optional[UsersTypeIDs]:
        """Retorna o tipo de Usuário caso a matrícula e a senha estejam corretas."""
        alunos = View.aluno_get_all()
        coords = View.coordenador_get_all()

        for al in alunos:
            if al.get_matricula() == matricula and al.get_senha() == senha:
                return UsersTypeIDs.ALUNO

        for co in coords:
            if co.get_matricula() == matricula and co.get_senha() == senha:
                return UsersTypeIDs.COORDENADOR
        
    @staticmethod
    def verificar_matricula(matricula: str) -> bool:
        """Retorna se a matrícula já está sendo utilizada"""
        alunos = View.aluno_get_all()
        coords = View.coordenador_get_all()

        for al in alunos:
            if al.get_matricula() == matricula:
                return True

        for co in coords:
            if co.get_matricula() == matricula:
                return True

        return False
    
    @staticmethod
    def get_user_types() -> Type[UsersTypeIDs]: return UsersTypeIDs
