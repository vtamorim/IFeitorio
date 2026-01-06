import pandas as pd
import streamlit as st
from time import sleep

class CoordenadorGerenciarNotificacoesUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Notificações")

        tab1, tab2, tab3, tab4 = st.tabs([ "Visualizar", "Enviar", "Atualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarNotificacoesUI.visualizar_notificacoes()
        with tab2: CoordenadorGerenciarNotificacoesUI.enviar_notificacao()
        with tab3: CoordenadorGerenciarNotificacoesUI.atualizar_notificacao()
        with tab4: CoordenadorGerenciarNotificacoesUI.deletar_notificacao()

    @staticmethod
    def visualizar_notificacoes() -> None:
        notif_dataframe = pd.DataFrame(
            {
                "id": [ "1", "2", "3" ],
                "titulo": [ "Hello World", "Alguma coisa teste", "Mudança no Cardápio 231" ],
                "conteudo": [ "lorem ipsum dolor amet", "", "Bolo foi adicionado no dia 31/02/2026" ],
                "quant_alunos": [ "1", "4", "23" ]
            }
        )
        st.dataframe(notif_dataframe, hide_index=True)

    @staticmethod
    def enviar_notificacao() -> None:
        titulo = st.text_input("Título")
        conteudo = st.text_area("Conteúdo")
        todos_os_alunos = st.button("Selecionar todos os Alunos", type="tertiary", key="selecionar_enviar")
        alunos = st.multiselect("Alunos Destinatários", [ "Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4", "Aluno 5" ])
        enviar = st.button("Enviar")

        if enviar:
            st.success("Notificação Enviada com Sucesso!")

            sleep(1)
            st.rerun()

    @staticmethod
    def atualizar_notificacao() -> None:
        notificacao_selecionada = st.selectbox("Notificação", [ "Notificação 512", "Notificação 262", "Notificação 126" ], key="notif_atualizar")
        titulo = st.text_input("Novo Título")
        conteudo = st.text_area("Novo Conteúdo")
        todos_os_alunos = st.button("Selecionar todos os Alunos", type="tertiary", key="selecionar_atualizar")
        alunos = st.multiselect("Novos Alunos Destinatários", [ "Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4", "Aluno 5" ])
        atualizar = st.button("Atualizar")

        if atualizar:
            st.success("Notificação Atualizada com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def deletar_notificacao() -> None:
        notificacao_selecionada = st.selectbox("Notificação", [ "Notificação 512", "Notificação 262", "Notificação 126" ], key="notif_deletar")
        deletar = st.button("Deletar")

        if deletar:
            st.success("Notificação Deletada com Sucesso!")

            sleep(1)
            st.rerun()
