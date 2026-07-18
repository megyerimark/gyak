import streamlit as st
import matplotlib.pyplot as plt

class Kliens:
    def __init__(self, nev, jovedelem, hitel):
        self.nev = nev
        self.jovedelem = jovedelem
        self.hitel = hitel
        
    def biralat(self):
        
        if (self.jovedelem * 0.5) > self.hitel:
            return True, "Siker, a hitel hamarosan folyósítva lesz!"
        else:
            return False, "Elutasítva! JTM szabály sérült!"
    
class VIPKliens(Kliens):
    def __init__(self, nev, jovedelem, hitel, bankar):
        super().__init__(nev, jovedelem, hitel)
        self.bankar = bankar
        
    def udvozles(self):
        return f"Üdvözlöm a VIP részlegen Tisztelt {self.nev}, a személyes bankára: {self.bankar}"



st.title("🏦 Middle Office Hitelbíráló")

if 'nevek' not in st.session_state:
    st.session_state.nevek = []
if 'jovedelmek' not in st.session_state:
    st.session_state.jovedelmek = []

# --- ŰRLAP (Ez váltja le az input() parancsokat) ---
with st.form("ugyfel_urlap"):
    ugyfel_neve = st.text_input("Kérem az ügyfél nevét:")
    
    jov = st.number_input("Kérem a jövedelmet:", min_value=0, step=10000)
    hit = st.number_input("Kérem a hitel összeget:", min_value=0, step=10000)
    
    vip_e = st.checkbox("VIP ügyfél?")
    
   
    submit_button = st.form_submit_button("Bírálat indítása")



if submit_button and ugyfel_neve:
    if vip_e:
        aktualis_ugyfel = VIPKliens(ugyfel_neve, jov, hit, "Kovács")
        st.info(aktualis_ugyfel.udvozles()) 
    else:
        aktualis_ugyfel = Kliens(ugyfel_neve, jov, hit)

    # Bírálat lefuttatása
    siker, uzenet = aktualis_ugyfel.biralat()
    
    if siker:
        st.success(uzenet)  # Zöld pipa doboz
    else:
        st.error(uzenet)    # Piros X doboz
        
    # Adatok elmentése a grafikonhoz
    st.session_state.nevek.append(ugyfel_neve)
    st.session_state.jovedelmek.append(jov)


# --- 4. A GRAFIKON (Matplotlib beágyazása a weboldalba) ---
st.divider() # Húz egy elválasztó vonalat
st.subheader("📊 Napi Jövedelem Elemzés")


if len(st.session_state.nevek) > 0:
    fig, ax = plt.subplots() 
    ax.bar(st.session_state.nevek, st.session_state.jovedelmek)
    ax.set_title("Elemzés")
    ax.set_ylabel("Jövedelem")
    ax.set_xlabel("Név")
    
    # plt.show() helyett a Streamlit rajzológépe:
    st.pyplot(fig)
else:
    st.write("Még nincs rögzített adat a rajzoláshoz.")