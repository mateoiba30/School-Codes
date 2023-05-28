from tkinter import * #declaro librerías
from tkinter import messagebox
import sqlite3
base=sqlite3.connect("baseparabuscar.db")#conecto a la base
registro=base.cursor()

login=Tk()
ventana=Toplevel()#ventana dependiente/hija

#lo que va en la primer ventana
label1=Label(login, text="usuario: ")
label1.grid(column=0, row=0)
entry1=Entry(login, width=20)
entry1.grid(column=1, row=0)

label2=Label(login, text="clave: ")
label2.grid(column=0, row=1)
entry2=Entry(login, width=20)
entry2.grid(column=1, row=1)

entry3=Entry(login, width=25)
entry3.grid(column=1, row=3)

#lo que va en la segunda ventana
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

#funciones
def limpiarlogin():
    t00=StringVar()
    t00.set(" ")
    entry1.configure(text=t00)

    t01=StringVar()
    t01.set(" ")
    entry2.configure(text=t01)
    
def mostrar():
    usuario=entry1.get()
    clave=entry2.get()
    registro.execute("Select * from Usuarios WHERE(usuario='%s'and clave='%s')"%(usuario, clave))    
    encontro=False
    
    for fila in registro:#si el usuario y clave coinciden
        encontro=True
    if encontro:
        ventana.deiconify()#se abre la ventna hija y se cierra el login
        login.withdraw()
#si fue correcta ya está cerrada la ventana login
    else:
        t03=StringVar()
        t03.set("usuario o clave incorrecto")#se muestra que la clave es incorrecta
        entry3.configure(text=t03)
    
        limpiarlogin()#limpiamos lo introducido
        
def insert():
    ELID=int(entry_id.get())
    NOMBRE=entry_nombre.get()
    APELLIDO=entry_apellido.get()
    USUARIO=entry_usuario.get()
    CLAVE=entry_clave.get()
    PUNTAJE=int(entry_puntaje.get())
    
    instruccion="INSERT INTO Usuarios('id', 'nombre', 'apellido', 'usuario', 'clave', 'puntaje') VALUES ('%d', '%s', '%s', '%s', '%s', '%d')" %(ELID, NOMBRE, APELLIDO, USUARIO, CLAVE, PUNTAJE)
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
    ID=int(entry_buscar.get())
    resultado=messagebox.askyesno("borrar el usuario %d?"%(ID))
    if resultado==True:
        delete()
    else:
        limpiar()
        
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

    ventana.withdraw()#cuando inicia el programa cerramos la ventana hija y solo si está bien el login esta se abre

    boton_login=Button(login, text="LOGIN", command=mostrar)#botón de la ventana madre
    boton_login.grid(column=0, row=3)

#botones de la ventana hija    
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
