daily_macros = {}

def calculate_protein ( weight, protein_per_100):
    protein = (weight/100) * protein_per_100
    return protein

with open("macro_log.txt", "r", encoding="utf-8") as macro:
    next(macro)
    for lines in macro:
        data = lines.strip().split(";")
        try:
            food_weight = float(data[2])
            protein_value = float(data[3])
        except ValueError as v:
            print(v,f"Data error at {data[1]}")
            continue
        else:
            actual_protein = calculate_protein( food_weight,protein_value)
            daily_macros[data[1]] = actual_protein
for k, v in daily_macros.items():
    print(f"Food: {k} - Total Protein {v}g")
        