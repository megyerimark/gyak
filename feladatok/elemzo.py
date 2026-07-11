import kalkulator_modul as km
import matplotlib.pyplot as plt

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
                vegleges_kda = km.kda_erekeles(kda_kill,kda_halal,kda_assist)
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

# 1. Fájl: kalkulator_modul.py (A te saját modelled)
# Ez a fájl fogja végezni a kőkemény matematikát a háttérben.

# Hozd létre benne az alábbi szótárat (később talán használjuk):
# rang_szorzo = {"Vas": 1.0, "Bronz": 1.2, "Ezüst": 1.5, "Arany": 2.0}

# Írj egy függvényt: def kda_ertekeles(kill, halal, assziszt):

# A függvény feladata, hogy kiszámolja az úgynevezett KDA arányt. A képlet: (Kill + Assziszt) osztva a Halállal.

# A csapda: A matematikában nem oszthatunk nullával! Írj a függvénybe egy if feltételt: ha a halal értéke 0, akkor a képletben a halál helyett 1-gyel osszon (így nem omlik össze a kód).

# A függvény térjen vissza a kiszámolt KDA eredménnyel!

# 2. Az Adatbázis: meccsek.txt
# Hozd létre ezt a fájlt a mappádban pontosan ezzel a tartalommal (vigyázz, az első sor a fejléc!):

# Plaintext
# Meccs_ID;Karakter;K/D/A;Rang;Eredmeny
# M01;Yasuo;10/2/5;Arany;Gyozelem
# M02;Zed;4/5/2;Ezüst;Vereseg
# M03;Yasuo;15/0/8;Arany;Gyozelem
# M04;Ahri;Hiba/2/4;Bronz;Vereseg
# M05;Yasuo;2/8/1;Arany;Vereseg
# 3. Fájl: elemzo_kozpont.py (A Főprogramod)
# Ez fogja össze a rendszert, olvassa a fájlt, és rajzolja a grafikont.

# A) Előkészületek

# Importáld be a saját kalkulator_modul-odat (pl. as km néven).

# Importáld be a Matplotlib-et is (import matplotlib.pyplot as plt).

# Hozz létre egy üres szótárat: yasuo_meccsek = {}

# Hozz létre egy kasszát: szerzett_lp = 0

# B) Fájlbeolvasás és Adattisztítás

# Nyisd meg a meccsek.txt fájlt olvasásra, és ugord át a fejlécet!

# Egy for ciklussal menj végig a sorokon, és darabold fel őket a pontosvesszők (;) mentén.

# A Szűrő (if): Mi csak Yasuo-t vizsgáljuk! Írj egy if-et: csak akkor menjen tovább a kód, ha a karakter neve (1. index) pontosan "Yasuo". (Mindenki mást hagyjon figyelmen kívül).

# Listaművelet: Ha Yasuo az illető, darabold fel a K/D/A oszlopot (2-es index) a perjelek (/) mentén, és mentsd el egy kda_lista nevű változóba! (Pl. a "10/2/5"-ből lesz egy ['10', '2', '5'] listád).

# C) A Védőháló és a Logika (Try-Except-Else)

# try: Próbáld meg a kda_lista 0., 1. és 2. elemét (a killeket, halálokat és asszisztokat) egész számmá (int) alakítani egy-egy külön változóba.

# except ValueError: Írd ki, hogy "Hibás statisztika a(z) {meccs_id} meccsnél!", és ugorj a következőre (continue).

# else (Ha sikerült a matek):

# Hívd meg a saját modulod kda_ertekeles függvényét a három számmal, és mentsd el az eredményt egy vegleges_kda változóba!

# Szótár feltöltése: A yasuo_meccsek szótár kulcsa legyen a Meccs_ID (0. index). Az Értéke pedig legyen egy 2-es Tuple: (vegleges_kda, Eredmeny). (Az Eredmény a darabolt sor 4. indexe).

# LP Számolás: Ha az "Eredmeny" pontosan "Gyozelem", akkor adj hozzá 20-at a szerzett_lp globális kasszához!

# D) A Matplotlib Grafikon (A ciklus után!)

# Hozz létre két üres listát: x_meccsek = [] és y_kda = [].

# Egy új for ciklussal iterálj végig a feltöltött yasuo_meccsek.items()-en!

# Az .append() segítségével töltsd fel az x_meccsek-et a kulcsokkal (Meccs_ID), az y_kda-t pedig az érték (Tuple) 0. indexével (ez a KDA szám).

# Rajzold ki egy oszlopdiagrammal (plt.bar), adj nevet az Y tengelynek ("KDA Arány"), és mutasd meg az ablakot (show)!

# E) Zárás
# A program legeslegvégén printeld ki:
# "A Yasuo elemzés lefutott. Nyeremény LP: {szerzett_lp}."

# Ez a feladat egyesíti a tegnap éjszakai harci napló logikáját a grafikonrajzolással és a külső moduljaiddal, de egy picit kevesebb "egymásba ágyazott" indexeléssel, hogy a tiszta adatfolyamra tudj koncentrálni