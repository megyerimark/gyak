import matplotlib.pyplot as py
szerver_kassza = 0
jatekosok_szotar = {}
proba = 0


def bonusz_kalkulator (alap_arany, *args):
    global szerver_kassza
    global proba
    teljes_arany = alap_arany + sum(args)
    szerver_kassza += teljes_arany
    return teljes_arany

while True:
    jelszo = input("Kérem a fejlesztői jelszót (vagy 'exit' a kilépéshez):")
    proba+= 1
    jo_pw = "DEV2026"
    if jelszo == "exit" or proba == 3:
        print("Rendszer leállítva")
        break
    if jelszo == jo_pw:
        print("Hozzáférés engedélyezve!") 
        break
    else:
        print("Helytelen jelszó")
with open ("szerver_log.txt", "r", encoding="utf-8") as log :
    next(log)
    for sor in log:
        adatok = sor.strip().split("|")
        rovid_nev = adatok[1][:3]
        targyak_lista = list(adatok[4].split(","))[::-1]
        try:
            arany = int(adatok[3])
            vegleges_arany =bonusz_kalkulator( arany, 200,50)
        except ValueError as v:
            print(f"Adathiba a szerveren a(z) {adatok[1]} nevű játékosnál!")
            continue
        else:
            jatekosok_szotar[adatok[1]] = (rovid_nev, vegleges_arany , targyak_lista)
nevek_x = []
arany_y= []
for kulcs, ertek in jatekosok_szotar.items():
    nevek_x.append(ertek[0])
    arany_y.append(ertek[1])
py.bar(nevek_x, arany_y)
py.ylabel("Birtokolt Arany")
py.show()
print(f"A teljes szerver gazdasága: {szerver_kassza}")