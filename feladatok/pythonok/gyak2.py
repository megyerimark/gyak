# 3. A Szabályok és a Logika:
# A) A Sebzés Függvény (kombó_sebzés)
# Írj egy függvényt, ami vár egy alap_csapas értéket (szám), és tetszőleges számú extra kombó sebzést (*args).
# A függvény adja össze ezeket, és térjen vissza a teljes kiosztott sebzéssel. (Itt most nem kell globális változóhoz adni semmit a függvényen belül).

# B) A Fájlbeolvasás és Adatszerkezet (For ciklus és Darabolás)
# Nyisd meg a szornyek.txt fájlt olvasásra.
# Ugord át a fejlécet, és egy for ciklussal menj végig a sorokon.
# Darabold fel a sorokat a pontosvessző (;) mentén.
# A Szótár feltöltése: A szorny_szotar Kulcsa legyen a Szörny ID-ja (pl. "S01"). Az Értéke pedig legyen egy Tuple, ami tartalmazza: (Nev, Eletpont (számmá alakítva!), Loot_Targyak).

# C) A Harci Ciklus (While, Try-Except, Szeletelés)
# Nyiss meg egy harci_naplo.txt fájlt hozzáfűzésre ("a").
# Ezen belül indíts egy while True: végtelen ciklust.
# Kérd be a játékostól: "Melyik szörnyet támadod? (S01/S02/S03 vagy 'kilepes'): "
# Ha "kilepes", törd meg a ciklust.
# Ha a beírt ID nincs benne a szótárban, írd ki: "Nincs ilyen szörny a zónában!", és ugorj a ciklus elejére (continue).
# Ha benne van, írd ki a képernyőre a szörny nevét a szótárból (emlékezz, az ID a kulcs, az érték 0. indexe a név!), majd kérj be egy alapsebzést az input()-tal: "Mekkora alapsebzést osztasz ki? "
# A Védőháló (Try-Except-Else):
# try: Próbáld meg az alapsebzést int-té alakítani.
# Hívd meg a kombó_sebzés függvényt az alapsebzéssel, és adj hozzá +50 és +120 bónusz sebzést (pl. kritikus csapás). Mentsd el az eredményt egy vegleges_sebzes változóba!
# except ValueError: Írd ki: "Melléütöttél! (Hibás számformátum)", és dobd vissza a ciklus elejére (continue).
# else: (Ha a sebzés sikeres volt):
# Húzd ki a szótárból a szörny életerejét (a Tuple 1. indexe), és vizsgáld meg egy if-fel: Ha a vegleges_sebzes nagyobb vagy egyenlő, mint a szörny életereje:
# Növeld meg a legyozott_szornyek_szama globális változót 1-gyel.
# Listaművelet és Szeletelés: Húzd ki a szótárból a zsákmányt (a Tuple 2. indexe). Ez még egy egyben lévő szöveg (pl. "Kard,Páncél,Tekercs"). Darabold fel a vesszők mentén listává, fordítsd meg a listát ([::-1]), és vedd ki belőle csak a legelső (0. indexű) elemet (ez lesz az Epic loot)!
# Írd ki a fájlba és a képernyőre is: "Legyőzted a(z) {szorny_neve}-t! Zsákmány: {epic_loot}."
# Ha a sebzés kisebb (elif vagy else):
# Írd ki a fájlba és a képernyőre is: "A(z) {szorny_neve} túlélte a támadást! Kiosztott sebzés: {vegleges_sebzes}."

# 4. Zárás
# A program legvégén (minden behúzásból kilépve) printeld ki:
# "A harctér kiürült. Összesen legyőzött szörnyek száma: {legyozott_szornyek_szama}."
# Ez a kód egy komplett mini-játék szerveroldali logikája. Kombinálja a fájlból való betöltést (adatbázis építés), a felhasználói inputot, a matematikai függvényeket, a hibaellenőrzést és a listák/szeletelések manipulációját.


# A) A Sebzés Függvény (kombó_sebzés)
# Írj egy függvényt, ami vár egy alap_csapas értéket (szám), és tetszőleges számú extra kombó sebzést (*args).
# A függvény adja össze ezeket, és térjen vissza a teljes kiosztott sebzéssel. (Itt most nem kell globális változóhoz adni semmit a függvényen belül).#

szorny_szotar = {}
legyozott_szornyek_szama = 0

def kombo_sebzes(alap_csapas, *args):
    global legyozott_szornyek_szama
    teljes_sebzes = alap_csapas + sum(args)
    return teljes_sebzes
with open("szornyek.txt", "r", encoding="utf-8") as moobs:
    next(moobs)
    for l in moobs:
        adatok =l.strip().split(";")
        szorny_szotar[adatok[0]] = (adatok[1], int(adatok[2]), adatok[3])  
with open("harci_naplo.txt", "a", encoding='utf-8') as fight:
    while True:
        bemenet = input("Melyik szörnyet támadod? (S01/S02/S03 vagy 'kilepes'):")
        if bemenet == "kilepes":
            break
        if bemenet not in szorny_szotar:
            print("Nincs ilyen szörny a zónában!")
            continue
        else:
            print(f"{szorny_szotar[bemenet][0]}")
            bemenet2 = input("Mekkora alapsebzést osztasz ki?")
        try:
            sebzes = int(bemenet2)
            vegleges_sebzes = kombo_sebzes(sebzes, 50,120)
        except ValueError as v:
            print("Melléütöttél! (Hibás számformátum)")
            continue
        else:
            if vegleges_sebzes >= szorny_szotar[bemenet][1]:
                legyozott_szornyek_szama += 1
                epic_loot = szorny_szotar[bemenet][2].split(",")[::-1][0]
            # if vegleges_sebzes >= adatok[2]:
            # if vegleges_sebzes >= szorny_szotar[bemenet][1]:
            #     legyozott_szornyek_szama += 1
            #     # epic_loot = szorny_szotar[adatok[3]].split(",")[::-1]
            #     epic_loot = szorny_szotar[bemenet][2].split(",")[::-1][0]
                print(f"Legyőzted a(z) {epic_loot[1]}-t! Zsákmány: {epic_loot[2]}.")
                print(f"Legyőzted a(z) {szorny_szotar[bemenet][0]}-t! Zsákmány: {epic_loot}.")                
                fight.write(f"Legyőzted a(z) {epic_loot[1]}-t! Zsákmány: {epic_loot[2]}.")

# print(f"Legyőzted a(z) {szorny_szotar[bemenet][0]}-t! Zsákmány: {epic_loot}.")                fight.write(f"Legyőzted a(z) {epic_loot[1]}-t! Zsákmány: {epic_loot[3]}.")
# print(f"A harctér kiürült. Összesen legyőzött szörnyek száma: {legyozott_szornyek_szama}.")
            
