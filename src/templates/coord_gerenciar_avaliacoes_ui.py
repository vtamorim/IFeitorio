import streamlit as st
from time import sleep

class CoordenadorGerenciarAvaliacoesUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Avaliações")

        tab1, tab2 = st.tabs([ "Visualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarAvaliacoesUI.visualizar_avaliacoes()
        with tab2: CoordenadorGerenciarAvaliacoesUI.deletar_avaliacao()
    
    @staticmethod
    def visualizar_avaliacoes() -> None:
        refeicao_selecionada = st.selectbox("Selecione uma Refeição", [ "Pão com Ovos", "Pão com Queijo", "Bolo de Chocolate" ])
        
        st.divider()
        st.subheader("Avaliação 231 - Aluno 1")
        st.feedback("stars", key="rating_1", default=2, disabled=True)
        st.subheader("Está sempre sem sal...")
        st.text("Todas as vezes que é servido não está salgado o suficiente.")

        st.divider()
        st.subheader("Avaliação 531 - Aluno 2")
        st.feedback("stars", key="rating_2", default=4, disabled=True)
        st.subheader("(Sem Título)")
        st.text("Muito bom.")

        st.divider()
        st.subheader("Avaliação 12 - Aluno 3")
        st.feedback("stars", key="rating_3", default=1, disabled=True)
        st.subheader("(Sem Título)")
        st.text("(Sem conteúdo)")

    @staticmethod
    def deletar_avaliacao() -> None:
        avaliacao_selecionada = st.selectbox("Avaliação", [ "Avaliação 231", "Avaliação 531", "Avaliação 12" ])
        deletar = st.button("Deletar")

        if deletar:
            st.success("Avaliação Deletada com Sucesso!")
            
            sleep(1)
            st.rerun()
