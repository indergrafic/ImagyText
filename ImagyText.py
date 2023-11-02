from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox
from PIL import Image
import pytesseract
from translate import Translator


# ---------------- Ventana Principal -------------------
root = Tk()

root.title('ImagyText')
root.resizable(True, 1)
root.iconbitmap('D:\\a_WEB-Trabajos\\Repo GitHub\\Imagen_a_Texto\\textlogo.ico')

# -------------- Mensaje de Bienvenida -------------------
def pantalla_Bienvenida():
        messagebox.showinfo('Bienvenido', 'Bienvenido a ImagyText.\nRecuerda tener instalado Tesseract.exe\nPodrás escanear una imagen con texto y extraerlo. Después podrás guardarlo en un ".txt" y/o traducirlo.')

# ---------------- Ventanas secundarias -------------------
def error_busqueda():
    respuesta = messagebox.askretrycancel("Error en la Busqueda", 'Ruta especificada no es correcta.')
    if respuesta == True:
        abrir_archivo()

# ---------------- Instruciones para la conversión -------------------
def abrir_archivo():
    global archivo
    ''' Función que nos permite hacer la busqueda del archivo que escanearemos su texto.'''
    try:
        archivo = filedialog.askopenfilenames(title="Buscar Archivo", 
                                            initialdir="C:/",
                                            filetypes=(("Archivos de imagen",''), ('JPG','*.jpg'), ('PNG','*.png'), ('BMP','*.bmp')))
    except: error_busqueda()

    '''Atraves de config, enviamos el texto del Label "label_ruta", para mostrar el path del archivo.'''
    try:
        label_ruta.config(text=archivo[0])
    except IndexError:
        error_busqueda()

def convert_text():
    global texto
    ''' Función con la que abrimos el programa que realiza la tarea de conversión.
    Se realiza una apertura del archivo, el escaneo del texto y su guardado, y lo enviamos
     a la etiqueta que lo imprime en pantalla. '''
    texto = ''
    try:    
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        ruta_imagen= archivo[0]
        imagen_abierta = Image.open(ruta_imagen, mode='r')
        texto = pytesseract.image_to_string(imagen_abierta)
        label_text_scan.config(text=texto)
    except: error_busqueda()

# ---- Funcionalidad para traducir el texto Español <> Ingles -------
def traduccion():
    ''' Funcion que tras instalar el modulo "Translator", nos permite convertir el texto del inglés al español y a la inversa.'''
    global texto
    traducido = ''

    idioma = str(caja_idiomas.get())
    if idioma == 'Trad. al Inglés':
        respuesta = messagebox.askquestion(title='Tradución', message="¿Esta seguro de querer traducir el texto?")
        try:
            trad = Translator(from_lang='es', to_lang='en')
            traducido = trad.translate(texto)
            label_text_scan.config(text=traducido)
            texto = traducido
        except: 
            respuesta = messagebox.askretrycancel("Error Traducción", 'Se ha producido un error inesperado.')
            if respuesta == True:
                traduccion()
    elif idioma == 'Trad. al Español':
        respuesta = messagebox.askquestion(title='Tradución', message="¿Esta seguro de querer traducir el texto?")
        if respuesta == 'yes':
            try:
                trad = Translator(from_lang='en', to_lang='es')
                traducido = trad.translate(texto)
                label_text_scan.config(text=traducido)
                texto = traducido
            except: 
                respuesta = messagebox.askretrycancel("Error Traducción", 'Se ha producido un error inesperado.')
                if respuesta == True:
                    traduccion()
    
# ---------------------- Guardar archivos -------------------------------- 
def guardar_archivo():
    resp = messagebox.askquestion(title='Guardar..', 
                                   message='¿Quiére guardar el texto actual?')
    if resp == 'yes':  
        archivo_guardado = filedialog.asksaveasfile(title="Guardar archivo...", 
                                                            defaultextension='.txt',
                                                            filetypes=(("Archivo de texto",'*.txt'),))
        while True:
            try:
                parrafo = texto
                archivo_guardado.write(parrafo)
                archivo_guardado.close()
                break
            except AttributeError:
                break
            except NameError:
                break

def borrar_texto():
     label_text_scan.config(text='')
            
# --------------- Barra de Menus y Funcionalidades ------------------------
def salir_Aplicacion():
    valor = messagebox.askquestion(title='Salir', message='¿Desea salir de la Aplicación?')
    if valor == 'yes':
        root.destroy()

