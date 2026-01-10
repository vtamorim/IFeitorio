import streamlit as st
from views import View
from templates import *

class IndexUI:
    @staticmethod
    def menu_visitante() -> None:
        st.sidebar.header("Menu de Visitante")

        op = st.sidebar.selectbox("Menu", ["Entrar no Site", "Criar Conta"])

        if op == "Entrar no Site": LoginUI.main()
        elif op == "Criar Conta": SigninUI.main()
    
    @staticmethod
    def menu_aluno() -> None:
        st.sidebar.header("Menu de Aluno")

        op = st.sidebar.selectbox("Menu", ["Meu Perfil", "Ver Cardápio", "Analisar Refeição", "Ver Notificações", "Justificar Faltas", "Ver Justificativas"])

        if op == "Meu Perfil": AlunoPerfilUI.main()
        elif op == "Ver Cardápio": AlunoVisualizarCardapiosUI.main()
        elif op == "Analisar Refeição": AlunoAvaliarRefeicaoUI.main()
        elif op == "Ver Notificações": AlunoVisualizarNotificacoesUI.main()
        elif op == "Justificar Faltas": AlunoJustificarUI.main()
        elif op == "Ver Justificativas": AlunoVerJustificativasUI.main()
    
    @staticmethod
    def menu_coordenador() -> None:
        st.sidebar.header("Menu de Coordenador")

        op = st.sidebar.selectbox("Menu", ["Meu Perfil", "Gerenciar Restrições", "Gerenciar Refeições", "Gerenciar Cardápios", "Gerenciar Avaliações", "Gerenciar Notificações", "Gerenciar Faltas", "Gerenciar Justificativas", "Gerenciar Alunos"])

        if op == "Meu Perfil": CoordenadorPerfilUI.main()
        elif op == "Gerenciar Restrições": CoordenadorGerenciarRestricoesUI.main()
        elif op == "Gerenciar Refeições": CoordenadorGerenciarRefeicoesUI.main()
        elif op == "Gerenciar Cardápios": CoordenadorGerenciarCardapiosUI.main()
        elif op == "Gerenciar Avaliações": CoordenadorGerenciarAvaliacoesUI.main()
        elif op == "Gerenciar Notificações": CoordenadorGerenciarNotificacoesUI.main()
        elif op == "Gerenciar Faltas": CoordenadorGerenciarFaltasUI.main()
        elif op == "Gerenciar Justificativas": CoordenadorGerenciarJustificativasUI.main()
        elif op == "Gerenciar Alunos": CoordenadorGerenciarAlunosUI.main()
    
    @staticmethod
    def log_out_sidebar() -> None:
        """Coloca o botão de 'sair da conta' no Sidebar."""
        if st.sidebar.button("Sair", type="primary"):
            del st.session_state["user_matricula"]
            del st.session_state["user_type"]
            st.rerun()

    @staticmethod
    def sidebar() -> None:
        """Mostra o Sidebar."""
        if "user_matricula" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            users_type = View.get_user_types()
            match st.session_state["user_type"]:
                case users_type.ALUNO: IndexUI.menu_aluno()
                case users_type.COORDENADOR: IndexUI.menu_coordenador()
            
            IndexUI.log_out_sidebar()

    @staticmethod
    def main() -> None:
        st.set_page_config(layout="centered")
        IndexUI.sidebar()

if __name__ == "__main__":
    IndexUI.main()
