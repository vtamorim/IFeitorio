import pandas as pd
import streamlit as st
from time import sleep

class CoordenadorGerenciarRefeicoesUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Refeições")

        tab1, tab2, tab3, tab4 = st.tabs([ "Visualizar", "Adicionar", "Atualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarRefeicoesUI.visualizar_refeicoes()
        with tab2: CoordenadorGerenciarRefeicoesUI.adicionar_refeicao()
        with tab3: CoordenadorGerenciarRefeicoesUI.atualizar_refeicao()
        with tab4: CoordenadorGerenciarRefeicoesUI.deletar_refeicao()
    
    @staticmethod
    def visualizar_refeicoes() -> None:
        refeicoes_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "nome": [ "Pão com Ovos", "Pão com Queijo", "Bolo" ],
                "descricao": [ "", "", "" ],
                "restricoes": [ "", "", "" ]
            }
        )
        
        st.dataframe(refeicoes_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_refeicao() -> None:
        nome = st.text_input("Nome da Refeição")
        descricao = st.text_input("Descrição da Refeição")
        restricoes = st.multiselect("Restrições da Refeição", [ "1 - Intolerância à Lactose", "2 - Vegetariano", "3 - Vegano" ], key="restricoes_adicionadas")
        adicionar = st.button("Adicionar")

        if adicionar:
            st.success("Refeição Adicionada com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_refeicao() -> None:
        refeicao_selecionada = st.selectbox("Refeição", [ "1 - Pão com Ovos", "2 - Pão com Queijo", "3 - Bolo" ], key="refeicao_atualizada")
        nome = st.text_input("Novo Nome da Refeição")
        descricao = st.text_input("Nova Descrição da Refeição")
        restricoes = st.multiselect("Novas Restrições da Refeição", [ "1 - Intolerância à Lactose", "2 - Vegetariano", "3 - Vegano" ], key="restricoes_atualizadas")
        atualizar = st.button("Atualizar")

        if atualizar:
            st.success("Refeição Atualizada com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def deletar_refeicao() -> None:
        refeicao_selecionada = st.selectbox("Refeição", [ "1 - Pão com Ovos", "2 - Pão com Queijo", "3 - Bolo" ], key="refeicao_deletada")
        deletar = st.button("Deletar")

        if deletar:
            st.success("Refeição Deletada com Sucesso!")

            sleep(1)
            st.rerun()
