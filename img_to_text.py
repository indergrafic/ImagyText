from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import pytesseract
from translate import Translator


# ---------------- Ventana Principal -------------------
root = Tk()

root.title('Convert-Text')
root.resizable(True, 1)
root.iconbitmap('text-Img.ico')

# -------------- Ventana de Bienvenida -------------------
def pantalla_Bienvenida():
        messagebox.showinfo('Bienvenida', 'Bien venido a Convert-Text.\nEscanea una imgen para extraer el texto de la misma en formato ".txt". Podras traducirlo del ingles al español y guardarlo en un archivo.\nRecuerda tener instalado Tesseract.exe ')

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

    '''Atraves del config, modificamos el texto de la Etiqueta, para mostrar el path del archivo.'''
    try:
        label_ruta.config(text=archivo[0])
        mostrar_imagen()
    except IndexError:
        error_busqueda()
def mostrar_imagen():
    ruta_correcta = archivo[0]
    a = '\ '
    b = '/'
    for i in ruta_correcta:
        if i == a:
            ruta_correcta = archivo[0].replace(i, b)
    
    print(ruta_correcta)

    img_min = Image.open(ruta_correcta)
    tamano = img_min.resize((70,70), Image.ADAPTIVE)
    foto = ImageTk.PhotoImage(tamano)
    label_foto = Label(frame_botones, image=foto)
    label_foto.pack(pady=20, padx=10)

def convert_text():
    global texto
    ''' Función con la que abrimos el programa que realiza la tarea de conversión.
    Ser realiza una apertura del archivo, el escaneo del texto y su guardado, y lo enviamos
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
def traduccion_espanol():
    global texto
    traducido = ''
    ''' Funcion que tras instalar el modulo "translator", nos convierte el texto en ingles a español.'''
    respuesta = messagebox.askquestion(title='Tradución', message="¿Esta seguro de querer Traducir el texto?")
    if respuesta == 'yes':
        try:
            trad = Translator(from_lang='en', to_lang='es')
            traducido = trad.translate(texto)
            label_text_scan.config(text=traducido)
            texto = traducido
        except: 
            respuesta = messagebox.askretrycancel("Error Traducción", 'Se ha producido un error inesperado.')
            if respuesta == True:
                traduccion_espanol()

def traduccion_ingles():
    global texto
    traducido = ''
    ''' Funcion que tras instalar el modulo "translator", nos convierte el texto en ingles a español.'''
    respuesta = messagebox.askquestion(title='Tradución', message="¿Esta seguro de querer Traducir el texto?")
    if respuesta == 'yes':
        try:
            trad = Translator(from_lang='es', to_lang='en')
            traducido = trad.translate(texto)
            label_text_scan.config(text=traducido)
            texto = traducido
        except: 
            respuesta = messagebox.askretrycancel("Error Traducción", 'Se ha producido un error inesperado.')
            if respuesta == True:
                traduccion_ingles()
    
# ---------------------- Guardar archivos -------------------------------- 
def guardar_archivo():
    resp = messagebox.askquestion(title='Guardar..', 
                                   message='¿Quiere guardar el texto actual?')
    if resp == 'yes':  
        archivo_guardado = filedialog.asksaveasfile(title="Guardar archivo...", 
                                                            defaultextension='.txt',
                                                            filetypes=(("Archivos de texto",'*.txt'),))
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
    messagebox.showinfo(title='Información', message='Conversor de texto en formato imagen a formato texto\n Vesion 1.0 (Octubre 2023)')

barra_Menu = Menu(root)
root.config(menu=barra_Menu, width=300, height=200)

opcion_Archivo = Menu(barra_Menu, tearoff=0)
opcion_Archivo.add_command(label='Salir', command=salir_Aplicacion)

opcion_Info = Menu(barra_Menu, tearoff=0)
opcion_Info.add_command(label='Ayuda', command=info_Aplicacion)

barra_Menu.add_cascade(label='Archivo', menu=opcion_Archivo)
barra_Menu.add_cascade(label='Info', menu=opcion_Info)

# ---------------- Ventanas Secundarias -------------------
''' El primer frame el donde colocamos el texto de presentacion y botones para
buscar la ruta e iniciar el escaneo. El segundo lo conpone botones de guardado y
traduccion, y el labelFrame que muestra el texto.'''
frame_botones = Frame()
frame_botones.pack(fill='both', expand='True')
frame_botones.config(bg='#333051', width=500, height=200, cursor='hand2')

frame_text = Frame()
frame_text.pack(fill='both', expand='True')
frame_text.config(bg='#333051', width=400, height=200,cursor='hand2')

mi_imagen = PhotoImage(file='textlogo.png')
Label(frame_botones, image=mi_imagen, bg='#333051').grid(row=0, column=0,
                                                         pady=20,
                                                         padx=10,
                                                         sticky='e')

# ---------------- Etiquetas de informacion y botones  -------------------
label_descrip = Label(frame_botones,text='Extraiga texto de una imagen\n con Convert-Text',
                      font=('Times', 16, 'bold'),
                      bg='#333051',
                      fg='#8DF3A8', anchor='center')
label_descrip.grid(row=0, column=1, padx=5, pady=30)

boton_buscar = Button(frame_botones, 
                      text='Buscar Ruta de la Imagen', 
                      font=('Times', 9, 'bold'),
                      bg='#258097',
                      fg='white',
                      border=2, 
                      command=abrir_archivo)
boton_buscar.grid(row=2, column=0, padx=50, pady=20, ipadx=3, ipady=3)

label_ruta = Label(frame_botones, text='..\indica la ruta del archivo.',
                   font=('Arial', 8, 'bold'), 
                   fg='#71729C',
                   bg='#333051',
                   anchor='center')
label_ruta.grid(row=2, column=1, padx=5, pady=20)

boton_iniciar = Button(frame_botones, 
                       text='Inicar Conversion', 
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
boton_guardar.grid(row=3, column=1, padx=30, pady=10)

boton_traducir_Es = Button(frame_botones, 
                       text='Traducir al Español', 
                       font=('Times', 10, 'bold'),
                       bg='#AB52A2',
                       fg='white',
                       border=2,                       
                       command=traduccion_espanol)
boton_traducir_Es.grid(row=4, column=0, padx=30, pady=10)

boton_traducir_In = Button(frame_botones, 
                       text='Traducir al Ingles', 
                       font=('Times', 10, 'bold'),
                       bg='#AB52A2',
                       fg='white',
                       border=2,
                       command=traduccion_ingles)
boton_traducir_In.grid(row=4, column=1, padx=30, pady=10)

# ---------------- Ventana para el texto -------------------
cuadro_texto= LabelFrame(frame_text,
                        text='Scan-Text',
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