#LIBRERIAS Y DATOS INICIALES
import sqlite3
import Tkinter 
from Tkinter import *
import ttk

base=sqlite3.connect("formulario.db3")
registro=base.cursor()
ventana=Tk()
ventana.title("AGREGAR USUARIOS")

valor=IntVar()
opcion=IntVar()
localidad=IntVar()
tipo=IntVar()

#FUNCIONES
def limpiar():
    t0=StringVar()
    t0.set(" ")
    Enombre.configure(text=t0)
    
    t1=StringVar()
    t1.set(" ")
    Eapellido.configure(text=t1)
    
    t2=StringVar()
    t2.set(" ")
    Ecalle.configure(text=t2)
    
    t3=StringVar()
    t3.set(" ")
    Enumero.configure(text=t3)
    
    t4=StringVar()
    t4.set(" ")
    Etelefono.configure(text=t4)
    
    t5=StringVar()
    t5.set(" ")
    Eusuario.configure(text=t5)

    t6=StringVar()
    t6.set(" ")
    Epassword.configure(text=t6)

    Lmensaje3=Label(ventana, text="                                             ").grid(column=0, row=16)
    Lmensaje4=Label(ventana, text="                                             ").grid(column=1, row=16)

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
        return valid
    if Cacepto==0:
        valid=False
        return valid
    
    if valid==True:
        Lmensaje3=Label(ventana, text="datos verificados").grid(column=0, row=16)

def insertar ():    
    Inombre=Enombre.get()
    Iapellido=Eapellido.get()
    Icalle=Ecalle.get()
    Itelefono=int(Etelefono.get())
    Ilocalidad=listalocalidad.get()
    Iestado=int(opcion.get())
    Iusuario=Eusuario.get()
    Iclave=Epassword.get()
    Itipo=int(tipo.get())
    if Enumero.get()!="":
        Inumero=int(Enumero.get())
    else:
        Inumero=0
    registro.execute("INSERT INTO Usuarios('tipousuario', 'nombre', 'apellido', 'calle', 'numero', 'telefono', 'localidad', 'estadocivil', 'nombreusuario', 'password') VALUES ('%d','%s', '%s','%s','%d','%d','%s','%d','%s','%s')" % (Itipo, Inombre, Iapellido, Icalle, Inumero, Itelefono, Ilocalidad, Iestado, Iusuario, Iclave))
    Lmensaje3=Label(ventana, text="datos insertados").grid(column=1, row=16)
    base.commit()

#LABELS, ENTRS, BOTONES, ETC.

#nombre
Lnombre=Label(ventana, text="nombre*: ")
Lnombre.grid(column=0, row=0)
Enombre=Entry(ventana, width=20)
Enombre.grid(column=1, row=0)

#apellido
Lapellido=Label(ventana, text="apellido*: ")
Lapellido.grid(column=0, row=1)
Eapellido=Entry(ventana, width=20)
Eapellido.grid(column=1, row=1)

#nombre calle
Lcalle=Label(ventana, text="nombre calle: ")
Lcalle.grid(column=0, row=2)
Ecalle=Entry(ventana, width=20)
Ecalle.grid(column=1, row=2)

#nro calle
Lnumero=Label(ventana, text="nro calle: ")
Lnumero.grid(column=0, row=3)
Enumero=Entry(ventana, width=20)
Enumero.grid(column=1, row=3)

#telefono
Ltelefono=Label(ventana, text="telefono*: ")
Ltelefono.grid(column=0, row=4)
Etelefono=Entry(ventana, width=20)
Etelefono.grid(column=1, row=4)

#nombre usuario
Lusuario=Label(ventana, text="nombre usuario*: ")
Lusuario.grid(column=0, row=5)
Eusuario=Entry(ventana, width=20)
Eusuario.grid(column=1, row=5)

#password
Lpassword=Label(ventana, text="password*: ")
Lpassword.grid(column=0, row=6)
Epassword=Entry(ventana, width=20)
Epassword.grid(column=1, row=6)

#estado civil
Lestado=Label(ventana, text="estado civil*: ").grid(column=2, row=0)
Radiobutton(ventana, variable=opcion, value=1, text="soltero").grid(column=2, row=1)
Radiobutton(ventana, variable=opcion, value=2, text="casado/en pareja").grid(column=2, row=2)
Radiobutton(ventana, variable=opcion, value=3, text="divorciado").grid(column=2, row=3)
Radiobutton(ventana, variable=opcion, value=4, text="prefiero no decirlo").grid(column=2, row=4)

#aceptar terminos
Cacepto=Checkbutton(text="aceptar terminos*: ", variable=valor, onvalue=1, offvalue=0).grid(column=0, row=7)

#localidad
Llocalidad=Label(ventana, text="Localidad:").grid(column=6, row=0)
listalocalidad=ttk.Combobox(ventana, width=20)
listalocalidad=ttk.Combobox(values=["Bariloche", "General Roca", "Viedma", "Bahia Blanca", "Buenos Aires", "El Bolson", "Piedra del Aguila", "Mar del Plata", "La Plata", "otro"])
listalocalidad.grid(column=6, row=1)

#tipo usuario
Lestado=Label(ventana, text="tipo de usuario*: ").grid(column=2, row=6)
Radiobutton(ventana, variable=tipo, value=1, text="profesor").grid(column=2, row=7)
Radiobutton(ventana, variable=tipo, value=2, text="alumno").grid(column=2, row=8)
Radiobutton(ventana, variable=tipo, value=3, text="preceptor").grid(column=2, row=9)

#botones
Binsertar=Button(ventana, text="insertar", command=insertar).grid(column=0, row=10)
Bvalidar=Button(ventana, text="validar", command=validar).grid(column=0, row=9)
Blimpiar=Button(ventana, text="limpiar", command=limpiar).grid(column=0, row=11)

#mensaje
Lpass=Label(ventana, text="COMPLETE LOS CAMPOS CON UN *")
Lpass.grid(column=0, row=18)

#cierre
ventana.mainloop()
base.close()
