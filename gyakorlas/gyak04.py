
print("******************************************************************")
print("1. Részfeladat: A Titkos Tekercs (Stringek és Ciklusok Találtál egy varázstekercset, de egy gonosz varázsló teleírta 'X' betűkkel, hogy elrejtse a valódi szöveget. Meg kell tisztítanod!")

# Feladat:
# Menj végig egy for ciklussal a tekercs betűin.
# Egy if feltétellel vizsgáld meg, hogy az aktuális betű NEM egyenlő-e "X"-szel és NEM egyenlő-e "x"-szel. (Használd a != operátort és az and szócskát!).
# Ha a betű nem iksz, akkor add hozzá a tiszta_szoveg változóhoz! (Stringeket a += operátorral tudsz egymáshoz fűzni).
# A ciklus végén (a cikluson kívül) írd ki: "A megfejtés: [tiszta_szoveg]"


tekercs = "VxaXrXaXzXsXlXaXtX"
tiszta_szoveg = ""

for betuk in tekercs:
    if betuk != "X" and betuk != "x":
        tiszta_szoveg += betuk
print(f"A megfejtés: [{tiszta_szoveg}]")
        

print("******************************************************************")
print("2. Részfeladat: A Makacs Troll (While ciklus Egy barlangi troll állja utadat. A troll nagyon makacs, ráadásul a hősöd most fáradt, így a sebzése véletlenszerű. (Ne aggódj, az alap logikát már tudod, csak a behúzásokra figyelj!)")

# Feladat:
# Írj egy while ciklust, ami addig fut, amíg a troll_hp nagyobb, mint 0.
# A ciklusban először növeld meg az utesek_szama értékét 1-gyel.
# Utána vonj le a troll életerejéből fixen 4-et (ez a sebzésed).
# A cikluson kívül (amikor a troll már meghalt), egy if-else blokkal vizsgáld meg: Ha az ütések száma kevesebb vagy egyenlő, mint 4, írd ki: "Gyors győzelem!". Ha több, írd ki: "Kemény harc volt!".
troll_hp = 15
utesek_szama = 0

while troll_hp > 0:
    utesek_szama +=1
    troll_hp -= 4
    
if utesek_szama <= 4:
    print("Gyors győzelem!")
else:
    print("Kemény harc volt!")

print("******************************************************************")
print("3. Részfeladat: A Kereskedőnél (Listák, Szótárak és For ciklus) A harcok után betérsz a városi boltba. Van egy bevásárlólistád, a kereskedőnek pedig egy ártáblázata. Ki kell számolnod, mennyi aranyba fog kerülni a vásárlás!")

# Feladat:
# Nem kell függvényt (def) írnod! Csak egy sima for ciklussal menj végig a bevasarlo_lista elemein.
# A cikluson belül vizsgáld meg (if), hogy az aktuális tárgy benne van-e a bolt_arak szótárban.
# Ha benne van, akkor a bolt_arak szótárból olvasd ki az adott tárgy árát, és add hozzá (+=) a vegosszeg változóhoz! (Tipp: vegosszeg += bolt_arak[aktualis_targy]).
# A legvégén nyomtasd ki: "A vásárlás teljes költsége: [vegosszeg] arany."

bolt_arak = {"kard": 15, "pajzs": 10, "alma": 2, "kötél": 5}
bevasarlo_lista = ["kard", "alma", "alma", "kötél"]
vegosszeg = 0


for targy in bevasarlo_lista:
    if targy in bolt_arak:
        vegosszeg+= bolt_arak[targy]
print(f"A vásárlás teljes költsége: [{vegosszeg}] arany")
        