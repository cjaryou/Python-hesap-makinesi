import tkinter as tk
from tkinter import messagebox

# Fonksiyonlar
def click(event):
    global expression
    expression += event.widget.cget("text")
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set(expression)

def evaluate():
    global expression
    try:
        result = eval(expression)
        entry_var.set(result)
        expression = str(result)
    except Exception as e:
        messagebox.showerror("Hata", "Geçersiz İşlem!")
        expression = ""
        entry_var.set("")

# Ana pencere oluşturuluyor
root = tk.Tk()
root.title("Haktanın Hesap Makinesi")
root.geometry("350x500")
root.config(bg="#2C2F33")
root.resizable(False, False)

expression = ""

# Giriş alanı
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 24), justify=tk.RIGHT, bd=0, bg="#23272A", fg="#FFFFFF")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=20, pady=20, padx=10)

# Tuş takımı
button_frame = tk.Frame(root, bg="#2C2F33")
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

button_colors = {
    "default": {"bg": "#4E5D6C", "fg": "#FFFFFF"},
    "special": {"bg": "#7289DA", "fg": "#FFFFFF"}
}

for row in buttons:
    button_row = tk.Frame(button_frame, bg="#2C2F33")
    button_row.pack(expand=True, fill="both")
    for button_text in row:
        bg_color = button_colors["special"] if button_text in ["C", "="] else button_colors["default"]
        button = tk.Button(button_row, text=button_text, font=("Arial", 18), relief=tk.FLAT, 
                           bg=bg_color["bg"], fg=bg_color["fg"], activebackground="#99AAB5", activeforeground="#FFFFFF")
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        if button_text == "C":
            button.config(command=clear)
        elif button_text == "=":
            button.config(command=evaluate)
        else:
            button.bind("<Button-1>", click)

# Ana döngü
root.mainloop()