# import streamlit as st
# import pandas as pd
# import numpy as np


# a = st.text_area("Kérlek írd le a panaszod vagy kérdésed ")
# b =st.date_input("Dátum")
# c =st.time_input("Idő")
# d = st.select_slider("Kérlek válazd ki a megfelelő pioritást", options=["Alacson", "Közepes", "Magas"])
# pipa = st.checkbox("Elfogadom az Adatkezelési Tájékoztatót")
# gomb =st.button("Beküldés")

# if gomb:
#     if pipa:
#         st.success("Sikeres beküldés!")
#         st.snow()
#     else:
#         st.error("Hiba! Kérlek fogadd el a szabályzatot a beküldéshez!")

# st.divider()
# ip = st.context.ip_address
# st.info(f"Biztonsági okokból... IP: {ip}")

# all_info_szoveg = f"""--- BEÉRKEZETT PANASZ JEGYZŐKÖNYV ---
# Panasz leírása: {a}
# Dátum: {b}
# Idő: {c}
# Prioritás: {d}
# Rögzített IP: {ip}
# """
# st.color_picker("kiemelő szín")

# st.download_button("Letöltés", data =all_info_szoveg, file_name="panasz.txt")
# st.feedback("stars")