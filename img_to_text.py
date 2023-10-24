from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import pytesseract


# ---------------- Ventana Principal -------------------
root = Tk()

root.title('Convert-Text')
root.resizable(False, False)
root.iconbitmap('text-Img.ico')
# ---------------- Ventanas secundarias -------------------
def error_busqueda():
    respuesta = messagebox.askretrycancel("Error en la Busqueda", 'Archivo o Ruta especificada\n no es correcta.')
    if respuesta == True:
        abrir_archivo()

# ---------------- Instruciones para la conversión -------------------
def abrir_archivo():
    ''' Función que nos permite hacer la busqueda del archivo que escanearemos su texto.'''
    global archivo
    try:
        archivo = filedialog.askopenfilenames(title="Buscar Archivo", 
                                            initialdir="C:/",
                                            filetypes=(("Archivos de imagen",''), ('JPG','*.jpg'), ('PNG','*.png'), ('BMP','*.bmp')))
    except: error_busqueda()

    '''Atraves del config, modificamos el texto de la Etiqueta, para mostrar el path del archivo.'''
    label_ruta.config(text=archivo[0])

def convert_text():
    ''' Función con la que abrimos el programa que realiza la tarea de conversión.
    Ser realiza una apertura del archivo, el escaneo del texto y su guardado, y lo enviamos
     a la etiqueta que lo imprime en pantalla. '''
    try:    
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        ruta_imagen= archivo[0]
        imagen_abierta = Image.open(ruta_imagen, mode='r')
        texto = pytesseract.image_to_string(imagen_abierta)
        label_text_scan.config(text=texto)
    except: error_busqueda()
    
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

mi_imagen = PhotoImage(file='textlogo-img.png')
Label(frame_botones, image=mi_imagen, bg='#333051').grid(row=0, column=0,
                                                         pady=10,
                                                         sticky='e')

# ---------------- Etiquetas de informacion y botones  -------------------
label_descrip = Label(frame_botones,text='Extraiga texto e una imagen\n con Convert-Text',
                      font=('Times', 16, 'bold'),
                      bg='#333051',
                      fg='white')
label_descrip.grid(row=0, column=1, padx=15, pady=20)

boton_buscar = Button(frame_botones, 
                      text='Buscar Ruta', 
                      font=('Times', 9, 'bold'),
                      bg='#3CB4FA',
                      fg='white',
                      border=2, command=abrir_archivo)
boton_buscar.grid(row=1, column=0, padx=20, pady=20, ipadx=3, ipady=3)

label_ruta = Label(frame_botones, text='..\indica la ruta del archivo.',
                   font=('Arial', 8, 'bold'), 
                   fg='#71729C',
                   bg='#333051',anchor='center')
label_ruta.grid(row=1, column=1, padx=5, pady=20)

boton_iniciar = Button(frame_botones, 
                       text='Inicar Conversion', 
                       font=('Times', 9, 'bold'),
                       bg='#3CB4FA',
                       fg='white',
                       border=2,
                       command=convert_text)
boton_iniciar.grid(row=2, column=0,columnspan=2, padx=30, pady=10,)

# ---------------- Ventana para el texto -------------------
cuadro_texto= LabelFrame(frame_text,
                        text='Scan-Text',
                        font=('Times', 8, 'bold'),
                        bg='#333051',
                        fg='white')
cuadro_texto.grid(row=0, column=0, padx=15, pady=10, sticky='we')

label_text_scan = Label(cuadro_texto,
                        text='',
                        font=('Time', 11, 'bold'),
                        justify='left',
                        fg='white',
                        bg='#333051',
                        width=60, anchor='center')
label_text_scan.grid(row=0, column=0, sticky='ew')


root.mainloop()