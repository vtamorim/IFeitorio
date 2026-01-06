import pandas as pd
import streamlit as st
from datetime import date
from time import sleep

class CoordenadorGerenciarJustificativasUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Justificativas de Faltas")

        tab1, tab2, tab3 = st.tabs([ "Ver não Analisadas", "Ver Analisadas", "Analisar" ])

        with tab1: CoordenadorGerenciarJustificativasUI.ver_nao_analisadas_justificativas()
        with tab2: CoordenadorGerenciarJustificativasUI.ver_analisadas_justificativas()
        with tab3: CoordenadorGerenciarJustificativasUI.analisar_justificativa()

    @staticmethod
    def ver_nao_analisadas_justificativas() -> None:
        just_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "falta_id": [ "213", "512", "647" ],
                "motivo": [ "Alguma razao", "Dormi demais", "Porque eu quis" ]
            }
        )
        st.dataframe(just_dataframe, hide_index=True)

    @staticmethod
    def ver_analisadas_justificativas() -> None:
        just_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "falta_id": [ "213", "512", "647" ],
                "motivo": [ "Alguma razao", "Dormi demais", "Porque eu quis" ],
                "aprovacao": [ "não", "sim", "não" ]
            } # É meio desnecessário armazenas o coordenador que executou a aprovação...
        )
        st.dataframe(just_dataframe, hide_index=True)
    
    @staticmethod
    def analisar_justificativa() -> None:
        justificativa = st.selectbox("Selecionar Justificativa", [ "Justificativa 1", "Justificativa 4", "Justificativa 7" ])
        st.text_input("Aluno", "Aluno 1", disabled=True)
        st.text_input("Cardápio", "Cardápio 231", disabled=True)
        st.date_input("Data", date(2026, 1, 4), disabled=True)
        st.text_input("Tipo", "Almoço", disabled=True)
        st.text_area("Motivo", "Lorem ipsum dolor amet", disabled=True)
        aprovacao = st.checkbox("Aprovar Justificativa")
        analisar = st.button("Analisar")

        if analisar:
            st.success("Justificativa Analisada com Sucesso!")

            sleep(1)
            st.rerun()
