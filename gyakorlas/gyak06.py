print("***************************************")
print("1. Részfeladat: A Céh Küldetés-Táblája (Fájlolvasás)")
# A feladat:
# Használd a ma tanult, legbiztonságosabb fájlmegnyitási módot: with open(...) as file: (Így a gép magától lezárja, nem kell a close()-ra figyelned!)
# A with blokkon belül olvass be minden sort a fájlból. (Használhatod a while sor: logikát a readline()-nal, vagy a zseniális for sor in file: ciklust).
# Írasd ki a képernyőre a küldetéseket, de figyelj rá, hogy ne legyenek dupla sorközök! (Használd a .strip() metódust a felesleges "levegő" levágására).

with open ("gyakorlas/kuldetesek.txt", "r", encoding="utf-8") as file:
    sor = file.readline()
    while sor:
        print(sor.strip())
        sor = file.readline()
    
    
    
print("***************************************")
print("2. Részfeladat: A Kocsmai Szkander-Bajnokság (Beépített függvények)")
# A versenyzok listáját írasd ki visszafelé, úgy, hogy egy igazi, olvasható lista legyen! (Tipp: használd a list() és a reversed() függvényeket egymásba ágyazva).
# Keresd meg a legnagyobb és a legkisebb erőt az eropontok listában a megfelelő beépített függvényekkel (max, min), és írd ki őket: "A leggyengébb ütés: [X], a legerősebb: [Y]"
# Az egyik versenyző erejét fel akarjuk erősíteni mágikusan a négyzeten! Használd a pow() függvényt, hogy kiszámold a 10-es szám 3. hatványát, és írd ki az eredményt!
# Végül: használd az enumerate() függvényt egy for ciklusban, hogy megszámozd és kiírd a versenyzők neveit. (Tipp: for index, nev in enumerate...)

versenyzok = ["Thor", "Gimli", "Hulk", "Kratos"]
eropontok = [142, 89, 255, 198]
#1
print(list(versenyzok.__reversed__()))
#2
min_ero = min(eropontok)
max_ero = max(eropontok)
print(f"A leggyengébb ütés: [{min_ero}], a legerősebb [{max_ero}]")
#3
print(pow(10, 3))

#4
for index, nev in enumerate(versenyzok):
    print(index, nev)
    
    
    
print("***************************************")
print("3. Részfeladat: A Főmágus Kombó Varázslata (Scope, Return és *args)")

# A feladat:
# Írj egy varazslat() nevű függvényt! Ennek legyen egy fix paramétere alapértelmezett értékkel (pl. alap_koltseg = 10), és fogadjon be akármennyi extra költséget (használd a *args varázsszót!).
# A függvény belsejében mondd meg a gépnek, hogy te a kinti, igazi kristályt akarod módosítani! (Tipp: használd a global kulcsszót a kristaly_mana előtt).
# Számold ki a varázslat teljes költségét: add össze az alap_koltseg-et és az összes számot, amit az *args-ban kaptál. (Tipp: ahogy a jegyzetedben is van, az args-on végigmehetsz egy for ciklussal, vagy használhatod rá a sum() függvényt).
# Ezt a kiszámolt teljes költséget vond le (-=) a globális kristaly_mana értékéből!
# A függvény legvégén térj vissza (return) azzal a szöveggel, hogy mennyi mana maradt a kristályban.
# A főprogramban (kint) hívd meg a függvényt kétszer:
# Először csak egy sima lövéssel: varazslat() (Itt csak az alap 10-es költség vonódik le).
# Másodszor egy hatalmas kombóval: varazslat(20, 15, 30, 50) (Itt az alap 20 lesz, az extra pedig a többi).
# Mivel a függvény return-nel adja vissza az eredményt, ne felejtsd el egy print()-be csomagolni a meghívást, hogy lásd is a szöveget a képernyőn!

kristaly_mana = 1000
def varazslat(alap_koltseg = 10, *args):
    global kristaly_mana
    fizetendo = alap_koltseg + sum(args)
    kristaly_mana-= fizetendo
    return f"A kristályban maradt: {[kristaly_mana]}"

print(varazslat(20, 15, 30, 50))