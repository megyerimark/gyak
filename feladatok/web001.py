import streamlit as st
import pandas as pd
import numpy as np



x = st.text_input("Kedvenc filmed")
x = st.write(f"Kedvenc filmed: {x}")
# is_clicked = st.button("Ráktaatinva")

# df = pd.read_csv("datas/data.csv")
data = pd.read_csv("data.csv")
st.write(data)

# grafikonok

char_fata = pd.DataFrame(
    data.set_index("Nev")
)
st.bar_chart(char_fata["Netto_Jovedelem"])
st.bar_chart(char_fata["Eletkor"])