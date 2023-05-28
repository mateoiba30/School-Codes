import sqlite3
import Tkinter 
import tkMessageBox as msg
from Tkinter import *
from ttk import *

base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()
ventana.title("EL FORMULARIO")

def estado():
    monitor=int(opcion.get())

def acepto():
    acepto=valor.get()

def validar():
    valid=True   
    if Enombre.get()=="":
        valid=False
        return valid
    if Eapellido.get()=="":
        valid=False
        return valid
    if Etelefono.get()=="":
        valid=False
        return valid
    if opcion.get()==0:
        valid=False
        return valid
    if Eusuario.get()=="":
        valid=False
        return valid
    if Eusuario.get()=="":
        valid=False
        return valid
    if Epassword.get()=="":
        valid=False
        return valid
    if acepto_terminos==0:
        valid=False
        return valid
    if valid==True:
        Lmensaje3=Label(ventana, text="datos verificados").grid(column=0, row=16)
        Binsertar=Button(ventana, text="insertar", command=insertar).grid(column=0, row=13)
    else:
        Lmensaje4=Label(ventana, text="datos verificados").grid(column=0, row=17)

def insertar ():
    Inombre=Enombre.get()
    Iapellido=Eapellido.get()
    Icalle=Ecalle.get()
    Inumero=int(Enumero.get())
    Itelefono=int(Etelefono.get())
    Ilocalidad=Elocalidad.get()
    Iestado=int(Eestado.get())
    Iusuario=Eusuario.get()
    Iclave=Epassword.get()

    instruccion="INSERT INTO Usuarios('nombre', 'apellido', 'calle', 'numero', 'telefono', 'localidad', 'estado civil', 'nombre usuario', 'password') VALUES ('%s', '%s','%s','%d','%d','%s','%d','%s','%s')" % (Inombre, Iapellido, Icalle, Inumero, Itelefono, Ilocalidad, Iestado, Iusuario, Iclave)
    registro.execute(instruccion)
    print(instruccion)
    base.commit()

    for fila in registro:
        coincide=True

    if registro:
        Lmensaje1=Label(ventana, text="datos agregados").grid(column=0, row=14)
    else:
        Lmensaje2=Label(ventana, text="datos NO agregados").grid(column=0, row=15)


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

Lpass=Label(ventana, text="password*: ")
Lpass.grid(column=0, row=7)
Epass=Entry(ventana, width=20)
Epass.grid(column=1, row=7)

monitor=Label(ventana, text="estado civil*: ").grid(column=0, row=8)
frame=Frame(ventana)
frame.grid(column=3, row=3)
opcion=IntVar()
Radiobutton(ventana, variable=opcion, value=1, text="soltero").grid(column=0, row=9)
Radiobutton(ventana, variable=opcion, value=2, text="casado/en pareja").grid(column=0, row=10)
Radiobutton(ventana, variable=opcion, value=3, text="divorciado").grid(column=0, row=11)
Radiobutton(ventana, variable=opcion, value=4, text="prefiero no decirlo").grid(column=0, row=12)

valor=IntVar()
Cacepto=Checkbutton(text="aceptar terminos*: ", variable=valor, command=acepto, onvalue=1, offvalue=0).grid(column=1, row=13)

Bvalidar=Button(ventana, text="validar", command=validar).grid(column=0, row=14)

Lpass=Label(ventana, text="COMPLETE LOS CAMPOS CON UN *")
Lpass.grid(column=0, row=18)

ventana.mainloop()
