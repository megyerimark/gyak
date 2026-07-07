import matplotlib.pyplot as py
szerver_kassza = 0
jatekosok_szotar = {}
proba = 0


def bonusz_kalkulator (alap_arany, *args):
    global szerver_kassza
    global proba
    teljes_arany = alap_arany + sum(args)
    szerver_kassza += teljes_arany
    return teljes_arany

while True:
    jelszo = input("Kérem a fejlesztői jelszót (vagy 'exit' a kilépéshez):")
    proba+= 1
    jo_pw = "DEV2026"
    if jelszo == "exit" or proba == 3:
        print("Rendszer leállítva")
        break
    if jelszo == jo_pw:
        print("Hozzáférés engedélyezve!") 
        break
    else:
        print("Helytelen jelszó")
with open ("szerver_log.txt", "r", encoding="utf-8") as log :
    next(log)
    for sor in log:
        adatok = sor.strip().split("|")
        rovid_nev = adatok[1][:3]
        targyak_lista = list(adatok[4].split(","))[::-1]
        try:
            arany = int(adatok[3])
            vegleges_arany =bonusz_kalkulator( arany, 200,50)
        except ValueError as v:
            print(f"Adathiba a szerveren a(z) {adatok[1]} nevű játékosnál!")
            continue
        else:
            jatekosok_szotar[adatok[1]] = (rovid_nev, vegleges_arany , targyak_lista)
nevek_x = []
arany_y= []
for kulcs, ertek in jatekosok_szotar.items():
    nevek_x.append(ertek[0])
    arany_y.append(ertek[1])
py.bar(nevek_x, arany_y)
py.ylabel("Birtokolt Arany")
py.show()
print(f"A teljes szerver gazdasága: {szerver_kassza}")Előkészület (A Bemeneti Fájl)


# Hozd létre a szerver_log.txt fájlt az alábbi tartalommal (az első sor a fejléc!):
# Plaintext
# ID|Nev|Kaszt|Arany|Targyak
# 01|YasuoMain|Kardmester|1500|Pancel,Kard,Sisak
# 02|NoobSlayer|Ijasz|Hiba|Ijj,Kopeny
# 03|TankZilla|Harcos|2200|Pajzs,Sisak,Kard,Cipo
# 04|MageLord|Varazslo|800|Bot,Ital
# 05|RogueX|Tolvaj|3100|Tor,Kopeny,Erme
# 2. Induló adatok (A fájlod legelején)

# Python
# import matplotlib.pyplot as plt

# szerver_kassza = 0
# jatekosok_szotara = {}
# 3. A Szabályok és a Logika:

# A) Az Extra Arany Függvény (bónusz_kalkulátor)
# Írj egy függvényt, ami vár egy alap_arany értéket, és végtelen számú rejtett bónusz aranyat (*args - pl. rejtett küldetésekből).
# Hívd be a globális szerver_kassza változót, és növeld meg a teljes összeggel.
# A függvény térjen vissza a játékos megnövelt aranyával!

# B) Az Admin Beléptető (A while ciklus)
# Mielőtt bármit csinálna a program, nyiss egy while True: ciklust!
# Kérd be az admin jelszót (input): "Kérem a fejlesztői jelszót (vagy 'exit' a kilépéshez): "
# Ha a jelszó "exit", a program írja ki, hogy "Rendszer leállítva", és törjön meg a ciklus (break).
# Ha a jelszó "DEV2026", printeld, hogy "Hozzáférés engedélyezve!", és egy break-kel lépj ki a ciklusból, hogy a program mehessen tovább a fájlkezelésre!
# Minden más jelszónál írja ki: "Helytelen jelszó!", és kérdezze újra.

# C) A Szerver Főmotorja (Fájlkezelés, For, Try-Except, Szeletelés)
# A jelszó után nyisd meg a szerver_log.txt-t olvasásra. (Ugorj egyet a fejlécnél!)
# A for cikluson belül darabolj a | (függőleges vonal) mentén.
# Szeletelés (Slicing): A grafikonon túl hosszú lenne a teljes név. Mentsd el egy rovid_nev változóba a játékos nevének (1-es index) csak az első 3 betűjét! (Használj szeletelést: [:3]).
# Lista megfordítás: A tárgyakat (4-es index) darabold fel a vesszők mentén egy listába. Mivel a játékosok a legújabb tárgyat akarják legelöl látni, fordítsd meg ezt a listát! (Használhatod a .reverse()-t vagy a [::-1] szeletelést). Mentsd el targyak_lista néven.
# A Védőháló (Try-Except)
# Próbáld meg int-té alakítani az aranyat. Ha sikerül, hívd meg a bónusz_kalkulátor-t, adj neki plusz 200 és 50 bónusz aranyat. Az eredményt mentsd egy vegleges_arany változóba!
# except ValueError: Írd ki: "Adathiba a szerveren a(z) {nev} nevű játékosnál!", és continue-val lépj a következőre.
# else ág (ha nincs hiba): Add hozzá a szótárhoz! A Kulcs legyen az eredeti teljes név. Az Érték legyen egy Tuple: (rovid_nev, vegleges_arany, targyak_lista).

# D) A Grafikus Finálé (Matplotlib vizualizáció)
# Miután lefutott a fájlbeolvasó for ciklus, és a szótárad feltöltődött:
# Hozz létre két üres listát: nevek_x = [] és arany_y = [].
# Egy új for ciklussal iterálj végig a jatekosok_szotara.items()-en.
# Az .append() segítségével töltsd fel a nevek_x listát a játékosok rövidített nevével (ezt a Tuple 0. indexén találod meg), az arany_y listát pedig a végleges aranyukkal (a Tuple 1. indexén)!
# Végül jöhet a rajzolás! Használd a plt.bar(nevek_x, arany_y) parancsot (a plot vonalat rajzol, a bar pedig látványos oszlopdiagramot, ami ide sokkal jobb).
# Adj neki egy feliratot: plt.ylabel("Birtokolt Arany")
# És jelenítsd meg: plt.show()
# 4. A Legutolsó Sor
# Printeld ki: "A teljes szerver gazdaság: {szerver_kassza} Arany."
# Ez a feladat az elmúlt napok összes vérzítékét megköveteli, a legelső string darabolásoktól kezdve a vadonatúj grafikonokig. Ha lefuttatod a végén, és felugrik egy ablak a saját játékos-statisztikáddal... az az igazi fejlesztői győzelem!