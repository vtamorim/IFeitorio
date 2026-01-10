import streamlit as st
from views import View
from time import sleep

class AlunoAvaliarRefeicaoUI:
    """Página do Aluno que exibirá as avaliações de uma refeição específica, assim como realizará a avaliação do Aluno."""
    @staticmethod
    def main() -> None:
        st.header("Analisar Refeição")

        aluno_matricula = st.session_state["user_matricula"]
        aluno = View.aluno_get_matricula(aluno_matricula)

        restricoes = View.restricao_get_all()
        refeicoes = View.refeicao_get_all()
        refeicao_escolhida = st.selectbox("Selecione uma Refeição", refeicoes)

        if refeicao_escolhida:
            avaliacoes = View.avaliacao_get_refeicao_id(refeicao_escolhida.get_id())
            
            st.divider()
            st.title("Informações da Refeição")
            
            if len(avaliacoes) > 0: # Se tiver avaliações, mostrar a nota média delas
                nota_media = round(sum([ av.get_nota() for av in avaliacoes ]) / len(avaliacoes))
                st.text("Nota Média (0 - 5):")
                st.feedback("stars", key="mean_rating", default=nota_media, disabled=True)
            
            st.text_input("Nome da Refeição", refeicao_escolhida.get_nome(), disabled=True)
            st.text_area("Descrição da Refeição", refeicao_escolhida.get_descricao(), disabled=True)
            st.multiselect("Restrições Compatíveis da Refeição", restricoes, refeicao_escolhida.get_restricoes_compativeis(), disabled=True)
            
            st.divider()
            st.title(f"Avaliar {refeicao_escolhida.get_nome()}")

            avaliacao_feita = None
            nota_padrao = 4
            titulo_padrao = ""
            conteudo_padrao = ""
            enviar = False
            atualizar = False
            for av in avaliacoes:
                if av.get_aluno().get_matricula() == aluno_matricula:
                    avaliacao_feita = av
                    nota_padrao = av.get_nota()
                    titulo_padrao = av.get_titulo()
                    conteudo_padrao = av.get_conteudo()
                    break

            nota = st.feedback("stars", default=nota_padrao)
            titulo = st.text_input("Título da Avaliação (Opcional)", titulo_padrao)
            conteudo = st.text_area("Conteúdo da Avaliação (Opcional)", conteudo_padrao)
            if avaliacao_feita:
                atualizar = st.button("Atualizar")
            else:
                enviar = st.button("Enviar")

            if enviar:
                try:
                    View.avaliacao_add(nota, aluno, refeicao_escolhida, conteudo, titulo)
                    st.success("Avaliação Enviada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
            if atualizar:
                try:
                    View.avaliacao_update(avaliacao_feita.get_id(), nota, aluno, refeicao_escolhida, conteudo, titulo)
                    st.success("Avaliação Atualizada com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
            
            st.divider()
            st.title("Avaliações de Outros Usuários")

            if len(avaliacoes) > 0:
                for i, av in enumerate(avaliacoes):
                    st.divider()
                    st.subheader(av.get_aluno().get_nome())
                    st.feedback("stars", key=f"rating_{i}", default=av.get_nota(), disabled=True)
                    titulo = av.get_titulo() if av.get_titulo() is not None else "(Sem Título)"
                    conteudo = av.get_conteudo() if av.get_conteudo() is not None else "(Sem Conteúdo)"
                    st.text_input("Título", titulo, disabled=True, key=f"title_{i}")
                    st.text_area("Conteúdo", conteudo, disabled=True, key=f"content_{i}")
            else:
                st.divider()
                st.info("Nenhuma Avaliação dessa Refeição Encontrada.")
        else:
            st.warning("Nenhuma Refeição Encontrada!")
