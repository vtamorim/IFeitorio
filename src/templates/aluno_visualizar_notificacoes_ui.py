import streamlit as st

class AlunoVisualizarNotificacoesUI:
    """Página que exibe as notificações recebidas do Aluno."""
    @staticmethod
    def main() -> None:
        st.header("Visualizar Notificações")

        st.divider()
        st.subheader("Título 1")
        st.text("lorem ipsum dolor amet")

        st.divider()
        st.subheader("Título 2")
        st.text("(Sem conteúdo)")

        st.divider()
        st.subheader("Título 3")
        st.text("lorem ipsum dolor amet 2.")
