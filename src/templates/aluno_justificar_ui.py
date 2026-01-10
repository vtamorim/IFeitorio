import streamlit as st
from views import View
from time import sleep

class AlunoJustificarUI:
    """Página que permite o Aluno justificar suas faltas."""
    @staticmethod
    def main() -> None:
        st.header("Justificar Faltas")

        aluno_matricula = st.session_state["user_matricula"]
        faltas = View.falta_get_sem_justificativas(aluno_matricula)

        falta_escolhida = st.selectbox("Selecione uma Falta", faltas)

        if falta_escolhida:
            motivo = st.text_area("Motivo da Falta", placeholder="Explique a razão da Falta")
            justificar = st.button("Justificar")

            if justificar:
                try:
                    View.justificativa_add(falta_escolhida, motivo)
                    st.success("Falta Justificada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
        else:
            st.warning("Nenhuma Falta Encontrada!")