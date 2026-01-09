import pandas as pd
import streamlit as st
from views import View
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
        refeicoes = View.refeicao_get_all()
        refeicoes_data = [ [ r.get_id(), r.get_nome(), r.get_descricao(), len(r.get_restricoes_compativeis()) ] for r in refeicoes ]
        refeicoes_dataframe = pd.DataFrame(refeicoes_data, columns=["id", "nome", "descricao", "quant_restricoes"])
        
        st.dataframe(refeicoes_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_refeicao() -> None:
        restricoes = View.restricao_get_all()
        
        nome = st.text_input("Nome da Refeição")
        descricao = st.text_input("Descrição da Refeição (Opcional)")
        restricoes_selecionadas = st.multiselect("Restrições Compatíveis da Refeição", restricoes, key="restricoes_adicionadas")
        adicionar = st.button("Adicionar")

        if adicionar:
            try:
                View.refeicao_add(nome, descricao, restricoes_selecionadas)
                st.success("Refeição Adicionada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_refeicao() -> None:
        refeicoes = View.refeicao_get_all()
        restricoes = View.restricao_get_all()
        refeicao_selecionada = st.selectbox("Refeição", refeicoes, key="refeicao_atualizada")

        if refeicao_selecionada:
            nome = st.text_input("Novo Nome da Refeição", refeicao_selecionada.get_nome())
            descricao = st.text_input("Nova Descrição da Refeição (Opcional)", refeicao_selecionada.get_descricao())
            if len(refeicao_selecionada.get_restricoes_compativeis()) > 0:
                st.text(f"Restrições Alimentares Compatíveis Originais:")
                for r in refeicao_selecionada.get_restricoes_compativeis():
                    st.text(f"- {r}")
            restricoes_selecionadas = st.multiselect("Novas Restrições Compatíveis da Refeição", restricoes, key="restricoes_atualizadas")
            atualizar = st.button("Atualizar")

            if atualizar:
                try:
                    View.refeicao_update(refeicao_selecionada.get_id(), nome, descricao, restricoes_selecionadas)
                    st.success("Refeição Atualizada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
        else:
            st.warning("Nenhuma Refeição Encontrada.")
    
    @staticmethod
    def deletar_refeicao() -> None:
        refeicoes = View.refeicao_get_all()
        refeicao_selecionada = st.selectbox("Refeição", refeicoes, key="refeicao_deletada")
        
        if refeicao_selecionada:
            deletar = st.button("Deletar")

            if deletar:
                try:
                    View.refeicao_delete(refeicao_selecionada.get_id())
                    st.success("Refeição Deletada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
        else:
            st.warning("Nenhuma Refeição Encontrada.")
