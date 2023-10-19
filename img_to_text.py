import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Convert-Text")
icono = tk.PhotoImage(file="text-img.png")
root.iconphoto(True, icono)
root.geometry("500x300")
root.resizable(width=False, height=True)
root.config(background='#292d3e')




label_info = ttk.Label(root, text='Extraiga texto de una imagen con Convert-Text ', 
                      background='#292d3e', 
                      foreground='#7FFFD4',
                      font= ('Arial', 15))
label_info.grid(row=0, columnspan=2, padx=30, pady=40)


button_ruta = tk.Button(root, 
                         text='Buscar Ruta',
                         bg='#00008B',
                         foreground='white')
button_ruta.grid(row=1, column=0,padx=20, sticky='ew')

entry_ruta = ttk.Entry(root, 
                       background='#0000CD', 
                       width=40, 
                       font=('Arial', 11))
entry_ruta.grid(row=1, column=1, sticky='e')




root.mainloop()