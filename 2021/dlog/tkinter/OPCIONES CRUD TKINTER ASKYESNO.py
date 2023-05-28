from tkinter import *
from tkinter import messagebox
import sqlite3
base=sqlite3.connect("baseparabuscar.db")
registro=base.cursor()

####
v_login=Tk()
ventana=Tk()
ventana.withdraw()

####
label1=Label(v_login, text="Ingrese usuario: ")
label1.grid(column=0, row=0)
entry1=Entry(v_login, width=20)
entry1.grid(column=1, row=0)

label2=Label(v_login, text="Ingrese password: ")
label2.grid(column=0, row=1)
entry2=Entry(v_login, width=20)
entry2.grid(column=1, row=1)

####
label_buscar=Label(ventana, text="ingrese el id a buscar: ")
label_buscar.grid(column=0, row=0)
entry_buscar=Entry(ventana, width=20)
entry_buscar.grid(column=1, row=0)

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

####
def limpiarlogin():
    t00=StringVar()
    t00.set(" ")
    entry1.configure(text=t00)

    t01=StringVar()
    t01.set(" ")
    entry2.configure(text=t01)
    
def validar():
    usuario=entry1.get()
    clave=entry2.get()
    registro.execute("Select * from Usuarios WHERE(usuario='%s'and clave='%s')"%(usuario, clave))    
    encontro=False
    for fila in registro:
        encontro=True
        v_login.destroy()
        ventana.deiconify()

    limpiarlogin()      
        
def insert():
    registro=base.cursor()
    ELID=int(entry_id.get())
    NOMBRE=entry_nombre.get()
    APELLIDO=entry_apellido.get()
    USUARIO=entry_usuario.get()
    CLAVE=entry_clave.get()
    PUNTAJE=int(entry_puntaje.get())
    registro.execute("INSERT INTO Usuarios('id', 'nombre', 'apellido', 'usuario', 'clave', 'puntaje') VALUES ('%d', '%s', '%s', '%s', '%s', '%d')" %(ELID, NOMBRE, APELLIDO, USUARIO, CLAVE, PUNTAJE))      
    base.commit()

def update():
    registro=base.cursor()  
    ID=int(entry_buscar.get())
    ELID=int(entry_id.get())
    NOMBRE=entry_nombre.get()
    APELLIDO=entry_apellido.get()
    USUARIO=entry_usuario.get()
    CLAVE=entry_clave.get()
    PUNTAJE=int(entry_puntaje.get())

    registro.execute("UPDATE Usuarios SET 'id'='%d', 'nombre'='%s', 'apellido'='%s', 'usuario'='%s', 'clave'='%s', 'puntaje'='%d' WHERE(id='%d');" %(ELID, NOMBRE, APELLIDO, USUARIO, CLAVE, PUNTAJE, ID))      
    base.commit()

def confirmar():
    registro=base.cursor()
    ID=entry_buscar.get()
    ID=int(ID)
    
    resultado=messagebox.askyesno("borrar el usuario %d?"%(ID))
    if resultado==True:
        delete()
    else:
        limpiar()

def delete():
    registro=base.cursor()  
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

####
if __name__=="__main__":

    btnLogin=Button(v_login, text="Login", command=validar)
    btnLogin.grid(column=1, row=2)
    
    v_login.mainloop()

####
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

