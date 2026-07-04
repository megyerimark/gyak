# A Kihívás: Az Alkimista Laboratórium
# A Céh alkimistái mindenféle főzeteket kotyvasztanak, és egy naplóban rögzítik az összetevőket. A probléma az, hogy sokszor kapkodnak: 
# van, hogy kihagynak adatokat, van, hogy számok helyett betűket írnak, vagy ami a legrosszabb, nulla katalizátort használnak, ami robbanáshoz vezetne.
# Neked kell egy biztonsági rendszert írnod, ami kiszűri a hibákat, kiszámolja a sikeres főzetek erejét, és levonja a költséget a Céh raktárából

# 3. A Szabályok és a Logika:

# A) A Számoló Függvény (kalkulator):
# Írj egy függvényt, ami egy alap_ero paramétert vár (alapértelmezett értéke legyen 10.0), és tetszőleges számú extra összetevőt (*args).
# Használja a globális raktar_kristaly változót!

# A függvény adja össze az *args-ban lévő számokat, és adja hozzá az alap_ero-t.
# Ezt az összeget a pow() segítségével emelje a négyzetre, majd a round()-dal kerekítse 1 tizedesjegyre.
# Vond le ezt a kerekített számot a raktar_kristaly-ból.
# A függvény térjen vissza (return) a kerekített végső erővel!

# B) A Főprogram (Fájlkezelés és Hibakezelés):
# Nyiss meg 3 fájlt egyetlen with open blokkban:
# alkimista_naplo.txt (Olvasásra).
# sikeres_fozetek.txt (Írásra).
# selejt_naplo.txt (Hozzáadásra).
# Menj végig a beolvasott sorokon egy for ciklussal, és darabold fel őket a pontosvessző (;) mentén egy adatok nevű listába.
# A Try Blokk:
# Szedd ki a listából az adatokat: az 1. index lesz az alap erő, a 2. a katalizátor, a 3. az extra kristály (ezeket alakítsd int-té!).
# Számold ki a Stabilitást: oszd el az alap erőt a katalizátorral! (pl. stabilitas = alap / katalizator).
# Hívd meg a kalkulator függvényedet az átalakított számokkal, és az eredményt mentsd el egy vegleges_ero változóba.
# Az Except Blokkok (Írás a selejt fájlba):
# IndexError esetén írd a selejt_naplo.txt-be: "Hiányzó összetevők: {adatok[0]}\n"
# ValueError esetén írd a selejt_naplo.txt-be: "Hibás mérési adat: {adatok[0]}\n"
# ZeroDivisionError esetén írd a selejt_naplo.txt-be: "Robbanásveszély: {adatok[0]}\n"
# Az else Blokk (Írás a sikeres fájlba):
# Ide csak a jó főzetek jutnak el! Írd a sikeres_fozetek.txt-be:
# "{adatok[0]} elkészült. Erő: {vegleges_ero}. Stabilitás: {stabilitas}\n"
# A Finally Blokk (Képernyőre írás):
# Dobj egy print-et a terminálba: "--- {adatok[0]} asztal letakarítva ---"

raktar_kristaly = 10000.0

def kalkulator( alap_Ero = 10, *args, ):
    global raktar_kristaly
    teljes_ero = sum(args) + alap_Ero
    negyzetes_Ero = round(pow(teljes_ero, 2), 1)
    raktar_kristaly -= negyzetes_Ero
    return negyzetes_Ero

#print(kalkulator())
with open("file/alkimista_naplo.txt", "r", encoding="utf-8") as olvas:
    with open ("file/sikeres_fozetek.txt", "w", encoding="utf-8") as ir:
        with open("file/selejt_naplo.txt", "a", encoding="utf-8") as selejt:
            for sor in olvas.readlines():
                adatok = sor.strip().split(";")
                try:
                    alap_ero = int(adatok[1])
                    katalizator = int(adatok[2])
                    extra_kristaly = int(adatok[3])
                    stabilitas = alap_ero / katalizator
                    vegleges_ero = kalkulator( alap_ero, katalizator, extra_kristaly)
                except IndexError as i:
                    selejt.write(f"Hiányzó összetevők: {adatok[0]}\n") 
                except ValueError as v:
                    selejt.write(f"Hibás mérési adat: {adatok[0]}\n")
                except ZeroDivisionError as z :
                    selejt.write(f"Robbanásveszély: {adatok[0]}\n")
                else:
                    ir.write(f"{adatok[0]} elkészült. Erő: {vegleges_ero}. Stabilitás: {stabilitas}\n")
                finally:
                    print(f"--- {adatok[0]} asztal letakarítva ---")