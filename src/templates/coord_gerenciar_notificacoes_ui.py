import pandas as pd
import streamlit as st
from views import View
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
        notificacoes = View.notificacao_get_all()
        notif_data = [
            [
                n.get_id(), 
                n.get_titulo(), 
                n.get_conteudo() if n.get_conteudo() is not None else "", 
                len(n.get_alunos_destinatarios())
            ] 
            for n in notificacoes
        ]
        
        notif_dataframe = pd.DataFrame(notif_data, columns=["id", "titulo", "conteudo", "quant_alunos"])
        st.dataframe(notif_dataframe, hide_index=True)

    @staticmethod
    def enviar_notificacao() -> None:
        alunos = View.aluno_get_all()
        
        titulo = st.text_input("Título")
        conteudo = st.text_area("Conteúdo (Opcional)")

        todos_os_alunos = st.button("Selecionar todos os Alunos", type="tertiary", key="selecionar_enviar")
        if "alunos_enviar" not in st.session_state:
            st.session_state.alunos_enviar = []
        if todos_os_alunos:
            st.session_state.alunos_enviar = [ a.get_matricula() for a in alunos ]
        
        alunos_selecionados = st.multiselect(
            "Alunos Destinatários", 
            [ a.get_matricula() for a in alunos ], 
            format_func=lambda m: next((str(a) for a in alunos if a.get_matricula() == m), ""), 
            key="alunos_enviar"
        )
        enviar = st.button("Enviar")

        if enviar:
            alunos_selecionados = [ a for a in alunos if a.get_matricula() in alunos_selecionados ]
            try:
                View.notificacao_add(titulo, conteudo, alunos_selecionados)
                st.success("Notificação Enviada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()

    @staticmethod
    def atualizar_notificacao() -> None:
        alunos = View.aluno_get_all()
        notificacoes = View.notificacao_get_all()
        notificacao_selecionada = st.selectbox("Notificação", notificacoes, key="notif_atualizar")
        if not notificacao_selecionada:
            st.warning("Nenhuma Notificação Encontrada!")
            return

        titulo = st.text_input("Novo Título", notificacao_selecionada.get_titulo())
        conteudo = st.text_area("Novo Conteúdo", notificacao_selecionada.get_conteudo())

        todos_os_alunos = st.button("Selecionar todos os Alunos", type="tertiary", key="selecionar_atualizar")
        if "alunos_atualizar" not in st.session_state:
            st.session_state.alunos_atualizar = []
        if todos_os_alunos:
            st.session_state.alunos_atualizar = [ a.get_matricula() for a in alunos ]
        
        alunos_selecionados = st.multiselect(
            "Alunos Destinatários", 
            [ a.get_matricula() for a in alunos ], 
            format_func=lambda m: next((str(a) for a in alunos if a.get_matricula() == m), ""), 
            key="alunos_atualizar"
        )

        atualizar = st.button("Atualizar")

        if atualizar:
            alunos_selecionados = [ a for a in alunos if a.get_matricula() in alunos_selecionados ]
            try:
                View.notificacao_update(notificacao_selecionada.get_id(), titulo, conteudo, alunos_selecionados)
                st.success("Notificação Atualizada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def deletar_notificacao() -> None:
        notificacoes = View.notificacao_get_all()
        notificacao_selecionada = st.selectbox("Notificação", notificacoes, key="notif_deletar")
        if not notificacao_selecionada:
            st.warning("Nenhuma Notificação Encontrada!")
            return

        deletar = st.button("Deletar")

        if deletar:
            try:
                View.notificacao_delete(notificacao_selecionada.get_id())
                st.success("Notificação Deletada com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
