import tkinter as tk


window = tk.Tk()
def run_macro_check():
    print("Macro checked function executed!")
window.title("Daily Macro Tinker")
window.geometry("400x400")
check_button = tk.Button(window, text="Run Macro Check" ,command=run_macro_check)
check_button.pack(pady=10)
window.mainloop()
