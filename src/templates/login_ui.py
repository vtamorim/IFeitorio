import streamlit as st
from views import View
from time import sleep

class LoginUI:
    """Página de Login do Visitante."""
    @staticmethod
    def main() -> None:
        st.header("Entrar no Sistema")

        matricula = st.text_input("Informe sua Matrícula")
        senha = st.text_input("Informe sua Senha", type="password")
        realizar_login = st.button("Entrar")

        if realizar_login: # Falta a autenticação com a View
            st.success("Login realizado com Sucesso!")
            
            sleep(1)
            st.rerun()
    