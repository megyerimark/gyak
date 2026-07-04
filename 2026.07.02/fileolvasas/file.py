# file = open('mondatok.txt', 'r', encoding='utf-8')


# # for sor in file:
# #     print(sor.strip())

# sor = file.readline()
# while sor:
#     print(sor.strip())
#     sor = file.readline()
    
    
    
# file.close()

with open('2026.07.02/fileolvasas/mondatok.txt', "r", encoding='utf-8') as file : # itt nem kell lezárni a file-opent, magától lezárja a filet
    # for sor in file:
    #     print(sor.strip())
    sor = file.readline()
    while sor:
        print(sor.strip())
        sor = file.readline()
        