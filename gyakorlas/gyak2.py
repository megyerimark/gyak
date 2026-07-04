
import math

print("************************************************************************************")
print("1. Részfeladat: A Kovácsműhely (Matematikai operátorok és Egészosztás)")
#A szabály: Egyetlen kard elkészítéséhez pontosan 3 darab vasra és 2 darab szénre van szükség.
max_vas = 14
max_szen = 10

vas_kardbol = max_vas // 3
print("Vasbol maximum : ", vas_kardbol ,"DB  kard készíthető el")    
szen_kardbol = max_szen // 2
print("Szénből maximum: ", szen_kardbol ,"DB  kard készíthető el")


kesz_kardok = min(vas_kardbol , szen_kardbol)
print("A kovács elkészített", kesz_kardok,"darab kardot!")

maradek_vas = max_vas % 3
maradek_szen = max_szen % 2

print("Megmaradt vas:", maradek_vas, "megmaradt szén:", maradek_szen)


print("************************************************************************************")
print("2. Részfeladat: A Hős Hátizsákja (Szótárak / Dictionaries)")

hatizsak = {
    "arany": 50,
    "gyogyital": 2,
    "kenyer": 3,
}
#Írd ki a képernyőre, hogy pontosan mennyi aranyad van! (Tipp: A szótár elemeire a kulcsuk nevivel hivatkozunk, pl. szotar["kulcs"]).
#Kincset találtál! Adj hozzá egy teljesen új elemet a szótárhoz: "varazskard", aminek az értéke legyen 1.
#Csata történt! A hősöd megivott egy gyógyitalt. Csökkentsd a "gyogyital" értékét 1-gyel (használhatod a -= operátort).
#Írj egy if feltételt: Ha a gyógyitalok száma eléri a 0-t, írd ki: "Figyelem: Elfogyott az összes gyógyitalod!"
#A feladat végén nyomtasd ki a teljes hatizsak tartalmát, hogy lásd a frissült állapotot!
print(hatizsak["arany"])
#Kincset találtál! Adj hozzá egy teljesen új elemet a szótárhoz: "varazskard", aminek az értéke legyen 1
hatizsak["varzskard"] = 1
#Csata történt! A hősöd megivott egy gyógyitalt. Csökkentsd a "gyogyital" értékét 1-gyel (használhatod a -= operátort).
hatizsak["gyogyital"]-=1

if hatizsak["gyogyital"]== 0:
    print('asd')
    
    

print(hatizsak)







print("************************************************************************************")
print("3. Részfeladat: A Veszélyes Útvonal (Tuple és Logikai operátorok)")

# (X, Y) koordináták
utvonal = [(10, 20), (12, 22), (15, 25), (18, 30), (20, 25)]

for x , y in utvonal:
    if x == 15 and y == 25:
        print("VIGYÁZAT! SÁRKÁNY A LÁTHATÁRON!")
    else:
         print(f"Biztonságos lépés a [{x}], [{y}] koordinátára")
