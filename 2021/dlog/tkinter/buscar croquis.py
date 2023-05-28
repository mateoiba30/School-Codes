from Tkinter import *
import sqlite3
base=sqlite3.connect("baseparabuscar.db")
registro=base.cursor()
ventana=Tk()

label_id=Label(ventana, text="id ")
label_id.grid(column=0, row=1)
entry_id=Entry(ventana, width=20)
entry_id.grid(column=1, row=1)

label_nombre=Label(ventana, text="nombre ")
label_nombre.grid(column=0, row=2)
entry_nombre=Entry(ventana, width=20)
entry_nombre.grid(column=1, row=2)

label_apellido=Label(ventana, text="apellido ")
label_apellido.grid(column=0, row=3)
entry_apellido=Entry(ventana, width=20)
entry_apellido.grid(column=1, row=3)

label_usuario=Label(ventana, text="usuario ")
label_usuario.grid(column=0, row=4)
entry_usuario=Entry(ventana, width=20)
entry_usuario.grid(column=1, row=4)

label_clave=Label(ventana, text="clave ")
label_clave.grid(column=0, row=5)
entry_clave=Entry(ventana, width=20)
entry_clave.grid(column=1, row=5)

label_puntaje=Label(ventana, text="puntaje ")
label_puntaje.grid(column=0, row=6)
entry_puntaje=Entry(ventana, width=20)
entry_puntaje.grid(column=1, row=6)
