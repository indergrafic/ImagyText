import tkinter as tk
from tkinter import *
from tkinter import ttk
# ------------------ Ventana Raiz ---------------------
root = tk.Tk()
root.title("Convert-Text")
icono = tk.PhotoImage(file="text-img.png")
root.iconphoto(True, icono)
root.geometry("500x500")
root.resizable(width=True, height=True)
root.config(background='#292d3e')


# ----------------- Elementos Interiores ----------------
label_info = ttk.Label(root, text='Extraiga texto de una imagen con Convert-Text ', 
                      background='#292d3e', 
                      foreground='#7FFFD4',
                      font= ('Arial', 15))
label_info.grid(row=0, column=0, columnspan=2, padx=20, pady=40)


button_ruta = tk.Button(root, 
                         text='Buscar Imagen',
                         font=('Arial', 8),
                         bg='#00008B',
                         foreground='white')
button_ruta.grid(row=1, column=0, padx=20, ipadx=2, ipady=2, pady=5)

entry_ruta = ttk.Label(root, 
                       background=('#3b4159'),
                       width=40, 
                       font=('Arial', 11))
entry_ruta.grid(row=1, column=1, padx=5, pady=5)

button_ruta = tk.Button(root, 
                         text='Iniciar',
                         font=('Helvetica  bold', 12),
                         bg='#00008B',
                         foreground='white')
button_ruta.grid(row=2, column=0, columnspan=2, pady=20, ipadx=40, ipady=10)

text_captura = tk.Text(root,
                       bg='blue',
                       font=('Arial', 12),
                       foreground='white',
                       border=10,
                       width=50,
                       height=30,
                       wrap='char')
text_captura.grid(row=3, column=0, columnspan=2, padx=10, pady=20)


# ------------------ Barra de Menus ----------------------------
barra_menu = Menu(root)
root.config(menu=barra_menu)

menu_file = Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(label='File', menu=menu_file)
menu_file.add_command(label='Salir')

menu_Ayuda = Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(label='Ayuda', menu=menu_Ayuda)
menu_Ayuda.add_command(label='Acerca de')




root.mainloop()