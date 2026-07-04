# # 1#. Részfeladat: Biztonsági beléptetés (Ciklusok, Input, Feltételek)
# # #Készíts egy beléptető rendszert a szuperadmin felülethez.
# # #Legyen egy helyes_jelszo változód (pl. "admin123").
# # Kérd be a felhasználótól a jelszót az input() segítségével.
# # Összesen 3 próbálkozása lehet (használj egy számlálót).
# # Ha elrontja, írd ki, hogy "Hibás jelszó!", és kérd be újra.
# # Ha eléri a 3 hibát, írd ki, hogy "Rendszer lezárva", és a break segítségével lépj ki a ciklusból.
# # Ha eltalálja, írd ki: "Sikeres belépés a vezérlőpultba!" és engedd tovább.

# 2. Részfeladat: Ingatlanos adatok tisztítása (Függvények, Típusvizsgálat, Lista metódusok)
# Kaptál egy "szemetes" listát az adatbázisból, amiben az ingatlanosok nevei közé hibás adatok (számok, boolean értékek) keveredtek.
# nyers_adatok = ["Kiss Piroska", "Nagy Zsombor", 104, True, "Kovács Anna", 3.14, "Tóth Gábor"]
# Írj egy adat_tisztito(lista) nevű függvényt.
# Hozz létre a függvényen belül egy üres listát: tiszta_nevek = [].
# Menj végig a kapott listán egy for ciklussal.
# Az isinstance() segítségével vizsgáld meg, hogy az adott elem str (szöveg) típusú-e.
# Ha igen: Konvertáld csupa nagybetűssé (a .upper() metódussal), és az .append() segítségével add hozzá a tiszta_nevek listához.
# Ha nem: Írd ki a terminálba: "Hibás adat észlelve, típusa: [ide jöjjön a típus]" (használd a type()-ot).
# A függvény legvégén rendezd ABC sorrendbe a megtisztított listát a .sort() segítségével, és írasd ki a képernyőre!

# 3. Részfeladat: Naptár és időpontkezelés (Listák listája, Szeletelés, Continue)
# A rendszerben egy ingatlanos napi naptára listák listájaként van tárolva. Minden belső lista első eleme az óra, a második az állapota.
# naptar = [ [8, "Szabad"], [9, "Foglalt"], [10, "Szabad"], [11, "Foglalt"] ]
# A nap elején a rendszernek ki kell listáznia a szabad időpontokat. Egy for ciklussal menj végig a naptar-on. Ha az időpont állapota "Foglalt", használd a continue parancsot a ciklus ugrásához. Ha "Szabad", írd ki: "Elérhető időpont: [óra] óra".
# Jött egy új foglalás reggel 8-ra! Módosítsd a naptar lista első elemének (a 8 órásnak) a második értékét "Foglalt"-ra (szeletelés/indexelés használatával).
# Túlóra! Az ingatlanos bevállalt egy új időpontot délben. Az .insert() vagy az .append() metódussal adj hozzá egy új elemet a naptár végéhez: [12, "Szabad"].

# # 1#. Részfeladat: Biztonsági beléptetés (Ciklusok, Input, Feltételek)
# # #Készíts egy beléptető rendszert a szuperadmin felülethez.
# # #Legyen egy helyes_jelszo változód (pl. "admin123").
# # Kérd be a felhasználótól a jelszót az input() segítségével.
# # Összesen 3 próbálkozása lehet (használj egy számlálót).
# # Ha elrontja, írd ki, hogy "Hibás jelszó!", és kérd be újra.
# # Ha eléri a 3 hibát, írd ki, hogy "Rendszer lezárva", és a break segítségével lépj ki a ciklusból.
# # Ha eltalálja, írd ki: "Sikeres belépés a vezérlőpultba!" és engedd tovább.

print('********************************')
print('1. Részfeladat: Biztonsági beléptetés (Ciklusok, Input, Feltételek)')
jelszo = "admin123"
bemenet = input("Kérlek add meg a jelszavad: ")
proba =0