def info_Aplicacion():
    messagebox.showinfo(title='Acerca de..', message='ImagyText\n Vesion 1.0 para Window 10 (Octubre 2023)\n\nEscanea una imagen que contenga texto y extráelo a un archivo “.txt”. Podrás traducirlo del español al inglés o viceversa y guardarlo.')

barra_Menu = Menu(root)
root.config(menu=barra_Menu, width=300, height=200)

opcion_Archivo = Menu(barra_Menu, tearoff=0)
opcion_Archivo.add_command(label='Salir', command=salir_Aplicacion)

opcion_Info = Menu(barra_Menu, tearoff=0)
opcion_Info.add_command(label='Ayuda', command=info_Aplicacion)

barra_Menu.add_cascade(label='Archivo', menu=opcion_Archivo)
barra_Menu.add_cascade(label='Info', menu=opcion_Info)

# ---------------- Ventanas Secundarias -------------------
''' El primer Frame, es donde colocamos el texto de presentacion e imgane de la aplicacion. Los botones para:
buscar la ruta, iniciar el escaneo, guardar el archivo y los de traducción. 
El segundo Frame se utiliza para mostrar el texto.'''
frame_botones = Frame()
frame_botones.pack(fill='both', expand='True')
frame_botones.config(bg='#333051', width=500, height=200, cursor='hand2')

frame_text = Frame()
frame_text.pack(fill='both', expand='True')
frame_text.config(bg='#333051', width=400, height=200,cursor='hand2')

# ---------------- Imagen logo de la aplicación -------------------
mi_imagen = PhotoImage(file='D:\\a_WEB-Trabajos\\Repo GitHub\\Imagen_a_Texto\\bitmat.png')
Label(frame_botones, image=mi_imagen, bg='#333051').grid(row=0, column=0,
                                                         pady=20,
                                                         padx=10,
                                                         sticky='e')

# ---------------- Etiquetas de informacion y botones  -------------------
label_descrip = Label(frame_botones,text='Extraer texto de una imagen\n con ImagyText',
                      font=('Times', 16, 'bold'),
                      bg='#333051',
                      fg='#8DF3A8', anchor='center')
label_descrip.grid(row=0, column=1, padx=5, pady=30)

boton_buscar = Button(frame_botones, 
                      text='Ruta de la Imagen', 
                      font=('Times', 9, 'bold'),
                      bg='#258097',
                      fg='white',
                      border=2, 
                      command=abrir_archivo)
boton_buscar.grid(row=2, column=0, padx=50, pady=20, ipadx=3, ipady=3)

label_ruta = Label(frame_botones, text='..\ aquí aparecerá la ruta del archivo.',
                   font=('Arial', 8, 'bold'), 
                   fg='#71729C',
                   bg='#333051',
                   anchor='center')
label_ruta.grid(row=2, column=1, padx=5, pady=20)

boton_iniciar = Button(frame_botones, 
                       text='Iniciar Conversión', 
                       font=('Times', 10, 'bold'),
                       bg='#5552AB',
                       fg='white',
                       border=2, 
                       anchor='center',
                       command=convert_text)
boton_iniciar.grid(row=3, column=0, padx=10, pady=10,)

boton_guardar = Button(frame_botones, 
                       text='  Guardar Texto..  ', 
                       font=('Times', 10, 'bold'),
                       bg='#5552AB',
                       fg='white',
                       border=2,
                       command=guardar_archivo)
boton_guardar.grid(row=4, column=0, padx=30, pady=10)

butom_trad = Button(frame_botones, text='Traducir Texto',
                   font=('Arial', 10, 'bold'), 
                   fg='white',
                   bg='#A20297',
                   anchor='center',
                   command=traduccion)
butom_trad.grid(row=3, column=1, padx=30, pady=10)

caja_idiomas = ttk.Combobox(frame_botones)
caja_idiomas.grid(row=4, column=1, padx=30, pady=5)
caja_idiomas['values']=("Trad. al Inglés", "Trad. al Español")
caja_idiomas.current(0)

# ---------------- Ventana para el texto -------------------
cuadro_texto= LabelFrame(frame_text,
                        text='Texto Extraido',
                        font=('Times', 8, 'bold'),
                        bg='#333051',
                        fg='white')
cuadro_texto.grid(row=1, column=0, padx=15, pady=10)

label_text_scan = Label(cuadro_texto,
                        text='',
                        font=('Time', 11, 'bold'),
                        justify='left',
                        fg='white',
                        bg='#333051',
                        width=60, anchor='center')
label_text_scan.grid(row=0, column=0, sticky='ew')


pantalla_Bienvenida()

root.mainloop()