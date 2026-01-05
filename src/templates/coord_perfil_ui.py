import streamlit as st
from views import View
from time import sleep

class CoordenadorPerfilUI:
    """Página de Ver/Modificar o Perfil do Coordenador."""
    @staticmethod
    def main() -> None:
        st.header("Meu Perfil")

        matricula = st.text_input("Informe sua Matrícula", "123456789", disabled=True)
        nome = st.text_input("Informe seu Nome", "Coordenador Teste 1")
        senha = st.text_input("Informe sua Senha", type="password", value="123456789")
        realizar_atualizacao = st.button("Atualizar")

        if realizar_atualizacao: # Falta o "Update" com a View
            st.success("Conta atualizada com Sucesso!")
            
            sleep(1)
            st.rerun()