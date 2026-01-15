import pandas as pd
import streamlit as st
from views import View
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
        faltas = View.falta_get_all()
        if len(faltas) <= 0:
            st.warning("Nenhuma Falta Encontrada!")
            return
        
        faltas_data = [ [ f.get_id(), f.get_aluno().get_matricula(), f.get_cardapio().get_id(), f.get_data_formatada(), f.get_tipo() ] for f in faltas ]
        faltas_dataframe = pd.DataFrame(faltas_data, columns=["id", "aluno_matricula", "cardapio_id", "data", "tipo"])
        st.dataframe(faltas_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_faltas() -> None:
        alunos = View.aluno_get_all()
        cardapios = View.cardapio_get_all()
        cardapio = st.selectbox("Selecionar Cardápio", cardapios)
        if not cardapio:
            st.warning("Nenhum Cardápio Encontrado!")
            return
        
        cardapio_datas = View.calc_dias_intermediarios(cardapio.get_data_inicial(), cardapio.get_data_final())
        
        data = st.selectbox("Selecionar Data no Cardápio", cardapio_datas, format_func=lambda cd: cardapio.get_data_formatada(cd))
        tipo = st.selectbox("Selecionar Tipo de Refeição", [ "Almoço", "Jantar" ])
        aluno = st.selectbox("Selecionar Aluno", alunos)
        adicionar = st.button("Adicionar")

        if adicionar:
            try:
                View.falta_add(aluno, cardapio, data, tipo)

                notif_titulo = "Falta Adicionada"
                notif_conteudo = f"Uma falta no Cardápio {cardapio.get_id()} - {cardapio.get_data_formatada(data)} no {tipo} foi cadastrada em seu nome."
                View.notificacao_add(notif_titulo, notif_conteudo, [ aluno ])
                
                st.success("Falta Adicionada com Sucesso! Aluno notificado.")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()

    @staticmethod
    def deletar_faltas() -> None:
        faltas = View.falta_get_all()
        falta = st.selectbox("Escolha uma Falta", faltas)
        if not falta:
            st.warning("Nenhuma Falta Encontrada!")
            return
        
        deletar = st.button("Deletar")

        if deletar:
            try:
                View.falta_delete(falta.get_id())

                notif_titulo = "Falta Removida"
                notif_conteudo = f"A Falta {falta.get_id()} foi removida do seu nome."
                View.notificacao_add(notif_titulo, notif_conteudo, [ falta.get_aluno() ])

                st.success("Falta Deletada com Sucesso! Aluno notificado.")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")
            
            sleep(1)
            st.rerun()
