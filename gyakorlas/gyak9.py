print("*" * 50)  
# Nyissa meg a kerelmek.txt fájlt olvasásra ("r").
# Nyissa meg a napi_jelentes.txt fájlt írásra ("w").
# Nyissa meg a veszelyes_aktak.txt fájlt hozzáadásra ("a").
# (Tipp: Ezeket egymásba ágyazott with open blokkokkal tudod a legbiztonságosabban kezelni).
# Olvassa be a kerelmek.txt sorait egyenként.
# Vágja ketté a sorokat a kettőspont (:) mentén egy listába.
# A napi_jelentes.txt fájlba (amely minden futtatáskor felülíródik) írja bele minden küldetés nevét, a következő formátumban:

# Feldolgozva: [Küldetés neve]
# Vizsgálja meg a küldetés veszélyességi szintjét (a kettőspont utáni számot).
# Ha ez az érték szigorúan nagyobb, mint 80, akkor írja bele az adatokat a veszelyes_aktak.txt fájlba 
    # amely folyamatosan bővül, sosem törlődik), a következő formátumban:
# Kritikus kockázat: [Küldetés neve] - Szint: [Veszélyesség]
# Ügyelj arra, hogy a kimeneti fájlokban a sorok ne follyanak össze, minden bejegyzés új sorban kezdődjön (\n használata a .write() belsejében)!
# Az Elvárt Eredmény:
# Ha a kódod sikeresen lefut, a terminálban nem fogsz látni semmit. Viszont a mappádban létrejön két új fájl:
# A napi_jelentes.txt 4 sort fog tartalmazni ("Feldolgozva...").
# A veszelyes_aktak.txt 2 sort fog tartalmazni ("Kritikus kockázat...").

with open ("file/kerelmek.txt", "r", encoding="utf-8") as olvas:
    with open("file/napi_jelentesek.txt", "w", encoding="utf-8") as iras:
        with open("file/veszelyes_aktak.txt", "a", encoding="utf-8") as felul:
            kerelem_sorok = olvas.readlines()
            for sor in kerelem_sorok:
                adatok = sor.strip().split(":")
                iras.write(f"Feldolgozva: {adatok[0]}\n")
                if int(adatok[1]) > 80:
                    felul.write(f"Kritikus kockázat: {adatok[0]} - Szint:{adatok[1]}\n")
                
                
    
            