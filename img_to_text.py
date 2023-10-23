from tkinter import *
from PIL import Image
import pytesseract


# ---------------- Ventana Principal -------------------
root = Tk()

root.title('Convert-Text')
root.resizable(True,True)
root.iconbitmap('text-Img.ico')

# ---------------- Instruciones para la conversión -------------------
def convert_text():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    ruta_imagen= 'imagentexto.png'
    imagen_abierta = Image.open(ruta_imagen)
    texto = pytesseract.image_to_string(imagen_abierta)
    label_text_scan.config(text=texto)
    

# ---------------- Ventanas Secundarias -------------------
frame_botones = Frame()
frame_botones.pack(fill='both', expand='True')
frame_botones.config(bg='#333051', width=500, height=200, cursor='hand2')

frame_text = Frame()
frame_text.pack(fill='both', expand='True')
frame_text.config(bg='#333051', width=400, height=200,cursor='hand2')

mi_imagen = PhotoImage(file='textlogo-img.png')
Label(frame_botones, image=mi_imagen, bg='#333051').grid(row=0, column=0,
                                                         padx=20, pady=10,
                                                         sticky='e')

# ---------------- Etiquetas de informacion y botones  -------------------
label_descrip = Label(frame_botones,text='Extraiga texto e una imagen\n con Convert-Text',
                      font=('Times', 16, 'bold'),
                      bg='#333051',
                      fg='white')
label_descrip.grid(row=0, column=1, padx=10, pady=20)

boton_buscar = Button(frame_botones, 
                      text='Buscar Ruta', 
                      font=('Times', 9, 'bold'),
                      bg='#3CB4FA',
                      fg='white',
                      border=2)
boton_buscar.grid(row=1, column=0, padx=10, pady=20, ipadx=3, ipady=3)

label_ruta = Label(frame_botones, text='../ruta de tu imagen',
                   font=('Times', 10, 'bold'), 
                   fg='#595C7C',
                   bg='#333051',
                   width=40)
label_ruta.grid(row=1, column=1, padx=10, pady=20, sticky='w')

boton_iniciar = Button(frame_botones, 
                       text='Inicar Conversion', 
                       font=('Times', 9, 'bold'),
                       bg='#3CB4FA',
                       fg='white',
                       border=2,
                       justify='center',
                       command=convert_text)
boton_iniciar.grid(row=2, column=0,columnspan=2, padx=30, pady=10)

# ---------------- Ventana para el texto -------------------
cuadro_texto= LabelFrame(frame_text,
                        text='Scan-Text',
                        font=('Times', 8, 'bold'),
                        bg='#333051',
                        fg='white')
cuadro_texto.grid(row=0, column=0, padx=15, pady=10, sticky='ew')

label_text_scan = Label(cuadro_texto,
                        text='',
                        font=('Time', 11, 'bold'),
                        justify='left',
                        fg='white',
                        bg='#333051',
                        width=40)
label_text_scan.grid(row=0, column=0, sticky='ew')


root.mainloop()

'''label_frame= LabelFrame(frame_text, 
                        text='Scan-Text',
                        font=('Times', 8, 'bold'),
                        bg='#333051',
                        fg='white',
                        padx=2, pady=2)
label_frame.pack(padx=10, pady=10)

label_text_scan = Label(label_frame,text='',
                        font=('Time', 11, 'bold'),
                        justify='left',
                        fg='white',
                        bg='#333051',
                        width=40)
label_text_scan.pack()'''