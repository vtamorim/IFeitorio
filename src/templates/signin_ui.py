import streamlit as st
from views import View
from time import sleep

class SigninUI:
    """Página de Abrir Conta de Aluno do Visitante."""
    @staticmethod
    def main() -> None:
        st.header("Abrir Conta no Sistema")

        restricoes_disponiveis = View.restricao_get_all()

        matricula = st.text_input("Informe sua Matrícula")
        nome = st.text_input("Informe seu Nome")
        senha = st.text_input("Informe sua Senha", type="password")
        restricoes = st.multiselect("Informe suas Restrições Alimentares", restricoes_disponiveis)
        realizar_criacao = st.button("Abrir")

        if realizar_criacao:
            try:
                View.aluno_add(matricula, nome, senha, restricoes)
                st.success("Conta criada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")
            
            sleep(1)
            st.rerun()
    