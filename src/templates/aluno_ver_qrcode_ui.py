import streamlit as st
from views import View

class AlunoVerQRCodeUI:
    @staticmethod
    def main() -> None:
        st.header("Ver QR-Code")
        
        aluno_matricula = st.session_state["user_matricula"]
        
        img = View.gerar_qrcode(aluno_matricula)

        st.image(img)

        st.text("O QR-Code só contém a matrícula que você está utilizando.")
