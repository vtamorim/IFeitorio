import streamlit as st
from views import View

class AlunoVisualizarNotificacoesUI:
    """Página que exibe as notificações recebidas do Aluno."""
    @staticmethod
    def main() -> None:
        st.header("Visualizar Notificações")

        aluno_matricula = st.session_state["user_matricula"]
        notificacoes = View.notificacao_get_aluno_matricula(aluno_matricula)

        if len(notificacoes) > 0:
            for notif in notificacoes:
                st.divider()
                st.subheader(f"Notificação {notif.get_id()}")
                st.subheader(notif.get_titulo())
                st.text(notif.get_conteudo() if notif.get_conteudo() is not None else "(Sem Conteúdo)")
        else:
            st.divider()
            st.info("Nenhuma Notificação Encontrada para Você.")
