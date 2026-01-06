import pandas as pd
import streamlit as st
from time import sleep

class CoordenadorGerenciarFaltasUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Faltas")

        tab1, tab2, tab3 = st.tabs([ "Visualizar", "Adicionar", "Deletar" ])

        with tab1: CoordenadorGerenciarFaltasUI.visualizar_faltas()
        with tab2: CoordenadorGerenciarFaltasUI.adicionar_faltas()
        with tab3: CoordenadorGerenciarFaltasUI.deletar_faltas()

    @staticmethod
    def visualizar_faltas() -> None:
        faltas_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "aluno_matricula": [ "219845921", "52817152", "12852012" ],
                "cardapio_id": [ "212", "251", "317" ],
                "data": [ "12/09/2025", "31/02/2026", "23/08/2026" ],
                "tipo": [ "almoço", "almoço", "janta" ]
            }
        )
        st.dataframe(faltas_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_faltas() -> None:
        cardapio = st.selectbox("Selecionar Cardápio", [ "Cardápio 1 - 12/09/2025 - 16/09/2025", "Cardápio 2 - 18/09/2025 - 22/09/2025" ])
        data = st.selectbox("Selecionar Data no Cardápio", [ f"{i}/09/2025" for i in range(12, 17) ])
        tipo = st.selectbox("Selecionar Tipo de Refeição", [ "Almoço", "Jantar" ])
        aluno = st.selectbox("Selecionar Aluno", [ "Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4", "Aluno 5" ])
        adicionar = st.button("Adicionar")

        if adicionar:
            st.success("Notificação Atualizada com Sucesso!")

            sleep(1)
            st.rerun()

    @staticmethod
    def deletar_faltas() -> None:
        falta = st.selectbox("Falta", [ "Falta 2", "Falta 5", "Falta 7" ])
        deletar = st.button("Deletar")

        if deletar:
            st.success("Falta Deletada com Sucesso!")
            
            sleep(1)
            st.rerun()
