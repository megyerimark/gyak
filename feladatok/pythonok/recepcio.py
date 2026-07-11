import lotus_adatbazis as ladb

napi_belepok = 0

with open ("lotus_naplo.txt", "a", encoding="utf-8") as naplo:
    while True:
        kartya_szam = input("Kérlek add meg a  kártyaszámod:\n ")
        print(f"Az általad megadott kártyaszám: {kartya_szam}")
        if kartya_szam == "zárás":
            break
        if kartya_szam not in ladb.berletek:
            print("Ismeretlen kártya, kérjük regisztráljon!")
            continue
        else:
            turmix =input("Mennyi turmixot szereznél?")
        try:
            
            adag= int(turmix)
        except ValueError as v:
            print("Hibás adatbevitel, kérjük számot adjon meg!")
            continue
        else:
            if ladb.jogosultsag(kartya_szam) == True:
                napi_belepok +=1
                naplo.write(f"{kartya_szam} belépett. Turmix {adag}\n")
            else:
                naplo.write(f"Az alábbi vendég lépett be : \n {kartya_szam} és lejárt a bérlete ,{adag} Adag fehérjét vásárolt a mai nap\n")
                print("Sajnos lejárt a bérleted! kérlek hosszabítsd azt meg")
print(f"A Lotus recepció bezárt. Mai sikeres belépők száma: {napi_belepok} fő. Eladott turmixok mennyisége : {adag}\n")