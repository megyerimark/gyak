nevek1= ["Xéne", "Alma", "Ildi", "Zsuzsi","Evi", 10, True]
nevek2= ["Xalma", "Körte", "Imre", "Zsolt","EPista"]

#for nev in nevek1:
  #  print(nev)
    
#for nev in nevek2:
 #   print(nev)
    

def nev_printer(nev_lista):
    for nev in nev_lista:
        if isinstance(nev, str): # a név, adott ciklusban, string-e
            print(nev.upper()) #nagy betűé konvertálás
        else:
            print('Nem string típus:' + str(type(nev)))
        
        
nev_printer(nevek1)
nev_printer(nevek2)