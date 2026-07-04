
# lista = [1,2,3]



# try:
#     print(pla)
#     print(lista[5])
#     print(1/0)
# except NameError as e:
#     print(e, ' Nem létező változó')
# except IndexError as e:
#     print(e, "Tartományon kívüli index")
# except ZeroDivisionError as z:
#     print(z, " - 0-val osztás nem leehtséges")

lista = ["1", "2", "3", None, "4", "", "5", True, "Bözsi", "12,65"]
for l in lista:
    try:
        print(int(l)*2)
    except:
        continue
    
    
try:
    print(bla)
except:
    print('nem jó változó név!')
else:
    print("az else")
finally:
    print("try vége")