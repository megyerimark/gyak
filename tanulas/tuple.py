#módosítható lista []
lista = ["jusi", "Ani", "Ili", "Barbi"]
# nem módosítható ()
tup1 = ("jusi", "Ani", "ili", "barbi")
print(tup1.index('ili'))
print(tup1.count("barbi"))


tup3 = ('Betti', )
print(tup3.upper())

# lista.append("Tmpon")
# print(lista)

# lista[-1] = ' Alma'
# print(lista)


#print(tup1[0:3])
tup2 = tuple(lista)
print(tup2)
lista2 = list(tup2)
print(lista2)