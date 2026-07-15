import pandas as pd

# 1. Lépés: Beolvassuk a gigantikus Excel vagy CSV fájlt a Pandasba (DataFrame-be)
# (Most a példa kedvéért egy mini adatsort hozok létre, de képzelj ide 50 000 sort!)
adatok = {
    'Dátum': ['2026-06-12', '2026-06-12', '2026-06-17', '2026-06-17'],
    'Étkezés': ['500ml latte + 2 tk zsemle csirkemellsonkával', '300g csirkemell + 70g rizs', '30g zab + fehérjepor + meggy', 'Fehérjés túrószelet'],
    'Típus': ['Reggeli', 'Ebéd', 'Reggeli', 'Snack'],
    'Kalória_kcal': [420, 550, 320, 180],
    'Fehérje_g': [28, 75, 35, 14]
}
df = pd.DataFrame(adatok)

# 2. Lépés: Jön a Főnök (Tech Lead) Kérdése!
# "Kiváncsi vagyok, hogy naponta mennyi volt a TOTAL fehérjebevitelem, de csak azokon a napokon, 
# amikor a reggeli kalória nem ment 500 fölé!"

# 3. Lépés: A Python megoldja 1 sorban:
napi_statisztika = df[df['Kalória_kcal'] < 500].groupby('Dátum')['Fehérje_g'].sum()

print(napi_statisztika)