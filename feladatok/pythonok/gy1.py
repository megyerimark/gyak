# 3. A Szabályok és a Logika:

# A) A Statisztika Függvény (kattintas_szamolo):
# Írj egy függvényt, ami a letoltott_oldalak számát várja paraméterként, és tetszőleges számú rejtett extra kattintást (*args).
# Hívd be a globális osszes_kattintas változót!
# Add hozzá a globális változóhoz a letoltott_oldalak-at és az *args-ban lévő számok összegét (tehát növeld meg az értékét).
# A függvény térjen vissza (return) az eredeti letoltott_oldalak számával!
# B) A Főprogram (Fájlkezelés és Védőháló):
# Nyiss meg 3 fájlt egyetlen with open blokkban:
# getingo_latogatok.txt (Olvasás - r).
# tiszta_analitika.txt (Írás - w).
# hibas_log.txt (Hozzáfűzés - a).
# Cikluson belüli darabolás a pontosvessző (;) mentén.
# A Try Blokk:
# Szedd ki int-ként az Eltöltött másodpercet (2. index) és a Letöltött oldalakat (3. index).
# Hívd meg a kattintas_szamolo függvényt a letöltött oldalakkal és néhány extra számmal (pl. 2, 4), és az eredményét mentsd el egy oldalak változóba!
# Számold kiaz Aktivitási Indexet: Oszd el az Eltöltött másodpercet az oldalak számával, és kerekítsd (round) 1 tizedesjegyre!
# A Tuple konverzió: A 4. indexen lévő URL-eket (pl. "Kezdőlap,Blog") vágd szét a vessző (,) mentén egy listává a .split(",") paranccsal. 
# Mivel a látogatási előzményeket biztonsági okokból tilos módosítani, ezt a friss listát alakítsd át Tuple-lé, és mentsd el egy url_tuple nevű változóba!
# A Szótár feltöltése: Add hozzá a feldolgozott adatokat a globális aktiv_felhasznalok szótárhoz! 
# A Kulcs (Key) legyen az USR-azonosító (0. index). Az Érték (Value) pedig legyen egy vadonatúj Tuple, ami a következőket tartalmazza: (Név, Aktivitási_Index, url_tuple).
# Az Except Blokkok:
# IndexError: Írd a fájlba: "Hiányos adat: {ID}"
# ValueError: Írd a fájlba: "Formátum hiba: {ID}"
# ZeroDivisionError: Írd a fájlba: "Inaktív felhasználó (0 oldal): {ID}"
# Az Else Blokk:
# Írd a tiszta_analitika.txt-be: "{ID} feldolgozva. Aktivitás: {aktivitasi_index}"
# A Finally Blokk:
# Képernyőre: "--- {ID} futtatás kész ---"
# C) A Nagy Finálé (A legkívülre balra húzott sorok):
# Miután az összes fájl bezárult:
# Egy új for ciklus segítségével iterálj végig a feltöltött aktiv_felhasznalok szótár elemein a frissen tanult .items() metódussal! A ciklus belsejében printeld ki a képernyőre: "{kulcs} -> Értékek: {ertek}"
# A legeslegutolsó sorban printeld ki a globális változódat: "A Getingo rendszeren regisztrált összes kattintás: {osszes_kattintas}"

osszes_kattintas = 0
aktiv_felhasznalok = {}

def kattintas_szamlalo(letoltott_oldalak, *args):
    global osszes_kattintas
    osszes = sum(args)
    osszes_kattintas += osszes + letoltott_oldalak
    return letoltott_oldalak

with open ("getingo_latogatok.txt", "r", encoding="utf-8") as latogatok:
    with open ( "tiszta_analitika.txt", "w" ,encoding="utf-8") as analatika:
        with open ("hibas_log.txt", "a", encoding="utf-8") as hibas:
            next(latogatok) # azért az 1-es mert az. sorba bele tettem a fejlécet. 
            for sorok in latogatok:
                adatok = sorok.strip().split(";")
                try:
                    masodperc = int(adatok[2])
                    oldalak = int(adatok[3])
                    vegso_oldal = kattintas_szamlalo(oldalak, 2 ,4 )
                    aktivitas = round(masodperc / oldalak , 1)
                    url_tuple = tuple(adatok[4].split(","))
                    aktiv_felhasznalok[adatok[0]] = (adatok[1], aktivitas, url_tuple) 
                    # A Szótár feltöltése: Add hozzá a feldolgozott adatokat a globális aktiv_felhasznalok szótárhoz! A Kulcs (Key) legyen az USR-azonosító (0. index). 
                    # Az Érték (Value) pedig legyen egy vadonatúj Tuple, ami a következőket tartalmazza: (Név, Aktivitási_Index, url_tuple)
                except IndexError as i :
                    hibas.write(f"Hiányos adat: {adatok[0]}\n")
                except ValueError as v:
                    hibas.write(f"Formátum hiba: {adatok[0]}\n")
                except ZeroDivisionError as z:
                    hibas.write(f"Inaktív felhasználó (0 oldal): {adatok[0]}\n")
                else:
                    analatika.write(f"{adatok[0]} feldolgozva. Aktivitás: {aktivitas}\n")
                finally:
                    print(f"--- {adatok[1]} futtatás kész ---")
for id, values in aktiv_felhasznalok.items():
    print(id, values)
print(f"A Getingo rendszeren regisztrált összes kattintás: {osszes_kattintas}")