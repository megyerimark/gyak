import tkinter as tk
import volume_calc as vc
import matplotlib.pyplot as plt

window = tk.Tk()

def analyze_workout():
    volume_data = {}
    with open ("workout_log.txt", "r", encoding='utf-8') as w:
        next(w)
        for l in w:
            data = l.strip().split(";")
            try:
                int_food = int(data[2])
                int_weigth = int(data[3])
                int_protein = int(data[4])
            except ValueError as v:
                print(v, "Data error at {data[1]}")
            else:
                result = vc.process_workout_data(int_food,int_protein, int_weigth)
                volume_data[data[1]] = result
                
    y = []
    x = []
    for k, v in volume_data.items():
        x.append(k)
        y.append(v)
    plt.bar(x , y )
    plt.show()
window.title("Edzés napló")
window.geometry("600x400")
button = tk.Button(window, text="Calculate", command=analyze_workout)
button.pack(pady=20)
window.mainloop()