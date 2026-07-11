berletek = {"1001": 15, "1002": 0, "1003": 30, "1004": -2}


def jogosultsag(kartya_szam): 
    if berletek[kartya_szam] > 0:
        return True
    else:
        return False
        
        
        
#         1. Fájl: lotus_adatbazis.py (A Modulod)
# Ez a háttérrendszer, ami a tagok bérletének érvényességét tárolja.

# Hozd létre benne a globális Szótárat (Dictionary):
# berletek = {"1001": 15, "1002": 0, "1003": 30, "1004": -2}
# (A kulcs a kártyaszám szövegként, az érték pedig a bérletből hátralévő napok száma).

# Írj egy függvényt: def jogosultseg(kartya_szam):

# A függvény nézze meg, hogy a kapott kártyaszámhoz tartozó érték (a hátralévő napok) a szótárban nagyobb-e, mint 0.

# Ha nagyobb, térjen vissza True értékkel.

# Ha 0 vagy negatív (mert mondjuk lejárt, de még jött utána), térjen vissza False értékkel.
# (Tipp: Ne feledd, a kártyaszámmal hivatkozol a szótár elemére: berletek[kartya_szam])

# 2. Fájl: recepcio.py (A Főprogramod)
# Ez fut a pultnál lévő gépen.

# Az Import: Importáld be a modulodat (pl. import lotus_adatbazis as adatbazis).

# Induló adat: napi_belepok = 0

# Nyiss meg egy lotus_naplo.txt fájlt hozzáfűzésre ("a").

# A Végtelen Ciklus: Nyisd meg a while True: csövet a with open blokkon belül!

# Kérd be a kártyát: "Kérem a kártyaszámot (vagy 'zaras'): "

# Ha a válasz "zaras", törd meg a ciklust (break).

# Ha a válasz nincs benne a modulod szótárában, printeld: "Ismeretlen kártya, kérjük regisztráljon!", és azonnal dobd vissza a ciklus elejére (continue).

# Ha létezik a kártya, kérd be az extrát: "Kérsz edzés utáni fehérjeturmixot? (Hány adagot? 0-5): "

# A Védőháló (Try-Except-Else):

# A try blokkban próbáld meg int-té (egész számmá) alakítani a turmix adagot. (Mentsd egy adag változóba).

# Except ValueError: Printeld: "Hibás adatbevitel, kérjük számot adjon meg!", és dobd vissza az elejére (continue).

# Az Else ág (A szív): Hívd meg a modulod ellenőrző függvényét! if adatbazis.jogosultseg(kartya_szam) == True:

# Ha True: Növeld meg a napi_belepok számát 1-gyel. Printeld a képernyőre: "Sikeres belépés a Lotus terembe!", és írd bele a fájlba: "{kartya_szam} belépett. Kért fehérje: {adag} adag.\n"

# Ha False: Printeld a képernyőre: "Belépés megtagadva: A bérleted lejárt, fáradj a kasszához!"

# 3. A Nap Vége
# Kilépve az összes behúzásból, a legeslegutolsó sorba (a bal szélre) printeld ki:
# "A Lotus recepció bezárt. Mai sikeres belépők száma: {napi_belepok} fő."

# A Tesztelés (Így törd fel a saját kódod):

# Próbálj belépni az 1001-es kártyával, és kérj 2 adag fehérjét (Sikeres belépést kell kapnod).

# Próbálj belépni az 1002-es kártyával (El kell utasítania lejárt bérlet miatt).

# Próbálj belépni egy 9999-es kártyával (Ismeretlen kártya hiba, majd újrakérdezés).

# Próbálj belépni az 1003-assal, de a fehérjéhez írd be, hogy "kettő" (A Try-exceptnek meg kell fognia, és nem engedheti be).

# Írd be: zaras.