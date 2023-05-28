from tkinter import *
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

def insert():

    ELID=int(entry_id.get())
    NOMBRE=entry_nombre.get()
    APELLIDO=entry_apellido.get()
    USUARIO=entry_usuario.get()
    CLAVE=entry_clave.get()
    PUNTAJE=int(entry_puntaje.get())
    
    instruccion="INSERT INTO Usuarios('id', 'nombre', 'apellido', 'usuario', 'clave', 'puntaje') VALUES ('%d', '%s', '%s', '%s', '%s', '%d')" %(ELID, NOMBRE, APELLIDO, USUARIO, CLAVE, PUNTAJE)
    print(instruccion)
    registro.execute(instruccion)      
    base.commit()

def update():
    
    ID=int(entry_buscar.get())
    ELID=int(entry_id.get())
    NOMBRE=entry_nombre.get()
    APELLIDO=entry_apellido.get()
    USUARIO=entry_usuario.get()
    CLAVE=entry_clave.get()
    PUNTAJE=int(entry_puntaje.get())
    
    instruccion="UPDATE Usuarios SET 'id'='%d', 'nombre'='%s', 'apellido'='%s', 'usuario'='%s', 'clave'='%s', 'puntaje'='%d' WHERE(id='%d');" %(ELID, NOMBRE, APELLIDO, USUARIO, CLAVE, PUNTAJE, ID)
    registro.execute(instruccion)      
    base.commit()

def confirmar():
    ventana2=Tk()

    ID=entry_buscar.get()
    ID=int(ID)

    label_pregunta=Label(ventana2, text="Seguro que queres borrar el usuario %d?"%ID)
    label_pregunta.grid(column=0, row=0)
    
    boton_confirmar=Button(ventana2, text="CONFIRMAR", command=delete)
    boton_confirmar.grid(column=0, row=1)
    
    boton_negar=Button(ventana2, text="NEGAR", command=limpiar)
    boton_negar.grid(column=1, row=1)
    
def delete():

    ID=int(entry_buscar.get())
    registro.execute("DELETE from Usuarios WHERE(ID='%d')"%(ID))
    limpiar()
    base.commit()
    
def select():
    ID=int(entry_buscar.get())
    registro.execute("SELECT * from Usuarios WHERE(ID='%d')"%(ID))
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
    t0=StringVar()
    t0.set(" ")
    entry_buscar.configure(text=t0)
    
    t1=StringVar()
    t1.set(" ")
    entry_id.configure(text=t1)

    t2=StringVar()
    t2.set(" ")
    entry_nombre.configure(text=t2)

    t3=StringVar()
    t3.set(" ")
    entry_apellido.configure(text=t3)

    t4=StringVar()
    t4.set(" ")
    entry_usuario.configure(text=t4)

    t5=StringVar()
    t5.set(" ")
    entry_clave.configure(text=t5)

    t6=StringVar()
    t6.set(" ")
    entry_puntaje.configure(text=t6)
    
if __name__=="__main__":
    
    label_buscar=Label(ventana, text="ingrese el id a buscar: ")
    label_buscar.grid(column=0, row=0)
    entry_buscar=Entry(ventana, width=20)
    entry_buscar.grid(column=1, row=0)
    
    boton_limpiar=Button(ventana, text="LIMPIAR", command=limpiar)
    boton_limpiar.grid(column=2, row=0)
    
    boton_borrar=Button(ventana, text="BORRAR", command=confirmar)
    boton_borrar.grid(column=2, row=1)

    boton_buscar=Button(ventana, text="BUSCAR", command=select)
    boton_buscar.grid(column=2, row=2)

    boton_buscar=Button(ventana, text="MODIFICAR", command=update)
    boton_buscar.grid(column=2, row=3)

    boton_buscar=Button(ventana, text="AGREGAR", command=insert)
    boton_buscar.grid(column=2, row=4)
    
    ventana.mainloop()

    base.close()
