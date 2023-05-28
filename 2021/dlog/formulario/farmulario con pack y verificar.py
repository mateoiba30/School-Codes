from tkinter import *
import sqlite3
import tkinter

base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()

opcion = IntVar()
opcion.set(0)

buton = IntVar()
opcion.set(0)

frame = Frame(ventana)

estado_completo=False

valid=False

label_nombre=Label(ventana, text="nombre*: ")
label_nombre.grid(column=0, row=0)
entry_nombre=Entry(ventana, width=20)
entry_nombre.grid(column=1, row=0)

label_apellido=Label(ventana, text="apellido*: ")
label_apellido.grid(column=0, row=1)
entry_apellido=Entry(ventana, width=20)
entry_apellido.grid(column=1, row=1)

label_calle=Label(ventana, text="calle: ")
label_calle.grid(column=0, row=2)
entry_calle=Entry(ventana, width=20)
entry_calle.grid(column=1, row=2)

label_numero=Label(ventana, text="nro calle: ")
label_numero.grid(column=0, row=3)
entry_numero=Entry(ventana, width=20)
entry_numero.grid(column=1, row=3)

label_telefono=Label(ventana, text="telefono*: ")
label_telefono.grid(column=0, row=4)
entry_telefono=Entry(ventana, width=20)
entry_telefono.grid(column=1, row=4)

label_localidad=Label(ventana, text="localidad: ")
label_localidad.grid(column=0, row=5)
entry_localidad=Entry(ventana, width=20)
entry_localidad.grid(column=1, row=5)

label_usuario=Label(ventana, text="nombre usuario*: ")
label_usuario.grid(column=0, row=6)
entry_usuario=Entry(ventana, width=20)
entry_usuario.grid(column=1, row=6)

label_pass=Label(ventana, text="password*: ")
label_pass.grid(column=0, row=7)
entry_pass=Entry(ventana, width=20)
entry_pass.grid(column=1, row=7)

entry_errores=Label(ventana, text="")

monitor=Label(ventana, text="estado civil*: ").grid(column=0, row=8)

frame=Frame(ventana)
opcion=IntVar()
Radiobutton(ventana, variable=opcion, value=1, text="soltero").grid(column=0, row=9)
Radiobutton(ventana, variable=opcion, value=2, text="casado/en pareja").grid(column=0, row=10)
Radiobutton(ventana, variable=opcion, value=3, text="divorciado").grid(column=0, row=11)
Radiobutton(ventana, variable=opcion, value=4, text="prefiero no decirlo").grid(column=0, row=12)

def estado_civil():
    monitor=int(opcion.get())
    estado_completo=True
    
def insert():
    registro=base.cursor()
    NOMBRE=entry_nombre.get() 
    APELLIDO=entry_apellido.get()
    CALLE=entry_calle.get()
    NUMERO=int(entry_numero.get())
    TELEFONO=int(entry_telefono.get())
    LOCALIDAD=entry_localidad.get()
    USUARIO=entry_usuario.get()
    ESTADO=int(opcion.get())
    registro.execute("INSERT INTO Usuarios('nombre', 'apellido', 'calle', 'numero', 'telefono', 'localidad', 'estado civil', 'usuario') VALUES ('%s', '%s', '%s', '%d', '%d', '%s', '%d', '%s')" %(NOMBRE, APELLIDO, CALLE, NUMERO, TELEFONO, LOCALIDAD, ESTADO, USUARIO))      
    base.commit()

    cadena="datos agregados"    

def validar():
    valid=True   
    if entry_nombre.get()=="":
        valid=False
        return valid
    if entry_apellido.get()=="":
        valid=False
        return valid
    if entry_telefono.get()=="":
        valid=False
        return valid
    if estado_completo==True:
        valid=False
        return valid
    if entry_usuario.get()=="":
        valid=False
        return valid
    if buton==0:
        valid=False
        return valid

if __name__=="__main__":

    Label(ventana,text="acepto términos*").grid(column=0, row=13)
    Checkbutton(ventana, variable=buton, onvalue=1, offvalue=0).grid(column=1, row=13)
    
    boton=Button(ventana, text="AGREGAR", command=validar)
    boton.grid(column=0, row=14)

    if valid==True:
        insert()
    else:
        label_errores=Label(ventana, text="complete los campos con un *").grid(column=0, row=16)
        
    monitor=Label(frame)
    
    ventana.mainloop()
    base.close()


