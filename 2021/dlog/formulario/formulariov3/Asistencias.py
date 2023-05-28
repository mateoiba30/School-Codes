from Tkinter import *
import sqlite3
ventana=Tk()
ventana2=Tk()
base=sqlite3.connect("formulario.db")
registro=base.cursor()

opcion = IntVar()

Lnombre=Label(ventana, text= "nombre de usuario:").grid(column=0, row=0)
Enombre=Entry(ventana, width=20).grid(column=1, row=0)

Lpassword=Label(ventana, text= "password:").grid(column=0, row=1)
Epassword=Entry(ventana, width=20).grid(column=1, row=1)


def validar():
    def llegada():
        monitor=int(opcion.get())
    
    nombre=Enombre.get()
    password=Epassword.get()
    registro.execute("Select * from usuarios_asistencia where nombre='%s' and password='%s' and tipo_usuario=1" % (nombre, password))
    valid=False

    for fila in registro:
        valid=True
        
    if valid: 
        Lmensaje=Label(ventana, text="Preceptor validado").grid(column=1, row=3)       
        ventana2 = Toplevel()
        ventana2.geometry("300x200")
        Lfecha=Label(ventana2, text= "Fecha:").grid(column=0, row=2)
        Efecha=Entry(ventana2, width=20).grid(column=1, row=2)
        Lhora=Label(ventana2, text= "Hora:").grid(column=0, row=1)
        Ehora=Entry(ventana2, width=20).grid(column=1, row=1)
        Lid=Label(ventana2, text= "ID del alumno:").grid(column=0, row=0)
        Eid=Entry(ventana2, width=20).grid(column=1, row=0)
        monitor = Label(ventana2, text="llegada:")
        monitor.grid(column=0, row=4)          
        frame = Frame(ventana2).grid(column=0, row=5)

        llego=Radiobutton(ventana2, text="presente", variable=opcion, value=1, command=llegada).grid(column=0, row=6)
        no_llego=Radiobutton(ventana2, text="ausente", variable=opcion, value=2, command=llegada).grid(column=0, row=7)
        llego_tarde=Radiobutton(ventana2, text="tarde", variable=opcion, value=3, command=llegada).grid(column=0, row=8)

        def buscaralumno():
            id_alumno=int(Eid.get())

            registros.execute("select id from Usuarios where id='%d' and tipo_usuario=1" % (id_alumno))
            valido=False

            for fila in registro:
                valido=True

            if valido:
                def insert():
                    Iid=int(entryC.get())
                    Illegada=int(opcion.get())
                    Ifecha=Efehca.get()
                    registro.execute("INSERT INTO asistencia ('Id_usuario', 'Llegada','Fecha','Hora') VALUES ('%d', '%d', '%s', '%s')" % (Iid, Illegada, Ifecha, Ihora))
                    base.commit()
                Binsert=Button(ventana2, text="Agregar", command=insertar).grid(column=2, row=9)

            else:
                Lmensaje2=Label(ventana2, text= "tipo de usario no valido").grid(column=1, row=9)
        Bvalidar=Button(ventana2, text="validar", command=buscaralumno).grid(column=1, row=4)


Blogin=Button(ventana, text="loginn", command=validar).grid(column=1, row=2)

ventana2.mainloop()
ventana.mainloop()
base.close()

