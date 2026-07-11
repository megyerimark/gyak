import tkinter as tk

def start_analysis():
    print("Anaéysis started: ...")
    
window = tk.Tk()   
my_button = tk.Button(window, text="Run Code", command=start_analysis)
my_button.pack(pady=10)