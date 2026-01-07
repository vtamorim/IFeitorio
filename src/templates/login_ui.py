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

        if realizar_login:
            try:
                resultado = View.auth_user(matricula, senha)

                if resultado:
                    st.session_state["user_matricula"] = matricula
                    st.session_state["user_type"] = resultado
                    st.success("Login realizado com Sucesso!")
                else:
                    st.warning("Matrícula ou Senha Inválidos!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")
            
            sleep(1)
            st.rerun()
    