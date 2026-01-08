import pandas as pd
import streamlit as st
from views import View
from time import sleep

class CoordenadorGerenciarRestricoesUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Restrições Alimentares")

        tab1, tab2, tab3, tab4 = st.tabs([ "Visualizar", "Adicionar", "Atualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarRestricoesUI.visualizar_restricoes()
        with tab2: CoordenadorGerenciarRestricoesUI.adicionar_restricao()
        with tab3: CoordenadorGerenciarRestricoesUI.atualizar_restricao()
        with tab4: CoordenadorGerenciarRestricoesUI.deletar_restricao()
    
    @staticmethod
    def visualizar_restricoes() -> None:
        restricoes = View.restricao_get_all()
        restricoes_data = [ [ r.get_id(), r.get_nome() ] for r in restricoes ]
        restricoes_dataframe = pd.DataFrame(restricoes_data, columns=["id", "nome"])
        
        st.dataframe(restricoes_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_restricao() -> None:
        nome = st.text_input("Nome da Restrição")
        adicionar = st.button("Adicionar")

        if adicionar:
            try:
                View.restricao_add(nome)
                st.success("Restrição Adicionada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_restricao() -> None:
        restricoes = View.restricao_get_all()
        restricao_selecionada = st.selectbox("Restrição", restricoes, key="restricao_atualizada")

        if restricao_selecionada:
            nome = st.text_input("Novo Nome da Restrição")
            atualizar = st.button("Atualizar")

            if atualizar:
                try:
                    View.restricao_update(restricao_selecionada.get_id(), nome)
                    st.success("Restrição Atualizada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
        else:
            st.warning("Nenhuma Restrição Encontrada.")
    
    @staticmethod
    def deletar_restricao() -> None:
        restricoes = View.restricao_get_all()
        restricao_selecionada = st.selectbox("Restrição", restricoes, key="restricao_deletada")

        if restricao_selecionada:
            deletar = st.button("Deletar")

            if deletar:
                try:
                    View.restricao_delete(restricao_selecionada.get_id())
                    st.success("Restrição Deletada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
        else:
            st.warning("Nenhuma Restrição Encontrada.")
