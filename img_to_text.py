import tkinter as tk
from tkinter import *
from tkinter import ttk
# ------------------ Ventana Raiz ---------------------
root = tk.Tk()
root.title("Convert-Text")
icono = tk.PhotoImage(file="text-img.png")
root.iconphoto(True, icono)
root.geometry("500x450")
root.resizable(width=True, height=True)
root.config(background='#292d3e')

buttom_frame = tk.Frame(root, background='#292d3e')
buttom_frame.pack()

frame_text = tk.Frame(root, background='#292d3e')
frame_text.pack()

# ----------------- Elementos Interiores ----------------
label_info = ttk.Label(buttom_frame, text='Extraiga texto de una imagen con Convert-Text ', 
                      background='#292d3e', 
                      foreground='#7FFFD4',
                      font= ('Arial', 15))
label_info.grid(row=0, column=0, columnspan=2, padx=20, pady=40)


button_ruta = tk.Button(buttom_frame, 
                         text='Buscar Imagen',
                         font=('Arial', 8),
                         bg='#00008B',
                         foreground='white',
                         relief='flat')
button_ruta.grid(row=1, column=0, padx=20, ipadx=2, ipady=2, pady=5)

entry_ruta = ttk.Label(buttom_frame, 
                       background=('#3b4159'),
                       width=40, 
                       font=('Arial', 11))
entry_ruta.grid(row=1, column=1, padx=5, pady=5, sticky='w')

button_ruta = tk.Button(buttom_frame, 
                         text='Iniciar',
                         font=('Helvetica  bold', 12),
                         bg='#00008B',
                         foreground='white',
                         relief='flat')
button_ruta.grid(row=2, column=0, columnspan=2, pady=20, ipadx=40, ipady=10)

scroll_barra = ttk.Scrollbar(frame_text,
                             orient='vertical')
scroll_barra.pack(fill='y',side='right')


text_captura = tk.Text(frame_text,
                       bg='blue',
                       font=('Arial', 12),
                       foreground='white',
                       width=50,
                       height=10,
                       wrap='none',
                       yscrollcommand=scroll_barra.set)
text_captura.pack(fill='both')

scroll_barra.config(command=text_captura.yview)


# ------------------ Barra de Menus ----------------------------
barra_menu = Menu(root)
root.config(menu=barra_menu)

menu_file = Menu(barra_menu, tearoff=False, foreground='white', background='#34394f')
barra_menu.add_cascade(label='File', menu=menu_file)
menu_file.add_command(label='Guardar Texo')
menu_file.add_command(label='Salir')

menu_Ayuda = Menu(barra_menu, tearoff=False, foreground='white', background='#34394f')
barra_menu.add_cascade(label='Ayuda', menu=menu_Ayuda)
menu_Ayuda.add_command(label='Acerca de')




root.mainloop()