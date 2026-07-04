#while True:
 #   pass
 
for i in range(10):
    if i == 5:
        break
    print(i)
    
    
szam= 0

while True:
    if szam == 5:
        break
    szam +=1
    print(szam)
    
for i in range(10):
    if i == 5:
        continue
    print(i)
    
szamalalo = 0
while True:
    szamalalo +=1
    if szamalalo % 2 == 0:
        continue
    print(szamalalo)
    if szamalalo > 20:
        break