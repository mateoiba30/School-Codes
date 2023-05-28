from Tkinter import *
import ttk
import tkMessageBox as MSGbox
import sqlite3
base=sqlite3.connect("formulario.db")
ventana=Tk()
registro=base.cursor()

Label1=Label(ventana, text="Ingrese usuario")
Label1.grid(column=0, row=0)
entry1=Entry(ventana, width=20)
entry1.grid(column=1,  row=0)

label2=Label(ventana, text="Ingrese password")
label2.grid(column=0, row=1)
entry2=Entry(ventana, width=20, show="*")
entry2.grid(column=1, row=1)

def validar():
    
    def limpiar2():
        t3=StringVar()
        t3.set("")
        entry_Fecha.configure(text=t3)

        t4=StringVar()
        t4.set("")
        entry_Hora.configure(text=t4)
        
        t5=StringVar()
        t5.set("")
        entry_Usuario.configure(text=t5)
        
    def limpiar():
        t1=StringVar()
        t1.set("")
        entry1.configure(text=t1)

        t2=StringVar()
        t2.set("")
        entry2.configure(text=t2)
        
    Nombre_Usuario=entry1.get()
    Password=entry2.get()
    registro.execute("Select * from Usuarios where (nombreusuario='%s' and password='%s' and tipousuario='3')" % (Nombre_Usuario, Password))
    encontro=False
    for fila in registro:
        encontro=True
    if encontro:
        if encontro==True:
            ventana2=Tk()
            Label_Fecha=Label(ventana2, text="Fecha (dia/mes): ")
            Label_Fecha.grid(column=0, row=0)
            entry_Fecha=Entry(ventana2, width=20)
            entry_Fecha.grid(column=1,  row=0)
            
            label_Hora=Label(ventana2, text="Hora (hs:min): ")
            label_Hora.grid(column=0, row=1)
            entry_Hora=Entry(ventana2, width=20)
            entry_Hora.grid(column=1, row=1)
            
            label_Usuario=Label(ventana2, text="Id del alumno: ")
            label_Usuario.grid(column=0, row=2)
            entry_Usuario=Entry(ventana2, width=20)
            entry_Usuario.grid(column=1, row=2)
                    
            def update():
                Fecha=entry_Fecha.get()
                Hora=entry_Hora.get()
                Usuario=entry_Usuario.get()
                registro.execute("INSERT INTO asistencia (alumno, fecha, hora) values ('%s','%s','%s')" %(Usuario, Fecha, Hora))
                base.commit()
            
            ButtonAgregar=Button(ventana2, text="Agregar", command=update)
            ButtonAgregar.grid(column=1, row=3)

            ventana2.mainloop()
    else:
         MSGbox.showerror(message="datos no validos")
         limpiar()

    limpiar2()

Blogin=Button(ventana, text="Login", command=validar)
Blogin.grid(column=1, row=2)


ventana.mainloop()
base.close()
