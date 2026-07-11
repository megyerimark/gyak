import random
import string

alphabet = [
    "a", "A", "b", "B", "c", "C", "d", "D", "e", "E",
    "f", "F", "g", "G", "h", "H", "i", "I", "j", "J",
    "k", "K", "l", "L", "m", "M", "n", "N", "o", "O",
    "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T",
    "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y",
    "z", "Z"
]
numbers = [0,1,2,3,4,5,6,7,8,9]
special = ["÷","*", "#"]

        # print(random.choice(seq))
        # print(random.choices(seq))
with open ("password.txt", "a", encoding="utf-8") as pw:     
    lin = input("Szeretnél egy egyedi jelszót generálni? : ")
    seq = alphabet + numbers +special
    while True:
        if lin == "yes":
            for j in range(9):
                pw.write(f"{random.choice(seq)}")
            else:
                break
        