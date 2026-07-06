csomagok = {"Alap": 5000, "Pro": 15000, "VIP": 45000}

def fizetes_ellenorzes(kartya_szam):
    kartya_szam = len(csomagok)
    while kartya_szam == kartya_szam :
        return True
    else:
        return False



    

# A Kihívás: A Getingo Moduláris Fizetési Rendszere
# Ehhez a feladathoz két külön Python fájlt kell létrehoznod ugyanabban a mappában!

# 1. Fájl: stripe_modul.py (A te saját alkatrészed)
# Ebben a fájlban semmilyen print, while vagy futtatható kód nem lehet. Ez egy tiszta adat- és logika-tároló modul.

# Hozz létre benne egy globális Szótárat (Dictionary) a Getingo szolgáltatásaival:
# csomagok = {"Alap": 5000, "Pro": 15000, "VIP": 45000}

# Írj egy függvényt: def fizetes_ellenorzes(kartya_szam):

# A függvény feladata csak annyi, hogy megnézi a kártyaszám hosszát a len() paranccsal.

# Ha a hossz pontosan 16 karakter, térjen vissza (return) True értékkel.

# Minden más esetben térjen vissza False értékkel.

# 2. Fájl: getingo_vezerlo.py (A Főprogramod)
# Ez az a fájl, amit majd le fogsz futtatni.

# Az Import: A fájl legelső sorában importáld be a saját modulodat! (Ahogy a videóban láttad: import stripe_modul).

# Induló adat: napi_bevetel = 0

# Nyiss meg egy sikeres_fizetesek.txt fájlt hozzáfűzésre ("a" mód) egy with open blokkal.

# A While Ciklus: A with open blokkon belül indíts egy végtelenített while True: ciklust (hogy a bolt folyamatosan nyitva legyen).

# A cikluson belül kérd be egy input()-tal: "Melyik csomagot kéred? (Alap/Pro/VIP vagy 'kilepes'): " és mentsd el egy változóba (pl. valasztott_csomag).

# Ha a válasz "kilepes", akkor a break paranccsal törd meg a ciklust (zárd be a boltot).

# Ha a valasztott_csomag nincs benne a modulod szótárában (Hivatkozás: stripe_modul.csomagok), akkor printeld ki: "Nincs ilyen csomag!", és a continue paranccsal ugorj vissza a ciklus elejére.

# Ha van ilyen csomag, kérd be a kártyaszámot egy input()-tal.

# Kérj be egy Borravalót/Támogatást is egy input()-tal: "Támogatás a fejlesztőnek (Ft): "

# A Try-Except-Else Blokk:

# Próbáld meg int-té alakítani a támogatást. Ha sikerül, számold ki a teljes_osszeg-et: add hozzá a támogatást a csomag modulból kiolvasott árához (stripe_modul.csomagok[valasztott_csomag]).

# ValueError esetén: Printeld ki: "Hibás összeg, tranzakció megszakítva!", majd continue.

# Else ágban (ha a matek sikeres): Hívd meg a modulod ellenőrző függvényét a kártyaszámmal: if stripe_modul.fizetes_ellenorzes(kartya_szam) == True:

# Ha True: Add hozzá a napi_bevetel-hez a teljes összeget, printeld ki a képernyőre, hogy "Sikeres fizetés!", és írd bele a .txt fájlba: "{valasztott_csomag} eladva. Bevétel: {teljes_osszeg} Ft\n"

# Ha False (vagyis else: az if-hez): Printeld ki a képernyőre: "Elutasítva: Érvénytelen kártyaszám!"

# 3. A Nagy Finálé
# Miután valaki beírta, hogy "kilepes", a while ciklus megtörik. A fájl legeslegvégén (kilépve minden behúzásból, a bal szélre igazítva) printeld ki:
# "A Getingo terminál lezárva. Napi bevétel: {napi_bevetel} Ft."

# Hogyan teszteld a kész programot?
# Indítsd el a getingo_vezerlo.py-t.

# Kérj egy "Pro" csomagot, adj meg egy véletlenszerű borravalót (pl. 1000), és adj meg egy 16 karakteres kártyaszámot (pl. 1234123412341234). Látnod kell a sikert.

# Kérj egy "VIP" csomagot, de a kártyaszámhoz írj be csak 3 számot. El kell, hogy utasítson a modulod.

# Kérj egy "Alap" csomagot, de borravalónak írd be azt a szót, hogy "sok". A try-except meg kell, hogy fogja.

# Írd be, hogy kilepes. Látnod kell a végső összeget.