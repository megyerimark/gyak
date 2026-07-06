# 3. A Szabályok és a Logika:
# A) A Számoló Függvény (kaloria_kalkulator):
# Írj egy függvényt, ami az alap_kaloria értéket várja paraméterként, és tetszőleges számú rejtett nasit (*args).
# Hívd be a globális napi_osszkaloria változót!
# Add hozzá a globális változóhoz az alap kalóriát és a nasik összegét (tehát növeld meg az értékét).
# A függvény térjen vissza a nasikkal megnövelt adott étkezés kalóriájával (tehát ne az összessel, csak az alap_kaloria + nasik összegével)!
# B) A Főprogram (Fájlkezelés és Védőháló):
# Nyiss meg 3 fájlt egy with open blokkban:
# napi_makrok.txt (Olvasás - r).
# tiszta_makrok.txt (Írás - w).
# hibas_meresek.txt (Hozzáfűzés - a).
# Ugord át a fejlécet, és cikluson belül darabolj a pontosvessző (;) mentén.
# A Try Blokk:
# Szedd ki int-ként a Kalóriát (2. index) és a Fehérjét (3. index).
# Számold ki a Fehérjesűrűséget (hány százaléka a kalóriának a fehérje): (feherje * 4) / kaloria * 100. Az eredményt kerekítsd 1 tizedesjegyre (round), és mentsd egy suruseg változóba!
# Hívd meg a kaloria_kalkulator függvényt a kinyert kalóriával és két extra nasi értékkel (pl. 50, 120 kalória bedobásával). Az eredményét mentsd el egy vegleges_kaloria változóba!
# A Tuple konverzió: A 4. indexen lévő összetevőket (pl. "Csirkemell,Jazmin rizs...") vágd szét a vessző mentén, és alakítsd át Tuple-lé, hogy az összetevők listája megváltoztathatatlan maradjon. (Mentsd egy osszetevok_tuple változóba).
# A Szótár feltöltése: Add hozzá az adatokat a globális etkezesi_naplo szótárhoz! A Kulcs legyen a LOG_ID. Az Érték pedig egy Tuple, ami a következőket tartalmazza: (Kategoria, suruseg, osszetevok_tuple).
# Az Except Blokkok:
# IndexError: Írd a fájlba: "Hiányzó adat a mérésben: {adatok[0]}\n"
# ValueError: Írd a fájlba: "Hibás számformátum: {adatok[0]}\n"
# ZeroDivisionError: Írd a fájlba: "Nulla kalóriás étkezés (osztási hiba): {adatok[0]}\n"
# Az Else Blokk:
# Írd a tiszta_makrok.txt-be: "{adatok[0]} mentve. Kategória: {adatok[1]}. Fehérjesűrűség: {suruseg}%\n"
# A Finally Blokk:
# Képernyőre: "--- {adatok[0]} ellenőrzése lezárva ---"
# C) A Nagy Finálé (A legkívülre balra húzott sorok):
# Miután a ciklus és a fájlok bezárultak:
# Iterálj végig a feltöltött etkezesi_naplo szótáron a .items() segítségével, és printeld ki: "{kulcs} -> Makró profil: {ertek}"
# A legeslegutolsó sorban printeld ki a globális változót: "A napi összes kalóriabevitel (nasikkal együtt): {napi_osszkaloria} kcal."


napi_osszkaloria = 0
etkezesi_naplo = {}

def kaloria_kalkulator(alap_kaloria, *args):
    global napi_osszkaloria
    osszes_kal = sum(args)
    napi_osszkaloria += alap_kaloria + osszes_kal
    return osszes_kal

with open ("napi_makrok.txt", "r", encoding="utf-8") as napi:
    with open("tiszta_makrok.txt", "w", encoding="utf-8") as tiszta:
        with open("hibas_meresek.txt","a", encoding="utf-8") as hibas:
            next(napi)
            for makrok in napi:
                adatok = makrok.strip().split(";")
                try:
                    kaloria = int(adatok[2])
                    feherje = int(adatok[3])
                    suruseg = round(((feherje * 4) / kaloria * 100),1)
                    vegleges_kaloria =  kaloria_kalkulator(kaloria, 50,120)
                    osszetevok_tuple = tuple(adatok[4].split(","))
                    etkezesi_naplo[adatok[0]] = (adatok[1] , suruseg, osszetevok_tuple)
                except IndexError as i:
                    hibas.write(f"Hiányzó adatok a mérésben {adatok[0]}\n")
                except ValueError as v:
                    hibas.write(f"Hibás számformátum {adatok[0]}\n")
                except ZeroDivisionError as z:
                    hibas.write(f"Nulla kalóriás étkezés (osztási hiba): {adatok[0]}\n")
                else:
                    tiszta.write(f"{adatok[0]} mentve. Kategória: {adatok[1]}. Fehérjesűrűség: {suruseg}%\n")
                finally:
                    print(f"--- {adatok[0]} ellenőrzése lezárva ---")
for key, value in etkezesi_naplo.items():
    print(f"{key}-> Makró profil {value}")
print(f"A napi összes kalóriabevitel (nasikkal együtt): {napi_osszkaloria} kcal")
    