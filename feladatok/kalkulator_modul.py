rang_szorzo = {"Vas": 1.0, "Bronz": 1.2, "Ezüst": 1.5, "Arany": 2.0}

def kda_erekeles(kill, halal, assziszt):
    if halal == 0:
        kda_arany = (kill + assziszt) / 1
        return kda_arany
    else:
        kda_arany = (kill+assziszt) / halal
        return kda_arany