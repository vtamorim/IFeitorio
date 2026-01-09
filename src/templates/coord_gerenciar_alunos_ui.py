import pandas as pd
import streamlit as st
from views import View
from time import sleep

class CoordenadorGerenciarAlunosUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Alunos")

        tab1, tab2, tab3, tab4 = st.tabs([ "Visualizar", "Adicionar", "Atualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarAlunosUI.visualizar_alunos()
        with tab2: CoordenadorGerenciarAlunosUI.adicionar_aluno()
        with tab3: CoordenadorGerenciarAlunosUI.atualizar_aluno()
        with tab4: CoordenadorGerenciarAlunosUI.deletar_aluno()
    
    @staticmethod
    def visualizar_alunos() -> None:
        alunos = View.aluno_get_all()
        alunos_data = [ [ a.get_matricula(), a.get_nome(), a.get_senha(), len(a.get_restricoes()) ] for a in alunos ]
        alunos_dataframe = pd.DataFrame(alunos_data, columns=[ "matricula", "nome", "senha", "quant_restricoes" ])
        
        st.dataframe(alunos_dataframe, hide_index=True)
    
    @staticmethod
    def adicionar_aluno() -> None:
        restricoes = View.restricao_get_all()
        
        matricula = st.text_input("Matrícula do Aluno")
        nome = st.text_input("Nome do Aluno")
        senha = st.text_input("Senha do Aluno")
        restricoes = st.multiselect("Restrições Alimentares do Aluno", restricoes)
        adicionar = st.button("Adicionar")

        if adicionar:
            try:
                View.aluno_add(matricula, nome, senha, restricoes)
                st.success("Aluno Adicionado com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_aluno() -> None:
        alunos = View.aluno_get_all()
        restricoes = View.restricao_get_all()
        
        aluno = st.selectbox("Aluno Selecionado", alunos)
        if aluno:
            matricula = st.text_input("Matrícula do Aluno", aluno.get_matricula(), disabled=True)
            nome = st.text_input("Nome do Aluno", aluno.get_nome())
            senha = st.text_input("Senha do Aluno", aluno.get_senha())
            if len(aluno.get_restricoes()) > 0:
                st.text("Restrições Alimentares Originais:")
                for r in aluno.get_restricoes():
                    st.text(f"- {r}")
            restricoes_selecionadas = st.multiselect("Restrições Alimentares do Aluno", restricoes, key="restricoes_atualizadas")
            atualizar = st.button("Atualizar")

            if atualizar:
                try:
                    View.aluno_update(matricula, nome, senha, restricoes_selecionadas)
                    st.success("Aluno Atualizado com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
    
    @staticmethod
    def deletar_aluno() -> None:
        alunos = View.aluno_get_all()
        aluno = st.selectbox("Aluno Selecionado", alunos, key="aluno_deletado")
        deletar = st.button("Deletar")

        if deletar:
            try:
                View.aluno_delete(aluno.get_matricula())
                st.success("Aluno Deletado com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
