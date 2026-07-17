import pandas as pd

with open("jirat/data-001.txt", "r", encoding="utf-8") as data:
    next(data)
    for d in data:
        d.strip()
        print(d)

adatok = {
    'Dátum': ['06.12', '06.12', '06.17', '06.17', '06.17'],
    'Étel_Neve': ['5 dl latte', '2 db Lidl teljes kiőrlésű zsemle + 100g csirkemellsonka', '30g zab + 1 adag fehérjepor', '50g fagyasztott meggy', '6-7 db Aldi gyorsfagyasztott pogácsa'],
    'Típus': ['Ital', 'Főétel', 'Főétel', 'Gyümölcs', 'Snack'],
    'Fehérje_g': [16, 32, 28, 1, 8]
}

dF = pd.DataFrame(adatok)