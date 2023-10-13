from tkinter import *
from PIL import ImageTk, Image

def identificar():
    l1 = int(cuadro_n1.get())
    l2 = int(cuadro_n2.get())
    l3 = int(cuadro_n3.get())
    if l1 == l2 and l1 == l3 and l2 == l3:
        res = "Triangulo equilátero"
        cargaImagen( "equilatero.png")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        res = "Triangulo isósceles"
        cargaImagen( "isosceles.png")
    else:
        res = "Triangulo escaleno"
        cargaImagen( "escaleno.png")

    resultado.configure(text="Resultado: "+res)

def cargaImagen(imagen):
    img = ImageTk.PhotoImage(Image.open(imagen))
    panel.configure(image=img)
    panel.image = img

raiz = Tk()
raiz.geometry("600x500")
raiz.title("Detectando tipos de triangulos segun lados")
miFrame= Frame()
miFrame.pack()
bienvenido = Label(miFrame, text="Detector de tipos de triangulos")
bienvenido.grid(row=0, column=0)
bienvenido.config(font=('Arial', 16))
n1= Label(miFrame, text="Ingrese lado 1:")
n1.grid(row=1, column=0)
n1.config(padx=10, pady=10)
cuadro_n1 = Entry(miFrame)
cuadro_n1.grid(row=1, column=1)
n2=Label(miFrame, text="Ingrese lado 2: ")
n2.grid(row=2, column=0)
n2.config(padx=10, pady=10)
cuadro_n2 = Entry(miFrame)
cuadro_n2.grid(row=2, column=1)
n3=Label(miFrame, text="Ingrese lado 3: ")
n3.grid(row=3, column=0)
n3.config(padx=10, pady=10)
cuadro_n3 = Entry(miFrame)
cuadro_n3.grid(row=3, column=1)
resultado=Label(miFrame, text="Resultado: ")
resultado.grid(row=4, column=0)
resultado.config(padx=10, pady=10)
#-----Seccion botones-----
boton1 = Button(miFrame, text="Indentificar triangulo",command=identificar)
boton1.grid( row=5, column=1)
# -----Imagenes-------
img = ImageTk.PhotoImage(Image.open("iacc.png"))
panel = Label( image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

raiz.mainloop()
