print("*" * 50)
print("1. Részfeladat: A Varázsigék Könyve (Fájl, Reversed, Enumerate)")

# Használd a with open('varazsigek.txt', "r", encoding='utf-8') as file: módszert!
# Olvasd be a fájl összes sorát egy listába (használd a file.readlines() parancsot, és mentsd el egy változóba, pl. igek_listaja).
# A with blokkon kívül fordítsd meg a beolvasott listát! (Tipp a tegnapi jegyzetből: list(reversed(igek_listaja))). Mentsd el ezt a fordított listát!
# Egy for ciklussal és az enumerate() függvénnyel menj végig a megfordított listán.
# Írasd ki a sorszámot és az igét f-stringgel! Ne felejtsd el a .strip() metódust használni a szavakon, hogy ne legyenek csúnya sortörések.

with open('file/varazsigek.txt', "r", encoding='utf-8') as file:
    igek_listaja = file.readlines()
fordit = (list(reversed(igek_listaja)))
for index, fr in enumerate(fordit):
    print(f"{[index]}, [{fr.strip()}]")
        
        
        
print("*" * 50)
print("2. Részfeladat: A Kovácsmester Üllője (Függvények, *args, max, min, sum)")
# A feladat:
# Írj egy kard_kovacsolas nevű függvényt! Legyen egy alap_sebzes paramétere (alapértelmezett értéke legyen mondjuk 25.5), és várjon tetszőleges számú extra követ (*args).
# A függvényen belül keresd meg a legerősebb és a leggyengébb követ a tegnap tanult max() és min() függvényekkel, és mentsd el őket egy-egy változóba!
# Számold ki az összes kő együttes erejét a sum() segítségével, és add hozzá az alap_sebzes-hez. Ez lesz a végső sebzés.
# Mivel az alap sebzés egy tizedestört, kerekítsd a végső sebzést kerek 1 tizedesjegyre a round() függvénnyel! (Tipp: round(valami, 1)).
# A függvény térjen vissza (return) egy ilyen f-stringgel:
# "Kész! Végső sebzés: [kerekített_végső]. Legjobb kő: [max], Legrosszabb kő: [min]"
# A főprogramban hívd meg egy print() belsejében, például így: print(kard_kovacsolas(25.5, 10, 4, 18, 2))

def kard_kovacsolas(alap_sebzes = 25.5, *args):
    legnagyobb = max(args)
    legrosszabb = min(args)
    teljes = sum(args)+ alap_sebzes
    kerekitett_vegso = round(teljes, 1)
    return f" Végső sebzés: [{kerekitett_vegso}], legjobb kő [{legnagyobb}], legrosszabb kő [{legrosszabb}]"
print(kard_kovacsolas(25.5, 10, 4, 18, 2, 64563534))


print("*" * 50)
print("3. Részfeladat: A Védőpajzs Merülése (Global, While, Pow)")
vedopajzs = 1000
# A feladat:
# Írj egy demon_tamadas() nevű függvényt, ami nem vár paramétert (üres a zárójel).
# A függvény legelején mondd meg a gépnek, hogy a kinti pajzsot fogod támadni (global vedopajzs).
# Számold ki a démon sebzését a pow() függvénnyel! A démon az 5-ös alapszám 3. hatványával támad. (Írd ezt bele a pow zárójeleibe).
# Vond le (-=) ezt a kiszámolt sebzést a globális vedopajzs-ból.
# A függvényen kívül írj egy sima while ciklust, ami addig fut, amíg a vedopajzs nagyobb, mint 0.
# A cikluson belül egyszerűen csak hívd meg a demon_tamadas() függvényt, majd írd ki print-tel: "Bumm! A pajzs energiája: [vedopajzs]"
def demon_tamadas():
    global vedopajzs
    sebzes = pow(5,3)
    vedopajzs -= sebzes
while vedopajzs >= 0:
    demon_tamadas()
    print(f"Bumm! A pajzs energiája: [{vedopajzs}]")