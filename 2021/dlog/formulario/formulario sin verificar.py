from tkinter import *
import sqlite3
base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()
ventana2=Tk()
ventana3=Tk()
opcion = IntVar()

frame = Frame(ventana3)
frame.pack(side="left")

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

Label(ventana2, text="estado civil: ").pack(anchor="w")
Radiobutton(ventana2, variable=opcion , value=1, text="soltero").pack(anchor="w")
Radiobutton(ventana2, variable=opcion, value=2, text="casado/en pareja").pack(anchor="w")
Radiobutton(ventana2, variable=opcion, value=3, text="divorciado").pack(anchor="w")
Radiobutton(ventana2, variable=opcion, value=4, text="prefiero no decirlo").pack(anchor="w")



label_usuario=Label(ventana, text="nombre usuario: ")
label_usuario.grid(column=0, row=10)
entry_usuario=Entry(ventana, width=20)
entry_usuario.grid(column=1, row=10)

label_pass=Label(ventana, text="password: ")
label_pass.grid(column=0, row=11)
entry_pass=Entry(ventana, width=20)
entry_pass.grid(column=1, row=11)

def selec():
    monitor.config(text = "Opción {}".format(opcion.get() ) )

def acepto():
    acept=True

if __name__=="__main__":
    Label(ventana3,text="acepto términos").pack(anchor="w")
    Checkbutton(frame, command=acepto).pack(anchor="w")

    monitor=Label(frame)
    monitor.pack()
    
    ventana.mainloop()
    base.close()

