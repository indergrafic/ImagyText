import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Convert-Text")
icono = tk.PhotoImage(file="text-img.png")
root.iconphoto(True, icono)
root.geometry("500x400")
root.config(bg="blue")

window = ttk.Frame(root)

window.pack(fill='both')


root.mainloop()