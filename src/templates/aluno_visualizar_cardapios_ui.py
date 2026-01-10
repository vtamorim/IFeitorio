import pandas as pd
import streamlit as st
from views import View

class AlunoVisualizarCardapiosUI:
    """Página do Aluno visualizar os cardápios."""
    @staticmethod
    def main() -> None:
        st.set_page_config(layout="wide")
        st.header("Visualizar Cardápios")

        cardapios = sorted(View.cardapio_get_all(), reverse=True, key=lambda c: c.get_data_inicial())
        weekdays = {
            0: "Segunda",
            1: "Terça",
            2: "Quarta",
            3: "Quinta",
            4: "Sexta"
        }

        for cardapio in cardapios:
            card_refeicoes = cardapio.get_refeicoes()
            refeicoes_horarios = {
                "lanche_manha": [],
                "lanche_tarde": [],
                "lanche_noite": [],
                "almoco": [],
                "jantar": []
            }
            dias_intermediarios = View.calc_dias_intermediarios(cardapio.get_data_inicial(), cardapio.get_data_final())
            for ref in card_refeicoes:
                tipo = ref.get_tipo()
                refeicoes_horarios[tipo].append(ref)
            
            st.divider()
            st.title(cardapio)

            st.subheader("Cardápio do Lanche")
            lanche_dia_tipo = { di : { "manha": [], "tarde": [], "noite": [] } for di in dias_intermediarios }
            for l_m in refeicoes_horarios["lanche_manha"]:
                lanche_dia_tipo[l_m.get_data()]["manha"].append(l_m)
            for l_t in refeicoes_horarios["lanche_tarde"]:
                lanche_dia_tipo[l_t.get_data()]["tarde"].append(l_t)
            for l_n in refeicoes_horarios["lanche_noite"]:
                lanche_dia_tipo[l_n.get_data()]["noite"].append(l_n)
        
            lanche_data = {}
            for di in lanche_dia_tipo.keys():
                lanche_data_key = f"{cardapio.get_data_formatada(di)} - {weekdays[di.weekday()]}"
                lanche_data[lanche_data_key] = []
                for refeicoes in lanche_dia_tipo[di].values():
                    lanche_data[lanche_data_key].append(" + ".join([ r.get_nome() for r in refeicoes ]))
            
            lanche_df = pd.DataFrame(lanche_data, index=["Manhã", "Tarde", "Noite"])
            st.dataframe(lanche_df)

            st.subheader("Cardápio do Almoço")
            almoco_dia = { di : [] for di in dias_intermediarios }
            for al in refeicoes_horarios["almoco"]:
                almoco_dia[al.get_data()].append(al)
            max_almoco_refeicoes = max(len(i) for i in almoco_dia.values())

            almoco_data: dict[str, list[str]] = {}
            for di in almoco_dia.keys():
                almoco_data_key = f"{cardapio.get_data_formatada(di)} - {weekdays[di.weekday()]}"
                almoco_data[almoco_data_key] = []
                for refeicoes in almoco_dia[di]:
                    almoco_data[almoco_data_key].append(refeicoes.get_nome())
                for _ in range(max_almoco_refeicoes - len(almoco_dia[di])):
                    almoco_data[almoco_data_key].append("")
        
            almoco_df = pd.DataFrame(almoco_data)
            st.dataframe(almoco_df, hide_index=True)

            st.subheader("Cardápio do Jantar")
            jantar_dia = { di : [] for di in dias_intermediarios }
            for ja in refeicoes_horarios["jantar"]:
                jantar_dia[ja.get_data()].append(ja)
            max_jantar_refeicoes = max(len(i) for i in jantar_dia.values())

            jantar_data: dict[str, list[str]] = {}
            for di in jantar_dia.keys():
                jantar_data_key = f"{cardapio.get_data_formatada(di)} - {weekdays[di.weekday()]}"
                jantar_data[jantar_data_key] = []
                for refeicoes in jantar_dia[di]:
                    jantar_data[jantar_data_key].append(refeicoes.get_nome())
                for _ in range(max_jantar_refeicoes - len(jantar_dia[di])):
                    jantar_data[jantar_data_key].append("")
        
            jantar_df = pd.DataFrame(jantar_data)
            st.dataframe(jantar_df, hide_index=True)
    
        if len(cardapios) <= 0:
            st.warning("Nenhum Cardápio Encontrado!")
