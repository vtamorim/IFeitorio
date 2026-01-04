import streamlit as st
from time import sleep

class AlunoAvaliarRefeicaoUI:
    """Página do Aluno que exibirá as avaliações de uma refeição específica, assim como realizará a avaliação do Aluno."""
    @staticmethod
    def main() -> None:
        st.header("Analisar Refeição")

        refeicoes = [ "Pão com Ovo", "Pão com Queijo", "Bolo de Chocolate" ]

        refeicao_escolhida = st.selectbox("Selecione uma Refeição", refeicoes)

        if refeicao_escolhida:
            st.divider()
            st.text("Nota Média (0 - 5):")
            st.feedback("stars", key="mean_rating", default=3, disabled=True)
            
            st.divider()
            st.title(f"Avaliar {refeicao_escolhida}")
            st.divider()

            nota = st.feedback("stars")
            titulo = st.text_input("Título da Avaliação (Opcional)")
            conteudo = st.text_area("Conteúdo da Avaliação (Opcional)")
            enviar = st.button("Enviar")

            if enviar:
                st.success("Avaliação Enviada com Sucesso!")

                sleep(1)
                st.rerun()
            
            st.divider()
            st.title("Avaliações de Outros Usuários")

            st.divider()
            st.text("Aluno 1")
            st.feedback("stars", key="rating_1", default=2, disabled=True)
            st.subheader("Está sempre sem sal...")
            st.text("Todas as vezes que é servido não está salgado o suficiente.")

            st.divider()
            st.text("Aluno 2")
            st.feedback("stars", key="rating_2", default=4, disabled=True)
            st.subheader("(Sem Título)")
            st.text("Muito bom.")

            st.divider()
            st.text("Aluno 3")
            st.feedback("stars", key="rating_3", default=1, disabled=True)
            st.subheader("(Sem Título)")
            st.text("(Sem conteúdo)")
