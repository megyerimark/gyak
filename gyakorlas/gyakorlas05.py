print("*******************************************")
print("1. Részfeladat: A Titkos Kincstár (Dupla ciklus és Kétdimenziós lista)A hősöd belép egy 3x3-as rácsból álló kincstárba. Minden sornak megvan a maga tartalma. Végig kell vizsgálnod az egész szobát")
# A feladat:
# Írj egy úgynevezett beágyazott for ciklust! Az első ciklus a sorokon menjen végig (pl. for sor in kincstar:), a második, belső ciklus pedig magán a soron (pl. for mezo in sor:). Figyelj a behúzásokra!
# A belső cikluson belül egy if-elif blokkal vizsgáld meg az aktuális mezo értékét!
# Ha az érték "Arany" vagy "Gyémánt", írd ki: "Találtam egy [mezo]-t!"
# Ha az érték "Csapda", írd ki: "Vigyázat, csapda!"
# Minden más esetben (else - ha "Üres"), használd a continue parancsot a csendes továbblépéshez!

kincstar = [
    ["Üres", "Arany", "Üres"],
    ["Üres", "Üres", "Csapda"],
    ["Gyémánt", "Üres", "Üres"]
]

for sor in kincstar:
    for mezo in sor:
        if mezo == "Arany" or mezo == "Gyémánt":
            print(f"Találtam egy [{mezo}]")
        elif  mezo == "Csapda":
            print("Vigyázat, csapda!")
        else:
            mezo == "Üres"
            continue
            
    
        
        
print("*******************************************")
print("2. Részfeladat: A Fegyvermester Raktára (Dupla indexelés és Lista bővítés)A fegyvermester a készletét egy listákból álló listában vezeti. Az első elem mindig a név, a második a darabszám.")

# A feladat:
# A hősöd vásárolt egy Vas kardot és két Fa pajzsot.
# Dupla indexelés (szögletes zárójelek, pl. raktar[sor][oszlop]) és a -= operátor használatával csökkentsd le a megfelelő értékeket a nagy raktar listában! (Emlékeztető: a Python 0-tól kezdve számolja az indexeket!).
# Jött egy új szállítmány! Az .append() metódus segítségével adj hozzá a raktar végéhez egy teljesen új listát: ["Gyógyital", 15].
# A módosítások után egy print() segítségével írasd ki a teljes raktárat, hogy lássuk a frissített készletet!

raktar = [ ["Vas kard", 5],
          ["Fa pajzs", 10], 
          ["Varázsbot", 2] ]



raktar[0][1] -= 1
raktar[1][1] -= 2
raktar.append(["Gyógyital", 15])

print(raktar)
        
print("*******************************************")
print("Részfeladat: A Bájital Keverés (Szótárak és Listák kombinálása) Találtál egy ősi receptkönyvet (szótár), és meg akarod nézni, hogy a hátizsákodban (lista) lévő dolgokból ki tudod-e főzni az Élet Elixírjét.")
# A feladat:
# Menj végig egy for ciklussal a recept alapján a szükséges hozzávalókon! Ezt úgy tudod megtenni, ha a ciklusnak a szótár konkrét listáját adod meg: for hozzavalo in receptkonyv["Elet Elixirje"]:
# A cikluson belül vizsgáld meg (if), hogy az adott hozzavalo NINCS-e benne a hatizsak listában! (Erre a not in kulcsszót tudod használni, pl. if valami not in lista:).
# Ha hiányzik a hátizsákból, növeld a hianyzo_anyagok változó értékét 1-gyel!
# A ciklus után egy if-else ággal hozd meg a döntést: Ha a hianyzo_anyagok száma pontosan 0, írd ki: "Sikeresen kifőzted az elixírt!". Minden más esetben írd ki: "Nem tudod elkészíteni, hiányzik [hianyzo_anyagok] hozzávaló!"

receptkonyv = {"Elet Elixirje": ["Víz", "Tündérpor", "Sárkányvér"]}
hatizsak = ["Víz", "Kavics", "Sárkányvér", "Tündérpor", "Kenyér"]
hianyzo_anyagok = 0


for hozzavalo in receptkonyv["Elet Elixirje"]:
    if hozzavalo not in hatizsak:
        hianyzo_anyagok += 1
if hianyzo_anyagok == 0:
    print("Sikeresen kifőzted az elixírt!")
else:
    print(f"Nem tudod elkészíteni, hiányzik [{hianyzo_anyagok}] hozzávaló!")
        
    