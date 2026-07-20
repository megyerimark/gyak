import streamlit as st
import numpy as np

class Kiadas:
    def __init__(self, kategoria, osszeg):
        self.kategoria = kategoria
        self.osszeg = osszeg
        
    def elbiralas(self):
        if self.osszeg > 50000:
            st.warning("Vezetői Jóváhagyás szükséges")
        else:
            st.success("Autómaitkus Jóváhagyás")


class EszkozBeszerzes(Kiadas):
    def __init__(self, kategoria, osszeg, eszkoz_neve):
        super().__init__(kategoria, osszeg)
        self.eszkoz_neve = eszkoz_neve
        
st.title("Céges Költségszámláló")
options = st.selectbox("Kérlek válassz az alábbiak közül",
    ("Utazás","Irodaszer","IT Eszköz"),
    )
st.write("Kiválasztottad a(z)", options)
price = st.number_input("Kérlek add meg az összeget: ",  min_value=3000)
st.info(f"Az általad megadott összeg:  {price}")



if options == "Utazás":
    bem = st.text_input("Helyszín: ")
elif options == "Irodaszer":
    bem = st.text_input("Irodaszer: ")
elif options == "IT Eszköz":
    bem = st.text_input("IT eszköz neve: ")
btn = st.button("Beküldés")


if btn: 
    st.write("Az általad megadott helyszín: ", bem)
    if options == "IT Eszköz":
        eszkoz = EszkozBeszerzes(options, price, bem)      
    else:
        ki = Kiadas(options, price)
        ki.elbiralas()
        
        
# # if options == "Utazás":
# em = st.text_input("Helyszín: ")
# if btn == True and options == "Utazás":
#         eszkoz = EszkozBeszerzes(options, price, bem)
#         st.write("Az általad megadott helyszín: ", bem)
#         EszkozBeszerzes.elbiralas(eszkoz)
#         st.success("Folyamat elindítva")
# elif options =="Irodaszer":
#         bem = st.text_input("Vásárolni kívánt tárgy: ")
#         eszkoz = EszkozBeszerzes(options, price, bem)
#         st.write("Az általad megadott készülék neve: ", bem)
#         EszkozBeszerzes.elbiralas(eszkoz)
#         st.success("Folyamat elindítva")
#         ki = Kiadas(options,price)
#         Kiadas.elbiralas(ki)
            
# elif options == "IT Eszköz":
#         bem = st.text_input("Vásárolni kívánt eszköz: ")
#         eszkoz = EszkozBeszerzes(options, price, bem)
#         st.write("Az általad megadott eszköz neve: ", bem)
#         EszkozBeszerzes.elbiralas(eszkoz)
#         st.success("Folyamat elindítva")
#         ki = Kiadas(options,price)
#         Kiadas.elbiralas(ki)
#         ki = Kiadas(options,price)
#         Kiadas.elbiralas(ki)
# if options == "Irodaszer":
#     bem = st.text_input("Vásárolni kívánt tárgy: ")
#     if btn == True and options == "Irodaszer":
#         eszkoz = EszkozBeszerzes(options, price, bem)
#         st.write("Az általad megadott készülék neve: ", bem)
#         EszkozBeszerzes.elbiralas(eszkoz)
#         st.success("Folyamat elindítva")
#     else:
#         ki = Kiadas(options,price)
#         Kiadas.elbiralas(ki)   
# if options == "IT Eszköz":
#     bem = st.text_input("Kérlek add meg a készülék nevét: ")
#     if btn == True and options== "IT Eszköz":     
#         eszkoz = EszkozBeszerzes(options, price, bem)
#         st.write("Az általad megadott készülék neve: ", bem)
#         EszkozBeszerzes.elbiralas(eszkoz)
#         st.success("Folyamat elindítva")
#     else:
#         ki = Kiadas(options,price)
#         Kiadas.elbiralas(ki)