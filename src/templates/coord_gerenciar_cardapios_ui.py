import pandas as pd
import streamlit as st
from views import View
from datetime import date, timedelta
from time import sleep

class CoordenadorGerenciarCardapiosUI:
    @staticmethod
    def main() -> None:
        st.header("Gerenciar Cardápios")

        tab1, tab2, tab3, tab4 = st.tabs([ "Visualizar", "Adicionar", "Atualizar", "Deletar" ])

        with tab1: CoordenadorGerenciarCardapiosUI.visualizar_cardapios()
        with tab2: CoordenadorGerenciarCardapiosUI.adicionar_cardapio()
        with tab3: CoordenadorGerenciarCardapiosUI.atualizar_cardapio()
        with tab4: CoordenadorGerenciarCardapiosUI.deletar_cardapio()
    
    @staticmethod
    def visualizar_cardapios() -> None:
        cardapios = View.cardapio_get_all()
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
    
    @staticmethod
    def adicionar_cardapio() -> None:
        segunda_atual, sexta_atual = View.calc_dias_da_semana(date.today())
        gerar_refeicoes = View.refeicao_get_all # Guardamos a função ao invés dos objetos para evitar uns problemas de referência com os diversos "multiselect"

        data_inicial = st.date_input("Data Inicial", segunda_atual, format="DD/MM/YYYY")
        data_final = st.date_input("Data Final", sexta_atual, format="DD/MM/YYYY")
        
        if data_inicial and data_final:
            dif_dias = data_final - data_inicial
            quant_datas = dif_dias.days + 1

            for i in range(quant_datas):
                dia_atual = data_inicial + timedelta(days=i)

                st.divider()
                st.subheader(f'Data: {dia_atual.strftime("%d/%m/%Y")}')

                st.multiselect("Lanche", gerar_refeicoes(), key=f"lanche_adicionar_{i}")
                st.multiselect("Almoço", gerar_refeicoes(), key=f"almoco_adicionar_{i}")
                st.multiselect("Jantar", gerar_refeicoes(), key=f"jantar_adicionar_{i}")
            
            adicionar = st.button("Adicionar")

            if adicionar:
                try:
                    refeicoes = []
                    for i in range(quant_datas):
                        dia_atual = data_inicial + timedelta(days=i)
                        refs_lanche = st.session_state[f"lanche_adicionar_{i}"]
                        refs_almoco = st.session_state[f"almoco_adicionar_{i}"]
                        refs_janta = st.session_state[f"jantar_adicionar_{i}"]

                        for ref in refs_lanche:
                            ref.set_data(dia_atual)
                            ref.set_tipo("lanche")
                        for ref in refs_almoco:
                            ref.set_data(dia_atual)
                            ref.set_tipo("almoco")
                        for ref in refs_janta:
                            ref.set_data(dia_atual)
                            ref.set_tipo("jantar")
                        
                        refeicoes.extend([*refs_lanche, *refs_almoco, *refs_janta])
                    View.cardapio_add(data_inicial, data_final, refeicoes)
                    st.success("Cardápio Adicionado com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
    
    @staticmethod
    def atualizar_cardapio() -> None:
        gerar_refeicoes = View.refeicao_get_all # Guardamos a função ao invés dos objetos para evitar uns problemas de referência com os diversos "multiselect"
        cardapios = View.cardapio_get_all()
        cardapio_selecionado = st.selectbox("Cardápio Escolhido", cardapios, key="cardapio_atualizado")
        if not cardapio_selecionado:
            st.warning("Nenhum Cardápio Encontrado!")
            return

        dias_intermediarios = View.calc_dias_intermediarios(cardapio_selecionado.get_data_inicial(), cardapio_selecionado.get_data_final())
        data_escolhida = st.selectbox("Data do Cardápio", [ di for di in dias_intermediarios ], format_func=lambda di: cardapio_selecionado.get_data_formatada(di))
        
        if data_escolhida:
            refeicoes_do_cardapio = cardapio_selecionado.get_refeicoes()
            refeicoes_cardapio_por_tipo = {
                "lanche_manha" : [],
                "lanche_tarde" : [],
                "lanche_noite" : [],
                "almoco" : [],
                "jantar" : []
            }
            for ref in refeicoes_do_cardapio:
                if ref.get_data() == data_escolhida:
                    refeicoes_cardapio_por_tipo[ref.get_tipo()].append(ref)
            
            st.divider()
            
            if len(refeicoes_cardapio_por_tipo["lanche_manha"]) > 0:
                st.text("Refeições Originais do Lanche da Manhã:")
                st.text(" + ".join([ r.get_nome() for r in  refeicoes_cardapio_por_tipo["lanche_manha"]]))
            lanche_manha = st.multiselect("Lanche da Manhã", gerar_refeicoes(), key="lanche_manha_atualizar")
            if len(refeicoes_cardapio_por_tipo["lanche_tarde"]) > 0:
                st.text("Refeições Originais do Lanche da Tarde:")
                st.text(" + ".join([ r.get_nome() for r in  refeicoes_cardapio_por_tipo["lanche_tarde"]]))
            lanche_tarde = st.multiselect("Lanche da Tarde", gerar_refeicoes(), key="lanche_tarde_atualizar")
            if len(refeicoes_cardapio_por_tipo["lanche_noite"]) > 0:
                st.text("Refeições Originais do Lanche da Noite:")
                st.text(" + ".join([ r.get_nome() for r in  refeicoes_cardapio_por_tipo["lanche_noite"]]))
            lanche_noite = st.multiselect("Lanche da Noite", gerar_refeicoes(), key="lanche_noite_atualizar")
            if len(refeicoes_cardapio_por_tipo["almoco"]) > 0:
                st.text("Refeições Originais do Almoço:")
                st.text(" + ".join([ r.get_nome() for r in  refeicoes_cardapio_por_tipo["almoco"]]))
            almoco = st.multiselect("Almoço", gerar_refeicoes(), key="almoco_atualizar")
            if len(refeicoes_cardapio_por_tipo["jantar"]) > 0:
                st.text("Refeições Originais do Jantar:")
                st.text(" + ".join([ r.get_nome() for r in  refeicoes_cardapio_por_tipo["jantar"]]))
            jantar = st.multiselect("Jantar", gerar_refeicoes(), key="jantar_atualizar")
            atualizar = st.button("Atualizar")
            
            if atualizar:
                try:
                    refeicoes = []
                    for ref in lanche_manha:
                        ref.set_tipo("lanche_manha")
                    for ref in lanche_tarde:
                        ref.set_tipo("lanche_tarde")
                    for ref in lanche_noite:
                        ref.set_tipo("lanche_noite")
                    for ref in almoco:
                        ref.set_tipo("almoco")
                    for ref in jantar:
                        ref.set_tipo("jantar")
                    refeicoes.extend([*lanche_manha, *lanche_tarde, *lanche_noite, *almoco, *jantar])
                    View.set_cardapio_dia_diferente(cardapio_selecionado, refeicoes, data_escolhida)
                    View.cardapio_update(
                        cardapio_selecionado.get_id(), 
                        cardapio_selecionado.get_data_inicial(), 
                        cardapio_selecionado.get_data_final(),
                        cardapio_selecionado.get_refeicoes()
                    )
                    st.success("Cardápio Atualizado com Sucesso!")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}")

                sleep(1)
                st.rerun()
        else:
            st.warning("Nenhuma Data Encontrada!")
     
    @staticmethod
    def deletar_cardapio() -> None:
        cardapios = View.cardapio_get_all()
        cardapio_selecionado = st.selectbox("Cardápio Escolhido", cardapios, key="cardapio_deletado")
        deletar = st.button("Deletar")

        if deletar:
            try:
                View.cardapio_delete(cardapio_selecionado.get_id())
                st.success("Cardápio Deletado com Sucesso!")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}")

            sleep(1)
            st.rerun()
