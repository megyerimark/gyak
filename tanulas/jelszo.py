

jelszo="a"
proba = 0

bementet = input("Add meg a jelszavad: ")
while bementet!= jelszo:
    proba += 1
    if proba == 3:
        print("Rendszer lezárva")
        break
    print("Hibás jelszó")
    bementet = input("Mi a jelszavad? ")

if bementet == jelszo:
    print("Beléptél a jelszavad : ", jelszo)
     