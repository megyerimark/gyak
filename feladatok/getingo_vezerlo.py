import stripe_modul as smodul

napi_bevetel = 0
#probak = 0

with open ( " sikeres_fizetesek.txt", "a", encoding="utf-8") as sikeres:
    while True:
        valasztott_csomag = input("Melyik csomagot kéred?\n" + " Alap/Pro/VIP \n  Kilépés a programból?\n")
        if valasztott_csomag == "kilépés":
            print(" Bezártad a boltot")
            break
        if valasztott_csomag not in smodul.csomagok:
            print("Nincs ilyen csomag")
            continue
        else:
            kartya_szam = input("Kártyaszám")
            borravalo = input("Támogatás a fejlesztőnek (Ft)")
        try:
            teljes_osszeg = int(borravalo)
            teljes_osszeg +=smodul.csomagok[valasztott_csomag]
        except ValueError as v:
            print(v, "Hibás összeg, a tranzakció megszakadt")
        else:
            if smodul.fizetes_ellenorzes(kartya_szam) == True:
                napi_bevetel += teljes_osszeg
                print("Siekres Fizetés! ")
                sikeres.write(f"{valasztott_csomag} eladva. Bevétel: {teljes_osszeg} Ft\n")
            else:
                print("Elutasítva, Érvénytelen kártyaszám")
print(f"A Getingo terminál lezárva. Napi bevétel: {napi_bevetel} Ft.")