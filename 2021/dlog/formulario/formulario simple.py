import tkinter
import sqlite3
from tkinter import *

base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()
ventana.title("EL FORMULARIO")

valor=IntVar()
opcion=IntVar()
tipo=IntVar()

def validar():
    valid=True
    estado=int(opcion.get())
    acepto=int(valor.get())
    tipoh=int(tipo.get())
    
    if Enombre.get()=="":
        valid=False
        return valid
    if Eapellido.get()=="":
        valid=False
        return valid
    if Etelefono.get()=="":
        valid=False
        return valid
    if tipoh==0:
        valid=False
        return valid    
    if estado==0:
        valid=False
        return valid
    if Eusuario.get()=="":
        valid=False
        return valid
    if valor==0:
        valid=False
        return valid
    if Epassword.get()=="":
        valid=False
        return valid
    if Cacepto==0:
        valid=False
        return valid
    
    if valid==True:
        Lmensaje3=Label(ventana, text="datos verificados").grid(column=0, row=20)
        Binsertar=Button(ventana, text="insertar", command=insertar).grid(column=0, row=17)

def insertar ():
    base=sqlite3.connect("formulario.db")
    registro=base.cursor()
    
    Inombre=Enombre.get()
    Iapellido=Eapellido.get()
    Icalle=Ecalle.get()
    Inumero=int(Enumero.get())
    Itelefono=int(Etelefono.get())
    Ilocalidad=Elocalidad.get()
    Iestado=int(opcion.get())
    Iusuario=Eusuario.get()
    Iclave=Epassword.get()
    Itipo=int(tipo.get())

    instruccion="INSERT INTO Usuarios('nombre', 'apellido', 'calle', 'numero', 'telefono', 'localidad', 'estado civil', 'nombre usuario', 'password', 'tipo usuario') VALUES ('%s', '%s','%s','%d','%d','%s','%d','%s','%s', '%d')" % (Inombre, Iapellido, Icalle, Inumero, Itelefono, Ilocalidad, Iestado, Iusuario, Iclave, Itipo)
    registro.execute(instruccion)
    print(instruccion)
    base.commit


Lnombre=Label(ventana, text="nombre*: ")
Lnombre.grid(column=0, row=0)
Enombre=Entry(ventana, width=20)
Enombre.grid(column=1, row=0)

Lapellido=Label(ventana, text="apellido*: ")
Lapellido.grid(column=0, row=1)
Eapellido=Entry(ventana, width=20)
Eapellido.grid(column=1, row=1)

Lcalle=Label(ventana, text="calle: ")
Lcalle.grid(column=0, row=2)
Ecalle=Entry(ventana, width=20)
Ecalle.grid(column=1, row=2)

Lnumero=Label(ventana, text="nro calle: ")
Lnumero.grid(column=0, row=3)
Enumero=Entry(ventana, width=20)
Enumero.grid(column=1, row=3)

Ltelefono=Label(ventana, text="telefono*: ")
Ltelefono.grid(column=0, row=4)
Etelefono=Entry(ventana, width=20)
Etelefono.grid(column=1, row=4)

Llocalidad=Label(ventana, text="localidad: ")
Llocalidad.grid(column=0, row=5)
Elocalidad=Entry(ventana, width=20)
Elocalidad.grid(column=1, row=5)

Lusuario=Label(ventana, text="nombre usuario*: ")
Lusuario.grid(column=0, row=6)
Eusuario=Entry(ventana, width=20)
Eusuario.grid(column=1, row=6)

Lpassword=Label(ventana, text="password*: ")
Lpassword.grid(column=0, row=7)
Epassword=Entry(ventana, width=20)
Epassword.grid(column=1, row=7)

Ltipo=Label(ventana, text="tipo de usuario: ").grid(column=0, row=8)

Radiobutton(ventana, variable=tipo, value=1, text="alumno").grid(column=0, row=9)
Radiobutton(ventana, variable=tipo, value=2, text="maestro").grid(column=0, row=10)
Radiobutton(ventana, variable=tipo, value=3, text="preceptor").grid(column=0, row=11)


Lestado=Label(ventana, text="estado civil*: ").grid(column=0, row=12)

Radiobutton(ventana, variable=opcion, value=1, text="soltero").grid(column=0, row=13)
Radiobutton(ventana, variable=opcion, value=2, text="casado/en pareja").grid(column=0, row=14)
Radiobutton(ventana, variable=opcion, value=3, text="divorciado").grid(column=0, row=15)
Radiobutton(ventana, variable=opcion, value=4, text="prefiero no decirlo").grid(column=0, row=16)

Cacepto=Checkbutton(text="aceptar terminos*: ", variable=valor, onvalue=1, offvalue=0).grid(column=1, row=17)

Bvalidar=Button(ventana, text="validar", command=validar).grid(column=0, row=18)

Lpass=Label(ventana, text="COMPLETE LOS CAMPOS CON UN *")
Lpass.grid(column=0, row=22)

ventana.mainloop()
base.close()
