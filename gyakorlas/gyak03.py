
print("******************************************************************")
print("1. Részfeladat: A Kocsmai Kódfejtő (Stringek és Ciklusok)")
# A hősöd egy titkos ajtóhoz ér. Ahhoz, hogy kinyíljon, meg kell számolnia, hány "a" vagy "A" betű szerepel a falra vésett ősi varázsszövegben.
# A cikluson belül egy if feltétellel vizsgáld meg, hogy az aktuális betu egyenlő-e "a"-val VAGY (or) "A"-val.
# Ha igen, növeld meg az a_betuk_szama változó értékét 1-gyel (+= 1).
# A ciklus után írd ki a képernyőre: "A titkos jelszó: [szám]"

felirat = "Az aranyalma a sarkany barlangjaban van."
a_betuk_szama = 0

for betuk in felirat:
    if betuk == "a" or betuk =="A":
        a_betuk_szama += 1
print(f"A titkos jelszó: [{a_betuk_szama}]")
        

print("******************************************************************")
print("2. Részfeladat: Az Első Összecsapás (While ciklus és változók)")
# Írj egy while ciklust, ami addig fut, amíg a hős életereje nagyobb, mint 0 ÉS (and) a goblin életereje nagyobb, mint 0.
# A cikluson belül játszunk le egy kört:
# Vond le a goblin HP-jából a hős sebzését (-=).
# Vond le a hős HP-jából a goblin sebzését (-=).
# Írd ki: "A hős lesújtott! Goblin HP: [goblin_hp]"
# Írd ki: "A goblin visszatámadt! Hős HP: [hos_hp]"
# Amikor a ciklus véget ér (valaki meghalt), egy if-else segítségével vizsgáld meg a hős HP-ját. Ha nagyobb, mint 0, írd ki: "GYŐZELEM! A goblin elhullott.", különben: "VERESÉG... A hős elbukott."

hos_hp = 30       # Hős életereje
hos_sebzes = 6    # Hős sebzése körönként

goblin_hp = 20    # Goblin életereje
goblin_sebzes = 4 # Goblin sebzése körönként

while hos_hp> 0 and goblin_hp > 0:
    goblin_hp -= hos_sebzes
    hos_hp -= goblin_sebzes
    print(f"A hős lesújtott! Goblin HP: [{goblin_hp}]")
    print(f"A goblin visszatámadt! Hős HP: [{hos_hp}]")
if hos_hp >= 0:
    print("GYŐZELEM! A goblin elhullott.")
else:
    print("VERESÉG... A hős elbukott")
        
        

print("******************************************************************")
print("3. Részfeladat: A Kincsesláda Kifosztása (Függvények, Szótárak és Listák)")
# Írj egy kifoszt() nevű függvényt, ami két paramétert vár: a ládát (listát) és a táskát (szótárt).
# A függvényen belül egy for ciklussal menj végig a talált tárgyakon.
# Egy if feltétellel nézd meg, hogy az adott tárgy benne van-e már a szótárban (használhatod az in kulcsszót, pl.: if targy in taska:).
# Ha benne van: Akkor csak növeld meg az értékét a szótárban 1-gyel. (Emlékezz az előző leckére: taska[targy] += 1)
# Ha nincs benne (else): Akkor add hozzá a szótárhoz új elemként, és adj neki 1-es értéket! (Emlékezz a varázskardos példára!)
# A kód legvégén hívd meg a függvényt a konkrét változóiddal, majd nyomtasd ki a frissült hátizsákot!

hatizsak = {"arany": 50, "gyogyital": 1}
talalt_targyak = ["arany", "arany", "gyogyital", "varazskard", "arany"]

def kifoszt(lada,táska):
    for targy in lada:
        if targy in táska:
            táska[targy]+= 1
        else:
            táska[targy] = 1
            
kifoszt(talalt_targyak,hatizsak)
print(hatizsak)
             