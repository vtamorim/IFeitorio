import streamlit as st
from views import View
from time import sleep

class AlunoPerfilUI:
    """Página de Ver/Modificar o Perfil do Aluno."""
    @staticmethod
    def main() -> None:
        st.header("Meu Perfil")

        aluno_matricula = st.session_state["user_matricula"]
        aluno = View.aluno_get_matricula(aluno_matricula)

        restricoes_disponiveis = View.restricao_get_all()

        st.text_input("Sua Matrícula", aluno_matricula, disabled=True)
        nome = st.text_input("Informe seu Nome", aluno.get_nome())
        senha = st.text_input("Informe sua Senha", type="password", value=aluno.get_senha())
        restricoes = st.multiselect("Informe suas Restrições Alimentares", restricoes_disponiveis, default=aluno.get_restricoes())
        realizar_atualizacao = st.button("Atualizar")

        if realizar_atualizacao:
            try:
                View.aluno_update(aluno_matricula, nome, senha, restricoes)
                st.success("Conta atualizada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")
            
            sleep(1)
            st.rerun()