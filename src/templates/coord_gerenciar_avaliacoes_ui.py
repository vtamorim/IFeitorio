import streamlit as st
from views import View
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
        refeicoes = View.refeicao_get_all()
        refeicao_selecionada = st.selectbox("Selecione uma Refeição", refeicoes)
        
        if refeicao_selecionada:
            avaliacoes = View.avaliacao_get_refeicao_id(refeicao_selecionada.get_id())

            for avaliacao in avaliacoes:
                st.divider()
                st.subheader(avaliacao)
                st.feedback("stars", key=f"rating_{avaliacao.get_id()}", default=avaliacao.get_nota(), disabled=True)
                titulo = avaliacao.get_titulo()
                titulo = titulo if titulo is not None else "(Sem Título)"
                conteudo = avaliacao.get_conteudo()
                conteudo = conteudo if conteudo is not None else "(Sem Conteúdo)"
                st.subheader(titulo)
                st.text(conteudo)
            
            if len(avaliacoes) <= 0:
                st.warning("Nenhuma Avaliação desta Refeição Encontrada.")

    @staticmethod
    def deletar_avaliacao() -> None:
        avaliacoes = View.avaliacao_get_all()
        avaliacao_selecionada = st.selectbox("Avaliação", avaliacoes)
        if not avaliacao_selecionada:
            st.warning("Nenhuma Avaliação Encontrada!")
            return
        
        deletar = st.button("Deletar")

        if deletar:
            try:
                View.avaliacao_delete(avaliacao_selecionada.get_id())
                st.success("Avaliação Deletada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")
            
            sleep(1)
            st.rerun()
