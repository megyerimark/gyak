import tkinter as tk
import matplotlib.pyplot as plt
import kalkulator_modul as mo


window = tk.Tk()
def generate_chart():
    yasuo_meccsek = {}
    szerzett_lp = 0
    with open ("meccsek.txt", "r", encoding="utf-8") as meccsek:
        next(meccsek)
        for m in meccsek:
            adatok = m.strip().split(";")
            if adatok[1] == "Yasuo":
                kda_lista = adatok[2].strip().split("/")
            # if yasuo_meccsek[adatok[1]] == adatok[1]:
            #     kda_lista = yasuo_meccsek[2].strip().split("/")
            #     print(kda_lista)
                try:
                    kda_kill = int(kda_lista[0])
                    kda_halal = int(kda_lista[1])
                    kda_assist = int(kda_lista[2])
                except ValueError as v:
                    print(f"Hibás statisztika a(z) {adatok[0]} meccsnél!")
                    continue
                else:
                    vegleges_kda = mo.kda_erekeles(kda_kill,kda_halal,kda_assist)
                    yasuo_meccsek[adatok[0]] = (vegleges_kda, adatok[4])
                    if adatok[4] == "Gyozelem":
                        szerzett_lp +=20
                    
    x_meccsek = []
    y_kda = []
    for kulcs, ertek in yasuo_meccsek.items():
        x_meccsek.append(kulcs)
        y_kda.append(ertek[0])
    plt.bar(x_meccsek, y_kda)
    plt.ylabel("KDA Arány")
    plt.show()
    print(f"A Yasuo elemzés lefutott. Nyeremény LP: {szerzett_lp}.")





window.title("Yasuo KDA")
window.geometry("400x700")
btn = tk.Button(window, text="Calculate", command=generate_chart)
btn.pack(pady=10)
    
    


window.mainloop()