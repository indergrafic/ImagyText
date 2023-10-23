import tkinter as tk
from tkinter import *
from tkinter import ttk


#------------------ Funciones ----------------------
def busqueda_ruta():
    mensaje = ('Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.')
    


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
frame_text.pack(padx=10, pady=10)

# ----------------- Elementos Interiores ----------------
label_info = ttk.Label(buttom_frame, text='Extraiga texto de una imagen con Convert-Text ', 
                      background='#292d3e', 
                      foreground='#7FFFD4',
                      font= ('Arial', 15, 'bold'))
label_info.grid(row=0, column=0, columnspan=2, padx=20, pady=40)


button_ruta = tk.Button(buttom_frame, 
                         text=('Buscar Imagen'),
                         font=('Arial', 8, 'bold'),
                         bg='#00008B',
                         foreground='white',
                         relief='flat')
button_ruta.grid(row=1, column=0, padx=20, ipadx=2, ipady=2, pady=5)

mensajetexto = StringVar()
entry_ruta = tk.Label(buttom_frame, 
                       background=('#3b4159'),
                       width=40, 
                       font=('Arial', 11),)
entry_ruta.grid(row=1, column=1, padx=5, pady=5, sticky='w')

button_ruta = tk.Button(buttom_frame, 
                         text='Iniciar',
                         font=('Helvetica', 12, "bold"),
                         bg='#00008B',
                         foreground='white',
                         relief='flat',
                         command=busqueda_ruta)
button_ruta.grid(row=2, column=0, columnspan=2, pady=20, ipadx=40, ipady=10)

scroll_barra = ttk.Scrollbar(frame_text,
                             orient='vertical')
scroll_barra.pack(fill='y',side='right')

mensajetexto = StringVar()
text_captura = tk.Label(frame_text,
                       bg='blue',
                       font=('Arial', 12),
                       foreground='white',
                       text=mensajetexto)
text_captura.pack(fill='both', padx=5, pady=5)
borde_frama_text = tk.LabelFrame(frame_text, text='Texto Escaneado', font=('Arial', 10), background='white')
borde_frama_text.config(bd=2)
borde_frama_text.pack(padx=2, pady=2)




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