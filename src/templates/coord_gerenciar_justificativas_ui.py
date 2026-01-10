import pandas as pd
import streamlit as st
from views import View
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
        justificativas = [ j for j in View.justificativa_get_all() if j.get_aprovada() is None ]
        just_data = [ [ j.get_id(), j.get_falta().get_id(), j.get_motivo() ] for j in justificativas ]
        just_dataframe = pd.DataFrame(just_data, columns=["id", "falta_id", "motivo"])
        st.dataframe(just_dataframe, hide_index=True)

    @staticmethod
    def ver_analisadas_justificativas() -> None:
        justificativas = [ j for j in View.justificativa_get_all() if j.get_aprovada() is not None ]
        just_data = [ [ j.get_id(), j.get_falta().get_id(), j.get_motivo(), "sim" if j.get_aprovada() else "não" ] for j in justificativas ]
        just_dataframe = pd.DataFrame(just_data, columns=["id", "falta_id", "motivo", "aprovacao"])
        st.dataframe(just_dataframe, hide_index=True)
    
    @staticmethod
    def analisar_justificativa() -> None:
        justificativas = [ j for j in View.justificativa_get_all() if j.get_aprovada() is None ]
        justificativa = st.selectbox("Selecionar Justificativa", justificativas)
        if not justificativa:
            st.warning("Nenhuma Justificativa Encontrada")
            return
        
        st.text_input("Aluno", justificativa.get_falta().get_aluno(), disabled=True)
        st.text_input("Cardápio", justificativa.get_falta().get_cardapio(), disabled=True)
        st.date_input("Data", justificativa.get_falta().get_data(), disabled=True)
        st.text_input("Tipo", justificativa.get_falta().get_tipo(), disabled=True)
        st.text_area("Motivo", justificativa.get_motivo(), disabled=True)
        aprovacao = st.checkbox("Aprovar Justificativa")
        analisar = st.button("Analisar")

        if analisar:
            try:
                View.justificativa_update(justificativa.get_id(), justificativa.get_falta(), justificativa.get_motivo(), aprovacao)
                st.success("Justificativa Analisada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
