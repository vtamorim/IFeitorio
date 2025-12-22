import pandas as pd
import streamlit as st
from views import View

class AlunoVisualizarCardapiosUI:
    """Página do Aluno visualizar os cardápios."""
    @staticmethod
    def main() -> None:
        st.set_page_config(layout="wide")
        st.header("Visualizar Cardápios")

        st.title("Cardápio 15/12/2025 - 19/12/2025") # Vamos pegar esses Dados da View
        st.subheader("Cardápio do Lanche")
        lanche_df = pd.DataFrame(
            {
                "15/12/2025": [ "Pão com Ovos + Banana + Suco de Manga", "Pão com Ovos + Banana + Suco de Manga", "Pão com Ovos + Banana + Suco de Manga" ],
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
