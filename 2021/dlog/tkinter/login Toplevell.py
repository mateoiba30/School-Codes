from tkinter import *
import sqlite3
base=sqlite3.connect("baseparabuscar.db")
registro=base.cursor()

v1=Tk()

label1=Label(v1, text="Ingrese usuario: ")
label1.grid(column=0, row=0)

entry1=Entry(v1, width=20)
entry1.grid(column=1, row=0)

label2=Label(v1, text="Ingrese password: ")
label2.grid(column=0, row=1)

entry2=Entry(v1, width=20)
entry2.grid(column=1, row=1)

def validar():
    usuario=entry1.get()
    clave=entry2.get()
    registro.execute("Select * from Usuarios WHERE(usuario='%s'and clave='%s')"%(usuario, clave))    
    encontro=False
    for fila in registro:
        encontro=True
        v2=Tk()
        

if __name__=="__main__":

    btnLogin=Button(v1, text="Login", command=validar)
    btnLogin.grid(column=1, row=2)
    v1.mainloop()
