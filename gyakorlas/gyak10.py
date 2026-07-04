import tkinter as tk
# A Szabályok és a Logika:
# A) A Számoló Függvény (energia_szivo):
# Írj egy energia_szivo nevű függvényt, ami egy alap_fogyasztas paramétert vár (alapértelmezett értéke legyen 10.0), majd tetszőleges számú extra fókuszkristályt (*args).
# A függvény a kinti, globális kozponti_kristaly értékével dolgozzon!
# A függvény belsejében írasd ki a képernyőre (print) a fókuszkristályok közül a legnagyobbat és a legkisebbet, egy ilyen formátumban: "--- Extra kristályok: Max: [max], Min: [min] ---" (Tipp: max() és min() az args-on).
# A matek: Számold ki a teljes fogyasztást! Add össze az extra kristályokat (sum), ehhez add hozzá az alap_fogyasztas-t. Az így kapott számot a pow() függvénnyel emeld a négyzetre (2. hatvány).
# Ezt a végső, négyzetre emelt értéket kerekítsd kerek 1 tizedesjegyre a round() függvénnyel.
# Vond le ezt a kerekített végeredményt a globális kozponti_kristaly-ból, majd a függvény térjen vissza (return) a kerekített fogyasztás számadatával!
# B) Az Adatfeldolgozás (A Főprogram):
# Nyiss meg egyszerre 3 fájlt: a napi_varazslatok.txt-t olvasásra, egy új tiszta_naplo.txt-t írásra, és egy tiltott_magia.txt-t hozzáadásra.
# Olvasd be a varázslatokat, de mielőtt feldolgoznád őket, fordítsd meg a listát a reversed() segítségével (a Torony mindig a legfrissebbtől visszafelé naplóz)!
# Menj végig a megfordított listán egy for ciklussal, amit az enumerate()-tel 1-től kezdesz sorszámozni!

# A ciklson belül darabold fel a sorokat a kettőspontnál (:).
# A tranzakció: Hívd meg a függvényedet! Az alap_fogyasztas helyére a fájlból kiolvasott számot tedd be (alakítsd át float()-tá, mert tizedestörtek vannak benne!), extra kristályoknak pedig adj meg 3 tetszőleges számot (pl. 4, 8, 2). A függvény által visszaadott eredményt mentsd el egy változóba (pl. fizetendo).
# A naplózás: Írd bele a tiszta_naplo.txt-be a következő sort (ne felejtsd a \n-t):
# "[Sorszám]. [Varázslat neve] elhasználva. Levont energia: [fizetendo]. Maradt a kristályban: [kozponti_kristaly]"
# A riasztás: Ha a fájlból kiolvasott alap fogyasztás szigorúan nagyobb, mint 100, akkor írd bele a varázslat nevét és az alap számot a tiltott_magia.txt-be, így:
# "FIGYELMEZTETÉS: [Név] - Veszélyszint: [Szám]
print("*" * 100)
kozponti_kristaly = 5000000

def energia_szivo (alap_fogyasztas = 10.0, *args):
    global kozponti_kristaly
    smal = min(args)
    big = max(args)
    print(f"A legolcsóbb termék ára :{smal}\nA legdrágább termék ára:{big}")
    teljes_fogyasztas = sum(args) + alap_fogyasztas
    negyzetes = pow(teljes_fogyasztas ,2)
    kerekitett = round(negyzetes, 3)
    kozponti_kristaly-= kerekitett
    return f"{kerekitett}"

print(energia_szivo(10,13 ))
print("*" * 100)
print("B Feladat")

with open ("file/napi_varazslatok.txt", "r", encoding='utf-8') as olvas:
    with open("file/tiszta_naplo.txt", "w", encoding='utf-8') as iras:
        with open("file/tiltott_magia.txt", "a", encoding="utf-8") as feluliras:
            sorok = olvas.readlines()
            for_lista = (list(reversed(sorok)))
            for index, fl in enumerate(for_lista, start=1):
                adatok = fl.strip().split(":")
                fizetendo = energia_szivo(float(adatok[1]),4,8,2)
                iras.write(f"{index}. {adatok[0]} elhasználva. Levont energia:{fizetendo}, Megmaradt kristályod: {kozponti_kristaly}\n")
                if float(adatok[1]) > 100:
                    feluliras.write(f"FIGYELMEZTETÉS: {adatok[0]} - Veszélyszint {adatok[1]} \n")
