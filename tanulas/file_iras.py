# w írás
# a append  meglévőhpz hozzáadunk
# r olvasás 
with open ("file/varazsigek.txt", "r", encoding="utf-8") as infile:
    with open("file/kimenet.txt", "w", encoding="utf-8") as outfile:
        
        sor = infile.readline()
        
        while sor:
            outfile.write(sor)
            sor = infile.readline()
    