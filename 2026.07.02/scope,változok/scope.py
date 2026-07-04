#function scope
def test():
    global a,b
    a = 12 
    b = 15
    print(a,b)
     
test()
print(a,b)

#module scope
a = 78
b = 47
def test2():
    for i in range(5):
        b = 54
        pass
test2()
def test3():
    if True:
        c = 78
    print(c)
test3()