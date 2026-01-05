import pandas as pd
import streamlit as st
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
        restricoes_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "nome": [ "Intolerância à Lactose", "Vegetariano", "Vegano" ]
            }
        )
        
        st.dataframe(restricoes_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_restricao() -> None:
        nome = st.text_input("Nome da Restrição")
        adicionar = st.button("Adicionar")

        if adicionar:
            st.success("Restrição Adicionada com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_restricao() -> None:
        restricao_selecionada = st.selectbox("Restrição", [ "1 - Intolerância à Lactose", "2 - Vegetariano", "3 - Vegano" ], key="restricao_atualizada")
        nome = st.text_input("Novo Nome da Restrição")
        atualizar = st.button("Atualizar")

        if atualizar:
            st.success("Restrição Atualizada com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def deletar_restricao() -> None:
        restricao_selecionada = st.selectbox("Restrição", [ "1 - Intolerância à Lactose", "2 - Vegetariano", "3 - Vegano" ], key="restricao_deletada")
        deletar = st.button("Deletar")

        if deletar:
            st.success("Restrição Deletada com Sucesso!")

            sleep(1)
            st.rerun()
