import streamlit as st
from views import View
from time import sleep

class SigninUI:
    """Página de Abrir Conta de Aluno do Visitante."""
    @staticmethod
    def main() -> None:
        st.header("Abrir Conta no Sistema")

        restricoes_disponiveis = View.restricao_get_all() # Vamos pegar as restrições do banco de dados e os dados do aluno do "session_storage"

        matricula = st.text_input("Informe sua Matrícula")
        nome = st.text_input("Informe seu Nome")
        senha = st.text_input("Informe sua Senha", type="password")
        restricoes = st.multiselect("Informe suas Restrições Alimentares", [ "Vegetariano", "Vegano", "Intolerância à lactose" ])
        realizar_criacao = st.button("Abrir")

        if realizar_criacao: # Falta o "add" com a View
            st.success("Conta criada com Sucesso!")
            
            sleep(1)
            st.rerun()
    