import streamlit as st
from time import sleep

class AlunoJustificarUI:
    """Página que permite o Aluno justificar suas faltas."""
    @staticmethod
    def main() -> None:
        st.header("Justificar Faltas")

        faltas = [ "Falta 378 - Cardápio 9 - Pão com Ovos", "Falta 521 - Cardápio 12 - Pão com Queijo" ]

        falta_escolhida = st.selectbox("Selecione uma Falta", faltas)

        if falta_escolhida:
            motivo = st.text_area("Motivo da Falta", placeholder="Motivo da Falta")
            enviar = st.button("Enviar")

            if enviar:
                st.success("Falta Justificada com Sucesso!")

                sleep(1)
                st.rerun()