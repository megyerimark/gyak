a = 10
b = 20


def osszeadas1():
    print(a+b)



def osszead(a,b, c =4):
    return a + b + c
    
def osszead3(*args):   #bármennyi szám lehet
     return sum(args)
 
def udvozlesek(*args):
    koszonoes = " Ennyi féle köszönés létezik: "
    for k in args:
        koszonoes += k
    print(koszonoes[0:len(koszonoes)-2]) 

 
osszeadas1()
osszeg = (osszead(45,25))  
print(osszeg)
print(osszead3(45,23,20,65))
udvozlesek("Szia"," Alma","Tampon2")
