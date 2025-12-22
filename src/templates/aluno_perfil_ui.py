import streamlit as st
from views import View
from time import sleep

class AlunoPerfilUI:
    """Página de Ver/Modificar o Perfil do Aluno."""
    @staticmethod
    def main() -> None:
        st.header("Meu Perfil")

        restricoes_disponiveis = View.restricao_get_all() # Vamos pegar as restrições do banco de dados e os dados do aluno do "session_storage"

        matricula = st.text_input("Informe sua Matrícula", "123456789")
        nome = st.text_input("Informe seu Nome", "Aluno Teste 1")
        senha = st.text_input("Informe sua Senha", type="password", value="123456789")
        restricoes = st.multiselect("Informe suas Restrições Alimentares", [ "Vegetariano", "Vegano", "Intolerância à lactose" ], default=[])
        realizar_atualizacao = st.button("Atualizar")

        if realizar_atualizacao: # Falta o "Update" com a View
            st.success("Conta atualizada com Sucesso!")
            
            sleep(1)
            st.rerun()