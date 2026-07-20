# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import os

# # --- 1. AZ AGY: Objektumorientált Üzleti Logika ---
# class Kliens:
#     def __init__(self, nev, jovedelem, hitel):
#         self.nev = nev
#         self.jovedelem = jovedelem
#         self.hitel = hitel
        
#     def biralat(self):
#         if (self.jovedelem * 0.5) > self.hitel:
#             return True, "Siker, a hitel hamarosan folyósítva lesz!"
#         else:
#             return False, "Elutasítva! JTM szabály sérült!"
    
# class VIPKliens(Kliens):
#     def __init__(self, nev, jovedelem, hitel, bankar):
#         super().__init__(nev, jovedelem, hitel)
#         self.bankar = bankar
        
#     def udvozles(self):
#         return f"Üdvözlöm a VIP részlegen Tisztelt {self.nev}, a bankára: {self.bankar}"


# # --- 2. AZ ADATBÁZIS: Pandas és Fájlkezelés ---
# # Létrehozunk egy funkciót, ami betölti a korábbi CSV fájlunkat
# @st.cache_data # Ez felgyorsítja a weblapot, nem olvassa be másodpercenként a fájlt
# def adat_betoltes():
#     # Ha létezik a fájl, beolvassa. Ha nem, csinál egy üres táblázatot.
#     if os.path.exists("banki_ugyfelek.csv"):
#         return pd.read_csv("banki_ugyfelek.csv")
#     else:
#         return pd.DataFrame(columns=["ID", "Nev", "Eletkor", "Netto_Jovedelem", "Kert_Hitel", "Hitel_Tipus", "VIP_Statusz"])


# # --- 3. A KÉPERNYŐ: Streamlit UI ---
# st.set_page_config(page_title="Banki Asszisztens", page_icon="💼", layout="wide")
# st.title("💼 Middle Office Banki Asszisztens")

# # Füleket (Tabs) hozunk létre a navigációhoz
# tab_uj_ugyfel, tab_dashboard = st.tabs(["📝 Új Hitelkérelem", "📊 Vezetői Dashboard"])

# df = adat_betoltes() # Betöltjük az "Excel" táblánkat

# # --- FÜL 1: ÚJ ÜGYFÉL (Az űrlapod és az OOP) ---
# with tab_uj_ugyfel:
#     st.subheader("Ügyféladatok Rögzítése")
    
#     with st.form("uj_hitel_form"):
#         col1, col2 = st.columns(2) # Két oszlopba rendezzük az űrlapot, hogy szebb legyen
#         with col1:
#             nev = st.text_input("Ügyfél neve:")
#             eletkor = st.number_input("Életkor:", min_value=18, max_value=100)
#             vip = st.checkbox("VIP Ügyfél?")
            
#         with col2:
#             jovedelem = st.number_input("Havi Nettó Jövedelem (Ft):", min_value=0, step=10000)
#             hitel = st.number_input("Kért Hitelösszeg (Ft):", min_value=0, step=100000)
#             tipus = st.selectbox("Hitel Típusa:", ["Személyi hitel", "Lakáshitel", "Autólízing"])
            
#         pipa = st.checkbox("Jogi nyilatkozat elfogadása")
#         bekuldes = st.form_submit_button("Bírálat Futtatása")
        
#     if bekuldes:
#         if not pipa:
#             st.error("Kérjük, fogadja el a jogi nyilatkozatot!")
#         else:
#             # Objektum példányosítása és bírálat
#             if vip:
#                 ugyfel = VIPKliens(nev, jovedelem, hitel, "Kovács")
#                 st.info(ugyfel.udvozles())
#             else:
#                 ugyfel = Kliens(nev, jovedelem, hitel)
                
#             siker, uzenet = ugyfel.biralat()
            
#             if siker:
#                 st.success(uzenet)
#                 st.snow()
#                 # Ha sikeres a bírálat, hozzáfűzzük az ÚJ ügyfelet a Pandas táblázathoz!
#                 uj_sor = pd.DataFrame([{
#                     "ID": len(df) + 1, "Nev": nev, "Eletkor": eletkor, 
#                     "Netto_Jovedelem": jovedelem, "Kert_Hitel": hitel, 
#                     "Hitel_Tipus": tipus, "VIP_Statusz": "Igen" if vip else "Nem"
#                 }])
#                 # Hozzáadjuk az eredeti táblázathoz, és azonnal felülírjuk a fizikai CSV fájlt!
#                 df = pd.concat([df, uj_sor], ignore_index=True)
#                 df.to_csv("banki_ugyfelek.csv", index=False)
#                 st.toast("Adatbázis sikeresen frissítve!")
#             else:
#                 st.error(uzenet)


# # --- FÜL 2: VEZETŐI DASHBOARD (A Pandas és a Matplotlib) ---
# with tab_dashboard:
#     st.subheader("Aktuális Portfólió Elemzés")
    
#     # 1. Pandas Statisztikák (Data elemzés)
#     osszes_hitel = df["Kert_Hitel"].sum()
#     atlag_jovedelem = df["Netto_Jovedelem"].mean()
    
#     colA, colB, colC = st.columns(3)
#     colA.metric("Ügyfelek száma", len(df))
#     colB.metric("Kiadott Hitelek (Összesen)", f"{osszes_hitel:,.0f} Ft")
#     colC.metric("Átlag Jövedelem", f"{atlag_jovedelem:,.0f} Ft")
    
#     st.divider()
    
#     col_bal, col_jobb = st.columns(2)
    
#     # 2. Pandas Csoportosítás + Matplotlib Rajzolás
#     with col_bal:
#         st.write("### Hitelek megoszlása típus szerint")
#         # A Pandas összeadja hiteltípusonként a pénzeket
#         tipus_csoport = df.groupby("Hitel_Tipus")["Kert_Hitel"].sum()
        
#         fig, ax = plt.subplots()
#         # Itt egy szép kördiagramot (pie chart) rajzoltatunk a Matplotlibbel
#         ax.pie(tipus_csoport, labels=tipus_csoport.index, autopct='%1.1f%%', startangle=90)
#         ax.axis('equal') # Hogy szép kerek legyen
#         st.pyplot(fig)
        
#     with col_jobb:
#         st.write("### VIP vs Normál ügyfelek jövedelme")
#         # Streamlit natív grafikon (a rövidebb út, amit tanultunk)
#         vip_csoport = df.groupby("VIP_Statusz")["Netto_Jovedelem"].mean()
#         st.bar_chart(vip_csoport)

#     # Nyers adatbázis megtekintése
#     with st.expander("Nyers Adatbázis Megtekintése"):
#         st.dataframe(df) # Ez egy interaktív Excel-szerű táblázatot rajzol a böngészőbe