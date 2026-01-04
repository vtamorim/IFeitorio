import streamlit as st
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

        op = st.sidebar.selectbox("Menu", ["Meu Perfil", "Ver Cardápio", "Analisar Refeição", "Ver Notificações", "Justificar Faltas"])

        if op == "Meu Perfil": AlunoPerfilUI.main()
        elif op == "Ver Cardápio": AlunoVisualizarCardapiosUI.main()
        elif op == "Analisar Refeição": AlunoAvaliarRefeicaoUI.main()
        elif op == "Ver Notificações": AlunoVisualizarNotificacoesUI.main()
        elif op == "Justificar Faltas": AlunoJustificarUI.main()
    
    @staticmethod
    def sidebar() -> None: # Falta analisar o "session_storage" para definir o menu correto
        IndexUI.menu_visitante()

    @staticmethod
    def main() -> None:
        st.set_page_config(layout="centered")
        IndexUI.sidebar()

if __name__ == "__main__":
    IndexUI.main()
