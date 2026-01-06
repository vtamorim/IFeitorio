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
        st.title("Cardápio 21/12/2025 - 26/12/2025")
        st.subheader("Cardápio do Lanche")
        lanche_df = pd.DataFrame(
            {
                "21/12/2025": [ "Pão com Ovos + Banana + Suco de Manga", "Pão com Ovos + Banana + Suco de Manga", "Pão com Ovos + Banana + Suco de Manga" ],
                "16/12/2025": [ "Bolo de Chocolate + Melancia + Suco de Goiaba", "Bolo de Chocolate + Melancia + Suco de Goiaba", "Bolo de Chocolate + Melancia + Suco de Goiaba" ],
                "17/12/2025": [ "Pão com Queijo + Bolo de Chocolate + Manga + Suco de Manga", "Pão com Queijo + Manga + Suco de Manga", "Pão com Queijo + Manga + Suco de Manga" ],
                "18/12/2025": [ "Cuscuz com Frango + Melancia + Suco de Acerola ao Leite", "Cuscuz com Frango + Melancia + Suco de Acerola ao Leite", "Cuscuz com Frango + Melancia + Suco de Acerola ao Leite" ],
                "19/12/2025": [ "Arroz com Frango + Maçã + Suco de Maracujá", "Arroz com Frango + Maçã + Suco de Maracujá", "Arroz com Frango + Maçã + Suco de Maracujá" ]
            },
            index=["Manhã", "Tarde", "Noite"]
        )
        st.dataframe(lanche_df)

        st.subheader("Cardápio do Almoço")
        almoco_df = pd.DataFrame(
            {
                "21/12/2025": [ "Salada Crua", "Isca de carne ao molho", "Almondega de abobrinha", "Macarrão", "Suco de Acerola" ],
                "22/12/2025": [ "Salada Cozida", "Frango em cubos ao molho de tomate", "Soja refogada ao molho", "Arroz refogado", "Suco de Manga" ],
                "23/12/2025": [ "Cardápio Natalino", "", "", "", "" ],
                "24/12/2025": [ "Salada Crua", "Bife Acebolado", "Omelete", "Arroz refogado", "Suco de Goaiba" ],
                "25/12/2025": [ "Salada Cozida", "Ensopado de peixe", "Estrogonofe de soja c/ vegetais", "Arroz integral", "Suco de Uva" ]
            }
        )
        st.dataframe(almoco_df, hide_index=True)

        st.subheader("Cardápio do Jantar")
        jantar_df = pd.DataFrame(
            {
                "21/12/2025": [ "Feijão Preto", "Farofa", "Suco de Acerola" ],
                "22/12/2025": [ "Feijão Carioca", "Suco de Manga", "" ],
                "23/12/2025": [ "Cardápio Natalino", "", "" ],
                "24/12/2025": [ "Feijão Preto", "Farofa", "Suco de Goaiba" ],
                "25/12/2025": [ "Feijão Branco", "Farofa de cuscuz", "Suco de Uva" ]
            }
        )
        st.dataframe(jantar_df, hide_index=True)

        st.title("Cardápio 15/12/2025 - 25/12/2025")
        st.subheader("Cardápio do Lanche")
        lanche_df = pd.DataFrame(
            {
                "15/12/2025": [ "Pão com Ovos + Banana + Suco de Manga", "Pão com Ovos + Banana + Suco de Manga", "Pão com Ovos + Banana + Suco de Manga" ],
                "22/12/2025": [ "Bolo de Chocolate + Melancia + Suco de Goiaba", "Bolo de Chocolate + Melancia + Suco de Goiaba", "Bolo de Chocolate + Melancia + Suco de Goiaba" ],
                "23/12/2025": [ "Pão com Queijo + Bolo de Chocolate + Manga + Suco de Manga", "Pão com Queijo + Manga + Suco de Manga", "Pão com Queijo + Manga + Suco de Manga" ],
                "24/12/2025": [ "Cuscuz com Frango + Melancia + Suco de Acerola ao Leite", "Cuscuz com Frango + Melancia + Suco de Acerola ao Leite", "Cuscuz com Frango + Melancia + Suco de Acerola ao Leite" ],
                "19/12/2025": [ "Arroz com Frango + Maçã + Suco de Maracujá", "Arroz com Frango + Maçã + Suco de Maracujá", "Arroz com Frango + Maçã + Suco de Maracujá" ]
            },
            index=["Manhã", "Tarde", "Noite"]
        )
        st.dataframe(lanche_df)

        st.subheader("Cardápio do Almoço")
        almoco_df = pd.DataFrame(
            {
                "15/12/2025": [ "Salada Crua", "Isca de carne ao molho", "Almondega de abobrinha", "Macarrão", "Suco de Acerola" ],
                "16/12/2025": [ "Salada Cozida", "Frango em cubos ao molho de tomate", "Soja refogada ao molho", "Arroz refogado", "Suco de Manga" ],
                "17/12/2025": [ "Cardápio Natalino", "", "", "", "" ],
                "18/12/2025": [ "Salada Crua", "Bife Acebolado", "Omelete", "Arroz refogado", "Suco de Goaiba" ],
                "19/12/2025": [ "Salada Cozida", "Ensopado de peixe", "Estrogonofe de soja c/ vegetais", "Arroz integral", "Suco de Uva" ]
            }
        )
        st.dataframe(almoco_df, hide_index=True)

        st.subheader("Cardápio do Jantar")
        jantar_df = pd.DataFrame(
            {
                "15/12/2025": [ "Feijão Preto", "Farofa", "Suco de Acerola" ],
                "16/12/2025": [ "Feijão Carioca", "Suco de Manga", "" ],
                "17/12/2025": [ "Cardápio Natalino", "", "" ],
                "18/12/2025": [ "Feijão Preto", "Farofa", "Suco de Goaiba" ],
                "19/12/2025": [ "Feijão Branco", "Farofa de cuscuz", "Suco de Uva" ]
            }
        )
        st.dataframe(jantar_df, hide_index=True)
    
    @staticmethod
    def adicionar_cardapio() -> None:
        segunda_atual, sexta_atual = View.calc_dias_da_semana(date.today())

        data_inicial = st.date_input("Data Inicial", segunda_atual, format="DD/MM/YYYY")
        data_final = st.date_input("Data Final", sexta_atual, format="DD/MM/YYYY")
        adicionar = False
        
        if data_inicial and data_final:
            dif_dias = data_final - data_inicial

            for i in range(dif_dias.days + 1):
                dia_atual = data_inicial + timedelta(days=i)

                st.divider()
                st.subheader(f'Data: {dia_atual.strftime("%d/%m/%Y")}')

                lanche = st.multiselect("Lanche", [ "Pão com Ovo", "Pão com Queijo", "Bolo de Chocolate" ], key=f"lanche_adicionar_{i}")
                almoco = st.multiselect("Almoço", [ "Macarrão com Queijo", "Suco de Laranja", "Ovos Cozidos" ], key=f"almoco_adicionar_{i}")
                janta = st.multiselect("Janta", [ "Macarrão com Queijo", "Suco de Laranja", "Ovos Cozidos" ], key=f"janta_adicionar_{i}")
            
            adicionar = st.button("Adicionar")

        if adicionar:
            st.success("Cardápio Adicionado com Sucesso!")

            sleep(1)
            st.rerun()
    
    @staticmethod
    def atualizar_cardapio() -> None:
        cardapio_selecionado = st.selectbox("Cardápio Escolhido", [ "Cardápio 1 - 12/09/2025 - 16/09/2025", "Cardápio 2 - 18/09/2025 - 22/09/2025" ], key="cardapio_atualizado")
        data_escolhida = st.selectbox("Data do Cardápio", [ f"{i}/09/2025" for i in range(12, 17) ])
        
        if data_escolhida:
            st.divider()
            
            lanche_manha = st.multiselect("Lanche da Manhã", [ "Pão com Ovo", "Pão com Queijo", "Bolo de Chocolate" ], key="lanche_manha_atualizar")
            lanche_tarde = st.multiselect("Lanche da Tarde", [ "Pão com Ovo", "Pão com Queijo", "Bolo de Chocolate" ], key="lanche_tarde_atualizar")
            lanche_noite = st.multiselect("Lanche da Noite", [ "Pão com Ovo", "Pão com Queijo", "Bolo de Chocolate" ], key="lanche_noite_atualizar")
            almoco = st.multiselect("Almoço", [ "Macarrão com Queijo", "Suco de Laranja", "Ovos Cozidos" ], key="almoco_atualizar")
            janta = st.multiselect("Janta", [ "Macarrão com Queijo", "Suco de Laranja", "Ovos Cozidos" ], key="janta_atualizar")
        atualizar = st.button("Atualizar")
        
        if atualizar:
            st.success("Cardápio Atualizado com Sucesso!")

            sleep(1)
            st.rerun()
     
    @staticmethod
    def deletar_cardapio() -> None:
 
        cardapio_selecionado = st.selectbox("Cardápio Escolhido", [ "Cardápio 1 - 12/09/2025 - 16/09/2025", "Cardápio 2 - 18/09/2025 - 22/09/2025" ], key="cardapio_deletado")
        deletar = st.button("Deletar")

        if deletar:
            st.success("Cardápio Deletado com Sucesso!")

            sleep(1)
            st.rerun()
