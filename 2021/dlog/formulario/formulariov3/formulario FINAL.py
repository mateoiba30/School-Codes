import sqlite3
import Tkinter 
from Tkinter import *
import ttk

base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()
ventana.title("EL FORMULARIO")

valor=IntVar()
opcion=IntVar()
localidad=IntVar()
tipo=IntVar()

def validar():
    claveV=True
    valid=True
    estado=int(opcion.get())
    acepto=int(valor.get())
    tipousuario=int(tipo.get())
    
    if Enombre.get()=="":
        valid=False
        return valid
    if Eapellido.get()=="":
        valid=False
        return valid
    if Etelefono.get()=="":
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
    if tipousuario==0:
        valid=False
        return valid
    if Epassword.get()=="":
        valid=False
    if claveV==False:
        valid=False        
        return valid
    if Cacepto==0:
        valid=False
        return valid
    
    if valid==True:
        Lmensaje3=Label(ventana, text="datos verificados").grid(column=0, row=16)
        Binsertar=Button(ventana, text="insertar", command=insertar).grid(column=0, row=13)

def validar_clave():
    claveV=True
    clave=Epassword.get()
    largo=len(clave)
    x=clave.isalnum()
    if x== False:
        MSGbox.showerror(message="la clave solo puede usar letras y numeros")
        claveV=False
    if largo <8:
        MSGbox.showerror(message="clave con almenos de 8 cifras")
        claveV=False
    if largo > 50: 
        MSGbox.showerror(message="la clave tiene más de 50 caracteres")
        claveV=False
    return claveV

def insertar ():
    base=sqlite3.connect("formulario.db")
    registro=base.cursor()
    
    Inombre=Enombre.get()
    Iapellido=Eapellido.get()
    Icalle=Ecalle.get()
    Inumero=int(Enumero.get())
    Itelefono=int(Etelefono.get())
    Ilocalidad=listalocalidad.get()
    Iestado=int(opcion.get())
    Iusuario=Eusuario.get()
    Iclave=Epassword.get()
    Itipo=int(tipo.get())

    registro.execute("INSERT INTO Usuarios('tipousuario', 'nombre', 'apellido', 'calle', 'numero', 'telefono', 'localidad', 'estadocivil', 'nombreusuario', 'password') VALUES ('%d','%s', '%s','%s','%d','%d','%s','%d','%s','%s')" % (Itipo, Inombre, Iapellido, Icalle, Inumero, Itelefono, Ilocalidad, Iestado, Iusuario, Iclave))
    base.commit()


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

Lusuario=Label(ventana, text="nombre usuario*: ")
Lusuario.grid(column=0, row=6)
Eusuario=Entry(ventana, width=20)
Eusuario.grid(column=1, row=6)

Lpassword=Label(ventana, text="password*: ")
Lpassword.grid(column=0, row=7)
Epassword=Entry(ventana, width=20)
Epassword.grid(column=1, row=7)

Lestado=Label(ventana, text="estado civil*: ").grid(column=0, row=8)
Radiobutton(ventana, variable=opcion, value=1, text="soltero").grid(column=0, row=9)
Radiobutton(ventana, variable=opcion, value=2, text="casado/en pareja").grid(column=0, row=10)
Radiobutton(ventana, variable=opcion, value=3, text="divorciado").grid(column=0, row=11)
Radiobutton(ventana, variable=opcion, value=4, text="prefiero no decirlo").grid(column=0, row=12)

Cacepto=Checkbutton(text="aceptar terminos*: ", variable=valor, onvalue=1, offvalue=0).grid(column=1, row=13)

Llocalidad=Label(ventana, text="Localidad:").grid(column=6, row=0)
listalocalidad=ttk.Combobox(ventana, width=20)
listalocalidad=ttk.Combobox(values=["bariloche", "general roca", "viedma", "bahia blanca", "buenos aires"])
listalocalidad.grid(column=6, row=1)

Lestado=Label(ventana, text="tipo de usuario*: ").grid(column=6, row=3)
Radiobutton(ventana, variable=tipo, value=1, text="profesor").grid(column=6, row=4)
Radiobutton(ventana, variable=tipo, value=2, text="alumno").grid(column=6, row=5)
Radiobutton(ventana, variable=tipo, value=3, text="preceptor").grid(column=6, row=6)

Bvalidar=Button(ventana, text="validar", command=validar).grid(column=0, row=14)

Lpass=Label(ventana, text="COMPLETE LOS CAMPOS CON UN *")
Lpass.grid(column=0, row=18)

ventana.mainloop()
base.close()
