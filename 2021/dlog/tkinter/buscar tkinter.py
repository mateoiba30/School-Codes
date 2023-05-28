from Tkinter import *
import sqlite3
base=sqlite3.connect("tabla1.db")
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


def select():
    ID=entry_buscar.get()
    ID=int(ID)
    registro.execute("SELECT * from Usuario WHERE(ID='%d')"%(ID))
    for fila in registro:

        texto1=StringVar()
        x=("%s")%(fila[0])
        x2=int(x)
        texto1.set(x2)
        entry_id.configure(text=texto1)

        texto2=StringVar()
        y=("%s")%(fila[1])
        texto2.set(y)
        entry_nombre.configure(text=texto2)

        texto3=StringVar()
        z=("%s")%(fila[2])
        texto3.set(z)
        entry_apellido.configure(text=texto3)

        texto4=StringVar()
        a=("%s")%(fila[3])
        texto4.set(a)
        entry_usuario.configure(text=texto4)

        texto5=StringVar()
        b=("%s")%(fila[4])
        texto5.set(b)
        entry_clave.configure(text=texto5)

        texto6=StringVar()
        c=("%s")%(fila[5])
        c2=int(c)
        texto6.set(c2)
        entry_puntaje.configure(text=texto6)

def limpiar():
    t1=StringVar()
    t1.set(" ")
    entry_id.configure(text=t1)

    t2=StringVar()
    t2.set(" ")
    entry_nombre.configure(text=t2)

    t3=StringVar()
    t3.set(" ")
    entry_nombre.configure(text=t3)

    t4=StringVar()
    t4.set(" ")
    entry_nombre.configure(text=t4)

    t5=StringVar()
    t5.set(" ")
    entry_nombre.configure(text=t5)

    t6=StringVar()
    t6.set(" ")
    entry_nombre.configure(text=t6)
    
if __name__=="__main__":
    limpiar()
    
    label_buscar=Label(ventana, text="ingrese el id a buscar: ")
    label_buscar.grid(column=0, row=0)
    entry_buscar=Entry(ventana, width=20)
    entry_buscar.grid(column=1, row=0)
    
    boton_buscar=Button(ventana, text="BUSCAR", command=select)
    boton_buscar.grid(column=2, row=0)

    ventana.mainloop()

    base.close()

