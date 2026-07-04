print("*" * 50)
print('Részfeladat: A Kódex Lapjai (Fájlkezelés és adatformázás)')
# Írj egy programot, ami beolvassa ezt a fájlt. A beolvasott elemek sorrendjét fordítsd meg, majd írasd ki őket a képernyőre egy sorszámozott listaként. 
# A sorszámozás 1-től induljon. Ügyelj arra, hogy a terminálban megjelenő szavak végén vagy között ne legyenek rejtett sortörések és felesleges üres sorok

with open ("file/kodex.txt", "r", encoding="utf-8") as file:
    lisa = file.readlines()
fordit = list(reversed(lisa))
for index,f in enumerate(fordit, start=1):
    print(index, f.strip())
        
        
        
print("*" * 50)   
print("2. Részfeladat: A Sárkány Zsákmánya (Függvények, *args és matematika)")
# Írj egy kincsosztas nevű függvényt! A függvény várjon egy ado nevű paramétert (amelynek az alapértelmezett értéke legyen 15.5),
# majd ezután fogadjon be tetszőleges számú fellelt aranykupacot (számokat).
# A függvényen belül:
# Keresd meg és mentsd el a kapott aranykupacok közül a legkisebbet és a legnagyobbat.
# Számold ki az aranyak teljes összegét, majd vond le belőle az adót.
# Ezt a végső, adózott összeget kerekítse a rendszer 2 tizedesjegy pontosságra.
# A függvény ne nyomtasson a képernyőre, hanem egy f-string formátumú szöveggel térjen vissza, amely tartalmazza a kerekített végeredményt, a legkisebb és a legnagyobb arany értékét is.
# A főprogramban (a függvényen kívül) egy print utasítás segítségével hívd meg a függvényt tetszőleges számokkal (pl. kincsosztas(15.5, 100, 45, 12, 89, 500)), hogy megjelenjen az eredmény.

def kincsosztas(ado = 15.55, *args):
    min_aranykupac = min(args)
    max_aranykupac = max(args)
    teljes = sum(args)
    netto = teljes - ado
    adozott = round(netto, 2)
    return f"[{adozott}],[{min_aranykupac}],[{max_aranykupac}]"

print(kincsosztas(15.56, 100, 45, 12, 89, 500))
    
print("*" * 50)  
print("3. Részfeladat: A Mágikus Kovácstűz (Global és Ciklusok)")
# A Feladat:
# Írj egy tuzeles() nevű függvényt, amely nem vár semmilyen paramétert. A függvény módosítsa a kint létrehozott parazs_hofok változót! 
# Számolja ki a 2-es szám 4. hatványát, és ezt a kiszámolt értéket adja hozzá a globális parázs hőfokához.
# A függvényen kívül írj egy ciklust, amely addig ismétlődik, amíg a hőfok el nem éri a 200-at (tehát amíg szigorúan kisebb, mint 200). 
# A cikluson belül egyetlen dolgod van: meghívni a tuzeles() függvényt,
# majd minden körben kinyomtatni az aktuális hőfokot egy szöveg kíséretében (pl. "A tűz erősödik! Hőfok: ...").
parazs_hofok = 100

def tuzeles():
    global parazs_hofok
    hatvany = pow(2,4)
    parazs_hofok += hatvany    
while parazs_hofok < 200:
    tuzeles()
    print(f"A tűz erősödik! Hőfok:{parazs_hofok}") 

    
  