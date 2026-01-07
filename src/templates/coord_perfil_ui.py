import streamlit as st
from views import View
from time import sleep

class CoordenadorPerfilUI:
    """Página de Ver/Modificar o Perfil do Coordenador."""
    @staticmethod
    def main() -> None:
        st.header("Meu Perfil")

        coord_matricula = st.session_state["user_matricula"]
        coord = View.coordenador_get_matricula(coord_matricula)

        st.text_input("Sua Matrícula", coord_matricula, disabled=True)
        nome = st.text_input("Informe seu Nome", coord.get_nome())
        senha = st.text_input("Informe sua Senha", type="password", value=coord.get_senha())
        realizar_atualizacao = st.button("Atualizar")

        if realizar_atualizacao:
            try:
                View.coordenador_update(coord_matricula, nome, senha)
                st.success("Conta atualizada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")
            
            sleep(1)
            st.rerun()