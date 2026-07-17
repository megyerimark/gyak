import matplotlib.pyplot as plt

class HitelKerelem:
    def __init__(self, nev, netto_jovedelem, kert_torleszto):
        self.nev = nev
        self.netto_jovedelem = int(netto_jovedelem)
        self.kert_torleszto = int(kert_torleszto)
        
    def biralat(self):
        print ("Engedélyezve") if self.kert_torleszto < (self.netto_jovedelem * 0.5) else print("Elutasítva")
            
            
class PremiumKerelem(HitelKerelem):
    def __init__(self, nev, netto_jovedelem, kert_torleszto, kapcsolattarto):
        super().__init__(nev, netto_jovedelem, kert_torleszto)
        self.kapcsolattarto = kapcsolattarto


    def vip_kezeles(self):
        print(f"VIP ügyfél kérelme feldolgozás alatt. Kapcsolattartó: {self.kapcsolattarto}")
        
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}            
if __name__ == "__main__":
    name = []
    income = []
    with open("txt-t/kerelmek.txt", "r", encoding="utf-8") as k:
        next(k)
        for i in k:
            adatok = i.strip().split(",")
            i_adatok = int(adatok[2])
            name.append(adatok[0])
            income.append(i_adatok)
            if adatok[1] == " Alap".lstrip():
                aktualis_ugyfel = HitelKerelem(adatok[0], adatok[2], adatok[3])
                aktualis_ugyfel.biralat()

            else:
                premium = PremiumKerelem(adatok[0], adatok[2], adatok[3], "István")
                premium.vip_kezeles()
                premium.biralat()
    plt.title("Elemzés")
    plt.xlabel("Név", fontdict=font2)
    plt.ylabel("Nettő bevétel", fontdict=font1)
    plt.bar(name,income)
    plt.show()