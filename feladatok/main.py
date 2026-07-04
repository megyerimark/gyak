# A Szabályok és a Logika:

# A) A Bevételszámoló Függvény (kasszakezelo):
# Írj egy függvényt, ami egy kötelező fizetett_osszeg paramétert vár, és tetszőleges számú extra tranzakciós költséget (*args).
# Hívd be a globális getingo_kassza változót!
# A függvény adja össze az eredeti fizetett_osszeg-et és az *args-ban lévő extra bevételeket (pl. szállítási díj, csomagolás).
# Ezt a teljes összeget add hozzá tartósan a getingo_kassza globális változóhoz.
# A függvény térjen vissza (return) ezzel a teljes kiszámolt bevétellel!

# B) A Főprogram (Fájlkezelés és Hibakezelés):
# Nyiss meg 3 fájlt egyetlen with open blokkban:
# getingo_tranzakciok.txt (Olvasásra).
# konyveles.txt (Írásra).
# csalas_gyanu.txt (Hozzáadásra).
# Menj végig a beolvasott sorokon egy for ciklussal, és darabold fel őket a pontosvessző (;) mentén.
# A Try Blokk:
# Szedd ki és alakítsd int-té a Fizetett Összeget (2. index) és a Darabszámot (3. index).
# Számold ki az Egységárat: oszd el a fizetett összeget a darabszámmal! (egyseg_ar = osszeg / darab).
# Hívd meg a kasszakezelo függvényedet! Add át neki a fizetett összeget, és pluszban dobj be neki két tetszőleges extra számot argumentumként (mondjuk 1500 szállítási díj és 500 csomagolási díj). Az eredményt mentsd el egy vegleges_bevetel változóba!
# Az Except Blokkok (Írás a csalás fájlba):
# IndexError: Írd a fájlba: "Hiányos tranzakció: {adatok[0]}\n"
# ValueError: Írd a fájlba: "Adathiba: {adatok[0]}\n"
# ZeroDivisionError: Írd a fájlba: "Sztornózva (0 darab): {adatok[0]} - {adatok[1]}\n"
# Az Else Blokk (Írás a könyvelésbe):
# Írd a konyveles.txt-be:
# "{adatok[0]} rögzítve. Termék: {adatok[1]}. Egységár: {egyseg_ar} Ft.\n"
# A Finally Blokk:
# Printeld a képernyőre: "--- {adatok[0]} feldolgozása lezárult ---"

# C) A Program Legvége (A ciklus után):
# Miután a for ciklus és a fájlkezelés teljesen lefutott (lépj ki a behúzásokból!), a legutolsó sorban printeld ki a képernyőre:
# "A Getingo napi záró egyenlege: {getingo_kassza} Ft."
# Az Elvárt Eredmény:
# A terminálban végigfut az 5 darab feldolgozási üzenet, a legvégén pedig a záró egyenleg (aminek pontosan 148000.0 Ft-nak kell lennie). A mappádban pedig ez a két fájl fog keletkezni:

getingo_kassza = 0.0
def kasszakezelo(fizetett_osszeg = 340, *args):
    global getingo_kassza
    csomagolas = sum(args) + fizetett_osszeg
    getingo_kassza += csomagolas
    return getingo_kassza
with open ("getingo_tranzakciok.txt", "r", encoding="utf-8") as r:
    with open ("konyveles.txt", "w", encoding="utf-8") as w:
        with open("csalas_gyanu.txt", "a", encoding="utf-8") as a :
            for adatok in r:
                sor = adatok.strip().split(";")
                try:
                    osszeg = int(sor[2])
                    darab = int(sor[3])
                    egyseg_ar = osszeg / darab
                    vegleges_bevetel = kasszakezelo(osszeg,   1500,500)
                except IndexError as i:
                    a.write(f" - Hiányos tranzakció:  {sor[0]}\n")
                except ValueError as v:
                    a.write(f" -Adathiba: {sor[0]}\n  ")
                except ZeroDivisionError as z :
                    a.write(f" -Sztornózva: {sor[0]} - {sor[1]}\n")
                else:
                    w.write(f"{sor[0]} rögzítve. Termék: {sor[1]}. Egységár: {egyseg_ar} Ft.\n ")
                finally:
                    print(f"{sor[0]} feldolgozása lezárult ---")
print(f"A Getingo napi záró egyenlege: {getingo_kassza} Ft.")
