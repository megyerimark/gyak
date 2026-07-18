import matplotlib.pyplot as plt
import streamlit as st
class Kliens:
    def __init__(self, nev, jovedelem,hitel):
        self.nev = nev
        self.jovedelem = jovedelem
        self.hitel = hitel
        
    def biralat(self):
        print (f"Siker, A hitel hamarosan folyósítva lesz. A kért hitelösszeg: {self.hitel} ")if (self.jovedelem  * 0.5)> self.hitel else print("Elutasítva! JTM szabály sérült!")
    
class VIPKliens(Kliens):
    def __init__(self, nev, jovedelem, hitel, bankar):
        super().__init__(nev, jovedelem, hitel)
        self.bankar = bankar
    def udvozles(self):
        print(f"Üdvözlöm a VIP részlegen Tisztelt {self.nev}, a személyes bankára : {self.bankar}")
        
        
        
if __name__ == "__main__":
    nevek = []
    jovedelmek = []
    while True:
        ugyfel_neve = input("Kérem az ügyfél nevét ( vagy 'vege' a bezáráshoz): ):  ")
        if ugyfel_neve == "vege":
            break
        else:
            jov = input("Kérem a jövedelmet: ")
            hit = input("Kérem a hitel összeget: ")
        try:
            int_jov = int(jov)
            int_hit = int(hit)
        except ValueError as v:
            print("Hibás adat! Csak számokat adjon meg!")
            continue
        vip_e = input("VIP ügyfél? (i/n): ")
        if vip_e == "i":
            vip = VIPKliens(ugyfel_neve, int_jov, int_hit, "Kovács")
            vip.udvozles()
            vip.biralat()
            
        
        elif vip_e == "n":
            nem_vip =Kliens(ugyfel_neve, int_jov,int_hit)
            nem_vip.biralat()
            
            
        nevek.append(ugyfel_neve)
        jovedelmek.append(int_jov)    
            
        plt.title("Elemzés")
        plt.ylabel("Jövedelem")
        plt.xlabel("Név")
        plt.bar(nevek, jovedelmek)
        plt.show()