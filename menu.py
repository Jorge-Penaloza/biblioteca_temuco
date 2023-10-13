#from logging import disable
from logging import NullHandler, disable
from tkinter import * 
from tkinter import messagebox as MessageBox
from tkinter import ttk
from  usuarios import Usuarios
from libros import Libros
from colaboradores import Colaborador
from datetime import date, datetime
from prestamo import Prestamo
def ayuda():
    MessageBox.showinfo("Ayuda", "Sistema de ayuda esta en desarrollo")

def acercaDe():
    MessageBox.showinfo("Sistema de biblioteca", "Sistema de biblioteca creado por Jorge Peñaloza")

def ventana_inicio():
    global ventana_principal
    global filemenu
    global usermenu
    global accesomenu
    global menubar
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("600x400") #DIMENSIONES DE LA VENTANA
    ventana_principal.title("Sistema de biblioteca") #TITULO DE LA VENTANA

    menubar =Menu(ventana_principal)
    ventana_principal.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Prestamo", command=prestamo)
    filemenu.add_command(label="Devolucion", command=devolucion)
    filemenu.add_separator()
    filemenu.add_command(label="Listado de libros", command=listaLibros ) 
    filemenu.add_command(label="Listado de colaboradores", command=listaColaboraciones ) 
    filemenu.add_separator()
    filemenu.add_command(label="Mantenedor de libros", command=crudLibros ) 
    
    

    usermenu = Menu(menubar, tearoff=0)
    usermenu.add_command(label="Mantenedor de usuarios", command=crudUsuarios)
    usermenu.add_command(label="Lista de usuarios", command=listaUsuarios)
    

    accesomenu = Menu(menubar, tearoff=0)
    accesomenu.add_command(label="Iniciar sesión", command=login)
    accesomenu.add_command(label="Cerrar sesión", comman=exitLogin)
    accesomenu.entryconfig(index=0, state=NORMAL)
    accesomenu.entryconfig(index=1, state=DISABLED)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda", command=ayuda)
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...", command=acercaDe)

    menubar.add_cascade(label="Libros", menu=filemenu)
    menubar.add_cascade(label="Usuarios", menu=usermenu)
    menubar.add_cascade(label="Acceso", menu=accesomenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    menubar.add_command(label="Salir", command=ventana_principal.quit)
    menubar.entryconfig(index=1, state=DISABLED)
    menubar.entryconfig(index=2, state=DISABLED)
    menubar.entryconfig(index=3, state=NORMAL)

    ventana_principal.mainloop()

def devolucion():
    global entrada_usuario
    global entrada_libro
    global libros_
    global ventana_devolucion  


    ventana_devolucion = Toplevel(ventana_principal)
    ventana_devolucion.title("Devolución de libros")
    ventana_devolucion.geometry("250x300")

    Label(ventana_devolucion, text="Introduzca datos de devolucion", bg="LightGreen").pack()
    Label(ventana_devolucion, text="").pack()

    usuarios_ = []
    pre = Prestamo()
    usuarios_prestamo = pre.usuariosConPrestamo()
    for registro in usuarios_prestamo:
       usuarios_.append(registro[0])
    
    etiqueta_usuario = Label(ventana_devolucion, text="Usuarios con prestamo pendiente")
    etiqueta_usuario.pack()
    entrada_usuario =  ttk.Combobox (ventana_devolucion, state="readonly")
    entrada_usuario["values"]   = usuarios_
    entrada_usuario.pack()
    
    Button(ventana_devolucion, text="Buscar libros de usuario", width=20, height=1, bg="LightGreen", command = librosPrestamo).pack()

    etiqueta_libro = Label(ventana_devolucion, text="Libros de usuario con prestamo pendiente")
    etiqueta_libro.pack()
    entrada_libro =  ttk.Combobox (ventana_devolucion, state="readonly")
    entrada_libro["values"]   = []
    entrada_libro.pack()

    Button(ventana_devolucion, text="Efectuar devolucion", width=20, height=1, bg="LightGreen", command = librosDevolucion).pack()

def librosDevolucion():
    usuario_ = entrada_usuario.get().strip()
    libro_ = entrada_libro.get().strip()
    if usuario_ == "" or libro_ == "":
        MessageBox.showerror(message="Debe seleccionar usuario y libro a devolver")
    else:
        libro = Libros()
        (existe, datos) = libro.buscar(libro_)
        if existe:
            cant = datos[0][5]
            libro.cambiarCantidad(libro_, int(cant) + 1)
            pres = Prestamo()
            pres.devolver( usuario_, libro_)
            MessageBox.showinfo(message="Devolucion exitosa!")
        else:
            MessageBox.showinfo(message="Libro no existe!")
    
    ventana_devolucion.destroy()
    

def librosPrestamo():
    usuario = entrada_usuario.get()
    libros_ = []
    pre = Prestamo()
    libros_prestamo = pre.librosConPrestamo(usuario)
    for registro in libros_prestamo:
       libros_.append(registro[0])
    entrada_libro["values"]   = libros_

def prestamo():
    global ventana_prestamo
    global entrada_fecha
    global fecha_prestamo
    global entrada_hora
    global hora_prestamo
    global usuario_prestamo
    global tipo_usuario
    global entrada_usuario
    global usuario_prestamo
    global entrada_prestamo
    global prestamo_prestamo
    global etiqueta_colaborador
    global entrada_colaborador
    global entrada_libro
    global libro_prestamo
    global combo

    fecha_prestamo = StringVar()
    hora_prestamo = StringVar()
    usuario_prestamo =StringVar()
    prestamo_prestamo = IntVar()
    libro_prestamo = StringVar()

    ventana_prestamo = Toplevel(ventana_principal)
    ventana_prestamo.title("Prestamo de libros")
    ventana_prestamo.geometry("300x420")

    Label(ventana_prestamo, text="Introduzca datos de prestamo", bg="LightGreen").pack()
    Label(ventana_prestamo, text="").pack()
    
    etiqueta_prestamo = Label(ventana_prestamo, text="Prestamo")
    etiqueta_prestamo.pack()
    entrada_prestamo = Entry(ventana_prestamo, textvariable=prestamo_prestamo) 
    entrada_prestamo.pack()
    entrada_prestamo.delete(0, END)

    pre = Prestamo()
    (existe, ultimo_prestamo) = pre.ultimoPrestamo()
    if existe:
        if ultimo_prestamo[0][0] == None:
            entrada_prestamo.insert(0, 1)
        else:
            entrada_prestamo.insert(0, ultimo_prestamo[0][0])
    else:
        entrada_prestamo.insert(0, 1)

    entrada_prestamo.configure(state="readonly")
    etiqueta_fecha = Label(ventana_prestamo, text="Fecha")
    etiqueta_fecha.pack()
    entrada_fecha = Entry(ventana_prestamo, textvariable=fecha_prestamo) 
    entrada_fecha.pack()

    etiqueta_hora = Label(ventana_prestamo, text="Hora")
    etiqueta_hora.pack()
    entrada_hora = Entry(ventana_prestamo, textvariable=hora_prestamo) 
    entrada_hora.pack()

    entrada_fecha.delete(0, END)
    entrada_fecha.insert(0,datetime.now().strftime('%Y-%m-%d'))

    entrada_hora.delete(0, END)
    entrada_hora.insert(0,datetime.now().strftime('%H:%M:%S'))

    #checkbox_value = BooleanVar()
    #tipo_usuario = Checkbutton(ventana_prestamo, text="Usuario interno ..", variable=checkbox_value)
    #tipo_usuario.pack()
    #checkbox_value.set(TRUE)
    colab = Colaborador()
    datos = colab.listado()
    combo = []
    for reg in datos:
        combo.append(reg[0] + ": " + reg[1])
    etiqueta_colaborador = Label(ventana_prestamo, text="Codigo de colaborador")
    etiqueta_colaborador.pack()
    entrada_colaborador =  ttk.Combobox (ventana_prestamo, state="readonly")
    entrada_colaborador["values"]   = combo
    entrada_colaborador.pack()

    etiqueta_usuario = Label(ventana_prestamo, text="RUT(Externo)/Usuario(Interno) ")
    etiqueta_usuario.pack()
    entrada_usuario = Entry(ventana_prestamo, textvariable=usuario_prestamo) 
    entrada_usuario.pack()

    etiqueta_libro = Label(ventana_prestamo, text="Codigo de libro")
    etiqueta_libro.pack()
    entrada_libro = Entry(ventana_prestamo, textvariable=libro_prestamo) 
    entrada_libro.pack()

    Label(ventana_prestamo, text="").pack()
    
    Button(ventana_prestamo, text="Efectuar prestamo", width=15, height=1, bg="LightGreen", command = guardarPrestamo).pack() 
    Button(ventana_prestamo, text="Cancelar", width=15, height=1, bg="LightYellow", command = cerrar_prestamo).pack() 

def cerrar_prestamo():
    ventana_prestamo.destroy()

def guardarPrestamo():

    prestamo_ = prestamo_prestamo.get()
    fecha_ = fecha_prestamo.get()
    hora_ = hora_prestamo.get()
    usuario_ = usuario_prestamo.get()
    codigo_libro_ = libro_prestamo.get()
    codigo_colaborador = entrada_colaborador.get()

    if prestamo_ == "" or fecha_.strip() == "" or hora_.strip() == "" or usuario_.strip() == "" or codigo_libro_.strip() == "" or codigo_colaborador.strip() == "":
        MessageBox.showwarning(message="No pueden haber campos vacios para efectuar prestamo")        
    else:
        libro = Libros()
        (existe, datos) = libro.buscar(codigo_libro_)
        if existe:
            cant = datos[0][5]
            libro.cambiarCantidad(codigo_libro_, int(cant) - 1)
            pres = Prestamo()
            pres.insertar( prestamo_, fecha_, hora_, usuario_, codigo_libro_,codigo_colaborador,"En préstamo")
            MessageBox.showinfo(message="Prestamo exitoso")
        else:
            MessageBox.showinfo(message="Libro no existe!")
    ventana_prestamo.destroy()

def crudLibros():
    global ventana_registro_libros
    ventana_registro_libros = Toplevel(ventana_principal)
    ventana_registro_libros.title("Mantenedor de libros")
    ventana_registro_libros.geometry("300x420")

    global codigo_libro
    global nombre_libro
    global autor_libro
    global descripcion_libro
    global anio_libro
    global cantidad_libro
    global entrada_codigo
    global entrada_nombreL
    global entrada_descripcion
    global entrada_anio
    global entrada_cantidad
    global entrada_autor

    codigo_libro = StringVar() 
    nombre_libro = StringVar()
    autor_libro = StringVar() 
    descripcion_libro = StringVar() 
    anio_libro = StringVar() 
    cantidad_libro = StringVar() 

    Label(ventana_registro_libros, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro_libros, text="").pack()


    etiqueta_codigo = Label(ventana_registro_libros, text="Codigo de libro")
    etiqueta_codigo.pack()
    entrada_codigo = Entry(ventana_registro_libros, textvariable=codigo_libro) 
    entrada_codigo.pack()

    etiqueta_nombre = Label(ventana_registro_libros, text="Nombre de libro")
    etiqueta_nombre.pack()
    entrada_nombreL = Entry(ventana_registro_libros, textvariable=nombre_libro) 
    entrada_nombreL.pack()

    etiqueta_autor = Label(ventana_registro_libros, text="Autor de libro")
    etiqueta_autor.pack()
    entrada_autor = Entry(ventana_registro_libros, textvariable=autor_libro) 
    entrada_autor.pack()

    etiqueta_descripcion = Label(ventana_registro_libros, text="Descripcion")
    etiqueta_descripcion.pack()
    entrada_descripcion = Entry(ventana_registro_libros, textvariable=descripcion_libro) 
    entrada_descripcion.pack()

    etiqueta_anio = Label(ventana_registro_libros, text="Año")
    etiqueta_anio.pack()
    entrada_anio = Entry(ventana_registro_libros, textvariable=anio_libro) 
    entrada_anio.pack()

    etiqueta_cantidad = Label(ventana_registro_libros, text="Cantidad")
    etiqueta_cantidad.pack()
    entrada_cantidad = Entry(ventana_registro_libros, textvariable=cantidad_libro) 
    entrada_cantidad.pack()

    Label(ventana_registro_libros, text="").pack()
    

    Button(ventana_registro_libros, text="Buscar", width=10, height=1, bg="LightGreen", command = buscar_libro).pack() 
    Button(ventana_registro_libros, text="Actualizar", width=10, height=1, bg="LightYellow", command = actualizar_libro).pack() 
    Button(ventana_registro_libros, text="Eliminar", width=10, height=1, bg="#F25245", command = eliminar_libro).pack() 
    Button(ventana_registro_libros, text="Limpiar", width=10, height=1, bg="Green", command = limpiar_libro).pack() 

def listaColaboraciones():
    global ventana_lista_colaborador
    ventana_lista_colaborador = Toplevel(ventana_principal)
    ventana_lista_colaborador.title("Lista de colaboradores")
    ventana_lista_colaborador.geometry("300x150")
    user = Colaborador()
    datos = user.listado()
    #datos.insert(0,["Nombre de usuario","Usuario","Perfil"])
    #Table(ventana_lista_usuarios,datos)
    tabla=ttk.Treeview(ventana_lista_colaborador,selectmode=BROWSE,height=10,columns="Nombre" )
    tabla.grid(row=10,column=0,columnspan=2)

    tabla.column("#0",width=50)
    tabla.column("Nombre",width=150)
    
    tabla.heading("#0",text="Codigo",anchor=CENTER)
    tabla.heading("Nombre",text="Nombre",anchor=CENTER)
    
    for elemento in datos:
            tabla.insert("",0,text=elemento[0],values=elemento[1])

def buscar_libro():
    codigo_ = codigo_libro.get()
    libro = Libros()
    (existe, datos) = libro.buscar(codigo_)
    if existe:
        entrada_codigo.configure (state="readonly")
        entrada_nombreL.delete(0, END)
        entrada_nombreL.insert(0,datos[0][1])
        entrada_autor.delete(0, END)
        entrada_autor.insert(0,datos[0][2])
        entrada_descripcion.delete(0, END)
        entrada_descripcion.insert(0,datos[0][3])
        entrada_anio.delete(0, END)
        entrada_anio.insert(0,datos[0][4])
        entrada_cantidad.delete(0, END)
        entrada_cantidad.insert(0,datos[0][5])
    else:
        MessageBox.showerror(message="Usuario no existe!")
    
def actualizar_libro():
    codigo_ = codigo_libro.get()
    nombre_ = nombre_libro.get()
    autor_ = autor_libro.get()
    descripcion_ = descripcion_libro.get()
    anio_ = anio_libro.get()
    cantidad_ = cantidad_libro.get()
    if codigo_.strip() == "" or nombre_.strip() == "" or autor_.strip() == "" or descripcion_.strip() == "" or anio_.strip() == "" or cantidad_.strip() == "":
        MessageBox.showwarning(message="No pueden haber campos vacios para actualizar")        
    else:
        libro = Libros()
        (existe, datos) = libro.buscar(codigo_)
        if existe:
            libro.actualizar(codigo_,nombre_,autor_,descripcion_,anio_,cantidad_)
            MessageBox.showinfo(message="Libro modificado exitosamente!")
        else:
            libro.insertar(codigo_,nombre_,autor_,descripcion_,anio_,cantidad_)
            MessageBox.showinfo(message="Libro agregado exitosamente!")
        limpiar_libro()

def eliminar_libro():
    codigo_ = codigo_libro.get()
    nombre_ = nombre_libro.get()
    autor_ = autor_libro.get()
    mensaje = "Esta seguro de eliminar a "+nombre_+ " escrito por "+ autor_
    resp = MessageBox.askquestion(title="Sistema de biblioteca", message=mensaje)
    if resp == "yes":
        libro = Libros()
        libro.eliminar(codigo_)
    limpiar_libro()

def limpiar_libro():
    entrada_codigo.configure (state=NORMAL)
    entrada_codigo.delete(0, END)
    entrada_codigo.insert(0,"")
    entrada_nombreL.delete(0, END)
    entrada_nombreL.insert(0,"")
    entrada_autor.delete(0, END)
    entrada_autor.insert(0,"")
    entrada_descripcion.delete(0, END)
    entrada_descripcion.insert(0,"")
    entrada_anio.delete(0, END)
    entrada_anio.insert(0,"")
    entrada_cantidad.delete(0, END)
    entrada_cantidad.insert(0,"")

def listaLibros():
    global ventana_lista_libros
    ventana_lista_libros = Toplevel(ventana_principal)
    ventana_lista_libros.title("Lista de libros")
    ventana_lista_libros.geometry("760x250")
    user = Libros()
    datos = user.listado()
    #datos.insert(0,["Nombre de usuario","Usuario","Perfil"])
    #Table(ventana_lista_usuarios,datos)
    tabla=ttk.Treeview(ventana_lista_libros,selectmode=BROWSE,height=10,columns=("Nombre","Autor","Descripción","Año","Cantidad" ))
    tabla.grid(row=10,column=0,columnspan=2)

    tabla.column("#0",width=50)
    tabla.column("Nombre",width=150)
    tabla.column("Autor",width=100)
    tabla.column("Descripción",width=250)
    tabla.column("Año",width=100)
    tabla.column("Cantidad",width=100)
    
    tabla.heading("#0",text="Codigo",anchor=CENTER)
    tabla.heading("Nombre",text="Nombre",anchor=CENTER)
    tabla.heading("Autor",text="Autor",anchor=CENTER)
    tabla.heading("Descripción",text="Descripción",anchor=CENTER)
    tabla.heading("Año",text="Año",anchor=CENTER)
    tabla.heading("Cantidad",text="Cantidad",anchor=CENTER)
    
    for elemento in datos:
            tabla.insert("",0,text=elemento[0],values=(elemento[1], elemento[2], elemento[3], elemento[4], elemento[5]))

def listaUsuarios():
    global ventana_lista_usuarios
    ventana_lista_usuarios = Toplevel(ventana_principal)
    ventana_lista_usuarios.title("Lista de usuarios")
    ventana_lista_usuarios.geometry("402x250")
    user = Usuarios()
    datos = user.listado()
    #datos.insert(0,["Nombre de usuario","Usuario","Perfil"])
    #Table(ventana_lista_usuarios,datos)
    tabla=ttk.Treeview(ventana_lista_usuarios,selectmode=BROWSE,height=10,columns=("Usuario","Perfil"))
    tabla.grid(row=10,column=0,columnspan=2)
    tabla.column("#0",width=200)
    tabla.column("Usuario",width=100)
    tabla.column("Perfil",width=100)
    tabla.heading("#0",text="Nombre de usuario",anchor=CENTER)
    tabla.heading("Usuario",text="Usuario",anchor=CENTER)
    tabla.heading("Perfil",text="Perfil",anchor=CENTER)
    
    for elemento in datos:
            tabla.insert("",0,text=elemento[0],values=(elemento[1], elemento[2]))

def crudUsuarios():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global nombre_usuarioC
    global clave
    global entrada_nombre
    global entrada_nombreC
    global entrada_clave
    global perfil
    nombre_usuario = StringVar() 
    nombre_usuarioC = StringVar()
    clave = StringVar() 
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()

    etiqueta_nombre = Label(ventana_registro, text="Usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) 
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()
    etiqueta_perfil = Label(ventana_registro, text="Perfil de usuario")
    etiqueta_perfil.pack()
    perfil =  ttk.Combobox (ventana_registro, state="readonly")
    perfil["values"]   = ["A: Administrador","U: Usuario"]
    perfil.pack()
    etiqueta_nombreC = Label(ventana_registro, text="Nombre del usuario")
    etiqueta_nombreC.pack()
    entrada_nombreC = Entry(ventana_registro, textvariable=nombre_usuarioC) 
    entrada_nombreC.pack()

    Label(ventana_registro, text="").pack()


    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() 

def exitLogin():
    menubar.entryconfig(index=1, state=DISABLED)
    menubar.entryconfig(index=2, state=DISABLED)
    menubar.entryconfig(index=3, state=NORMAL) 
    accesomenu.entryconfig(index=0, state=NORMAL)
    accesomenu.entryconfig(index=1, state=DISABLED)
    filemenu.entryconfig(index=0, state=DISABLED)
    filemenu.entryconfig(index=1, state=DISABLED)
    filemenu.entryconfig(index=3, state=DISABLED)
    filemenu.entryconfig(index=4, state=DISABLED)
    filemenu.entryconfig(index=6, state=DISABLED)
    
def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    #ventana_login = Tk()
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()
    entrada_login_usuario.focus_set()

def habilitarAdministrador():
    menubar.entryconfig(index=1, state=NORMAL)
    menubar.entryconfig(index=2, state=NORMAL)
    menubar.entryconfig(index=3, state=NORMAL) 
    accesomenu.entryconfig(index=0, state=DISABLED)
    accesomenu.entryconfig(index=1, state=NORMAL)
    filemenu.entryconfig(index=0, state=NORMAL)
    filemenu.entryconfig(index=1, state=NORMAL)
    filemenu.entryconfig(index=3, state=NORMAL)
    filemenu.entryconfig(index=4, state=NORMAL)
    filemenu.entryconfig(index=6, state=NORMAL)

def habilitarUsuario():
    menubar.entryconfig(index=1, state=NORMAL)
    menubar.entryconfig(index=2, state=DISABLED)
    menubar.entryconfig(index=3, state=NORMAL) 
    accesomenu.entryconfig(index=0, state=DISABLED)
    accesomenu.entryconfig(index=1, state=NORMAL)
    filemenu.entryconfig(index=0, state=DISABLED)
    filemenu.entryconfig(index=1, state=DISABLED)
    filemenu.entryconfig(index=3, state=NORMAL)
    filemenu.entryconfig(index=4, state=NORMAL)
    filemenu.entryconfig(index=6, state=DISABLED)

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    acceso = Usuarios()
    (existencia, datos) = acceso.buscar(usuario1,clave1)
    entrada_login_usuario.delete(0, END) 
    entrada_login_clave.delete(0, END) 
    
    if existencia:
        
        titulo = "Sistema de biblioteca con acceso a "
        titulo += datos[0][0] + "[[ perfil: "+ datos[0][1] +"]]"
        if datos[0][1] == "A":
            habilitarAdministrador()
        if datos[0][1] == "U":
            habilitarUsuario()
        ventana_principal.title(titulo)
        ventana_login.destroy()
        
    else:
        
        MessageBox.showinfo(message="Usuario no existe o hay error de contraseña")
        ventana_login.destroy()
 

 
 

def registro_usuario():
 
    usuario_info = entrada_nombre.get()
    nombre_info = entrada_nombreC.get()
    clave_info = entrada_clave.get()
    perilUsuario = perfil.get()
    acceso = Usuarios()
    (existencia, datos) = acceso.buscarUsuario(usuario_info)
  
    if existencia:
        mensaje = "Usuario " + datos[0][0] + " ya existe "
        mensaje += "¿Ésta seguro de cambiar contraseña ?"
        resp = MessageBox.askquestion(title="Sistema de biblioteca", message=mensaje)
        if resp == "yes":
            try:
                acceso.actualizar(usuario_info,clave_info,perilUsuario[0:1],nombre_info)
            except:
                MessageBox.showerror(message="Error al ingresar Usuario")
    else:
        mensaje = "Usuario " + nombre_info + " NO existe "
        mensaje += "¿Ésta seguro de agregar usuario ?"
        resp = MessageBox.askquestion(title="Sistema de biblioteca", message=mensaje)
        if resp == "yes":
            try:
                acceso.insertar(usuario_info,clave_info,perilUsuario[0:1],nombre_info)
            except:
                MessageBox.showerror(message="Error al ingresar Usuario")
        
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
    ventana_registro.destroy()
    #Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
 
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
