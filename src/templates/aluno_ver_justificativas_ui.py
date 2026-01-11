import pandas as pd
import streamlit as st
from views import View

class AlunoVerJustificativasUI:
    @staticmethod
    def main() -> None:
        st.header("Ver Justificativas de Falta")
        
        aluno_matricula = st.session_state["user_matricula"]
        justificativas = View.justificativa_get_aluno_matricula(aluno_matricula)

        if len(justificativas) <= 0:
            st.warning("Nenhuma Justificativa Encontrada!")
            return
        
        just_data = []
        for j in justificativas:
            aprovacao = j.get_aprovada()
            if aprovacao is not None:
                aprovacao = "Sim" if aprovacao else "Não"
            else:
                aprovacao = "Não Verificado"
            just_data.append([ j.get_id(), str(j.get_falta()), j.get_motivo(), aprovacao ])

        just_dataframe = pd.DataFrame(just_data, columns=["id", "falta", "motivo", "aprovacao"])
        st.dataframe(just_dataframe, hide_index=True)
