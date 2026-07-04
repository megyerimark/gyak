# 2. A Szabályok és a Logika:
# Nyiss meg 3 fájlt egy with open blokkban:
# oracle_naplo.txt (Olvasásra).
# tiszta_statisztika.txt (Írásra - ide jönnek a jó adatok).
# hibajelentes.txt (Hozzáadásra - ide gyűjtjük a selejtet).
# Olvasd be a bemeneti fájl sorait, és menj rajtuk végig egy for ciklussal.
# A cikluson belül vágd ketté (vagyis inkább több részre) a sort a pontosvesszők (;) mentén!
# A Try Blokkod:
# Próbáld meg kinyerni a szerver nevét (0. index), a kérések számát (1. index, alakítsd int-té), és az eltelt időt (2. index, szintén alakítsd int-té).
# Számold ki a Kérések per másodperc (RPS) értéket: osztás a kérések és az idő között.
# Az Except Blokkok: Készülj fel pontosan háromféle hibára, amiket be is kell írnod a hibajelentes.txt-be:
# Ha egy index nem létezik (mert mondjuk csak a szerver neve van ott): IndexError. Írd a hibafájlba: "Hiányos adatsor!"
# Ha a szöveget nem lehet számmá alakítani (pl. "Száz"): ValueError. Írd a hibafájlba: "Adatformátumi hiba!"
# Ha az eltelt idő nulla: ZeroDivisionError. Írd a hibafájlba: "Kritikus fagyás (0-val osztás)!"
# Az Else Blokk:
# Ha a try blokkban minden matematika és átalakítás sikeresen lefutott (nem volt hiba), akkor az else blokkban írd be a tiszta_statisztika.txt-be az eredményt:
# "[Szerver neve] működik. Terhelés: [RPS] kérés/mp."
# A Finally Blokk:
# Ez mindig fusson le az adott sornál! Dobj egy sima print-et a terminálba: "--- Egy sor ellenőrzése befejeződött ---"
print("")

with open("file/oracle_naplo.txt", "r", encoding="utf-8") as olvas:
    with open("file/tiszta_staisztika.txt", "w", encoding="utf-8") as ír:
        with open ("file/hibajelentés.txt", "a", encoding="utf-8") as hiba:
            for o in olvas.readlines():
                adatok = o.strip().split(";")
                try:
                    keresek =int(adatok[1])
                    ido = int(adatok[2])
                    rps  = keresek / ido
                except IndexError as i:
                    print(i , " - Hiányos Adatsor!\n")
                    hiba.write("Hiányos adat\n")
                except ValueError as v:
                    print(v,  " - Adatformátumi hiba!\n")
                    hiba.write(" Adatformátumi hiba!\n")
                except ZeroDivisionError as z:
                    print(z, " - Kritikus fagyás (0-val osztás)!\n")
                    hiba.write("- Kritikus fagyás (0-val osztás)!\n")
                else:
                    ír.write(f"{adatok[0]} működik. Terhelés: {rps} kérés/mp\n")
                finally:
                    print("--- Egy sor ellenőrzése befejeződött ---")