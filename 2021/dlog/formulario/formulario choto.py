from tkinter import *
import sqlite3
base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()
opcion = IntVar()


label_nombre=Label(ventana, text="nombre: ")
label_nombre.grid(column=0, row=0)
entry_nombre=Entry(ventana, width=20)
entry_nombre.grid(column=1, row=0)

label_apellido=Label(ventana, text="apellido: ")
label_apellido.grid(column=0, row=1)
entry_apellido=Entry(ventana, width=20)
entry_apellido.grid(column=1, row=1)

label_calle=Label(ventana, text="calle: ")
label_calle.grid(column=0, row=2)
entry_calle=Entry(ventana, width=20)
entry_calle.grid(column=1, row=2)

label_numero=Label(ventana, text="numero: ")
label_numero.grid(column=0, row=3)
entry_numero=Entry(ventana, width=20)
entry_numero.grid(column=1, row=3)

label_telefono=Label(ventana, text="telefono: ")
label_telefono.grid(column=0, row=4)
entry_telefono=Entry(ventana, width=20)
entry_telefono.grid(column=1, row=4)

label_localidad=Label(ventana, text="localidad: ")
label_localidad.grid(column=0, row=5)
entry_localidad=Entry(ventana, width=20)
entry_localidad.grid(column=1, row=5)


label_usuario=Label(ventana, text="nombre usuario: ")
label_usuario.grid(column=0, row=10)
entry_usuario=Entry(ventana, width=20)
entry_usuario.grid(column=1, row=10)

label_pass=Label(ventana, text="password: ")
label_pass.grid(column=0, row=11)
entry_pass=Entry(ventana, width=20)
entry_pass.grid(column=1, row=11)


if __name__=="__main__":

    ventana.mainloop()
    base.close()


