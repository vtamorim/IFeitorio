import pandas as pd
import streamlit as st
from time import sleep

class CoordenadorGerenciarCardapiosUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Cardápios")

        tab1, tab2, tab3, tab4 = st.tabs([ "Visualizar", "Adicionar", "Atualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarCardapiosUI.visualizar_cardapios()
        with tab2: CoordenadorGerenciarCardapiosUI.adicionar_cardapio()
        with tab3: CoordenadorGerenciarCardapiosUI.atualizar_cardapio()
        with tab4: CoordenadorGerenciarCardapiosUI.deletar_cardapio()
    
    @staticmethod
    def visualizar_cardapios() -> None:
        cardapios_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "data_inicial": [ "12/09/2025", "18/09/2025", "22/09/2025" ],
                "data_final": [ "16/09/2025", "20/09/2025", "27/09/2025" ]
            }
        )
        
        st.dataframe(cardapios_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_cardapio() -> None:
        data_inicial = st.date_input("Data Inicial")
        data_final = st.date_input("Data Final")
        # Fazer depois o sistema de gerenciar as refeições dos cardápios
        adicionar = st.button("Adicionar")

        if adicionar:
            st.success("Cardápio Adicionado com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_cardapio() -> None:
        cardapio_selecionado = st.selectbox("Cardápio Escolhido", [ "Cardápio 1 - 12/09/2025 - 16/09/2025", "Cardápio 2 - 18/09/2025 - 22/09/2025" ], key="cardapio_atualizado")
        data_inicial = st.date_input("Nova Data Inicial")
        data_final = st.date_input("Nova Data Final")
        # Fazer depois o sistema de gerenciar as refeições dos cardápios
        atualizar = st.button("Atualizar")

        if atualizar:
            st.success("Cardápio Atualizado com Sucesso!")

            sleep(1)
            st.rerun()
     
    @staticmethod
    def deletar_cardapio() -> None:
 
        cardapio_selecionado = st.selectbox("Cardápio Escolhido", [ "Cardápio 1 - 12/09/2025 - 16/09/2025", "Cardápio 2 - 18/09/2025 - 22/09/2025" ], key="cardapio_deletado")
        deletar = st.button("Deletar")

        if deletar:
            st.success("Cardápio Deletado com Sucesso!")

            sleep(1)
            st.rerun()