while bemenet != jelszo:
    proba += 1
    if proba == 3:
        print("Rendszer lezárva! Próbálkozások száma :" ,proba)
        break
    print("Hibás jelszó")
    bementet = input("Mi a jelszavad? ")
if bemenet == jelszo:
    print("Sikeres belépés a vezérlőpultba!")
    
    
# 2. Részfeladat: Ingatlanos adatok tisztítása (Függvények, Típusvizsgálat, Lista metódusok)
# Kaptál egy "szemetes" listát az adatbázisból, amiben az ingatlanosok nevei közé hibás adatok (számok, boolean értékek) keveredtek.
# nyers_adatok = ["Kiss Piroska", "Nagy Zsombor", 104, True, "Kovács Anna", 3.14, "Tóth Gábor"]
# Írj egy adat_tisztito(lista) nevű függvényt.
# Hozz létre a függvényen belül egy üres listát: tiszta_nevek = [].
# Menj végig a kapott listán egy for ciklussal.
# Az isinstance() segítségével vizsgáld meg, hogy az adott elem str (szöveg) típusú-e.
# Ha igen: Konvertáld csupa nagybetűssé (a .upper() metódussal), és az .append() segítségével add hozzá a tiszta_nevek listához.
# Ha nem: Írd ki a terminálba: "Hibás adat észlelve, típusa: [ide jöjjön a típus]" (használd a type()-ot).
# A függvény legvégén rendezd ABC sorrendbe a megtisztított listát a .sort() segítségével, és írasd ki a képernyőre!

            
print('********************************')
print('2. Részfeladat: Ingatlanos adatok tisztítása (Függvények, Típusvizsgálat, Lista metódusok)')
nyers_adatok = ["Kiss Piroska", "Nagy Zsombor", 104, True, "Kovács Anna", 3.14, "Tóth Gábor"]

def adat_tisztito(nyers_adatok):
    tiszta_nevek = []
    for tnev in nyers_adatok:
        if isinstance(tnev,str):
            tiszta_nevek.append(tnev.upper())
        else:
            print(type(tnev), "Hibás Adatok!")
    tiszta_nevek.sort()
    print(tiszta_nevek)
adat_tisztito(nyers_adatok)

# 3. Részfeladat: Naptár és időpontkezelés (Listák listája, Szeletelés, Continue) kész
# A rendszerben egy ingatlanos napi naptára listák listájaként van tárolva. Minden belső lista első eleme az óra, a második az állapota. kész
# naptar = [ [8, "Szabad"], [9, "Foglalt"], [10, "Szabad"], [11, "Foglalt"] ] kész
# A nap elején a rendszernek ki kell listáznia a szabad időpontokat. Egy for ciklussal menj végig a naptar-on. Ha az időpont állapota "Foglalt", használd a continue parancsot kész
# a ciklus ugrásához. Ha "Szabad", írd ki: "Elérhető időpont: [óra] óra". kész
# Jött egy új foglalás reggel 8-ra! Módosítsd a naptar lista első elemének (a 8 órásnak) a második értékét "Foglalt"-ra (szeletelés/indexelés használatával).
# Túlóra! Az ingatlanos bevállalt egy új időpontot délben. Az .insert() vagy az .append() metódussal adj hozzá egy új elemet a naptár végéhez: [12, "Szabad"].

            
            
print('********************************')
print('3. Részfeladat: Naptár és időpontkezelés (Listák listája, Szeletelés, Continue)')

naptar = [ [8, "Szabad"], [9, "Foglalt"], [10, "Szabad"], [11, "Foglalt"] ]

for  ora, allapot in naptar:
    if allapot =="Foglalt":
        continue
    else:
        print("Elérhető időpont: ", ora, "óra")
naptar[0][1] = "Foglalt"
naptar.append([12, "Szabad"])     
print(naptar)
naptar




        

print('********************************')


        

