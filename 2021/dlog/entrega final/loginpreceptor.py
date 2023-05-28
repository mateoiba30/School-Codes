#LIBRERIAS
from Tkinter import *
import tkMessageBox as MSGbox
import ttk
import sqlite3

#CONECTAR A LA BD
base=sqlite3.connect("formulario.db3")
ventana=Tk()
registro=base.cursor()

#USUARIO
Lusuario=Label(ventana, text="Ingrese usuario")
Lusuario.grid(column=0, row=0)
Eusuario=Entry(ventana, width=20)
Eusuario.grid(column=1,  row=0)

#PASSWORD
Lpassword=Label(ventana, text="Ingrese password")
Lpassword.grid(column=0, row=1)
Epassword=Entry(ventana, width=20, show="*")
Epassword.grid(column=1, row=1)


#FUNCIONES
def validar():
    #funiones dentro de validar
    def limpiar2():#ventana 2
        t3=StringVar()
        t3.set("")
        Efecha.configure(text=t3)

        t4=StringVar()
        t4.set("")
        Ehora.configure(text=t4)
        
        t5=StringVar()
        t5.set("")
        Ealumno.configure(text=t5)
        
    def limpiar():#ventana login
        t1=StringVar()
        t1.set("")
        Eusuario.configure(text=t1)

        t2=StringVar()
        t2.set("")
        Epassword.configure(text=t2)

    #validar
    Usuario=Eusuario.get()
    Password=Epassword.get()
    registro.execute("Select * from Usuarios where (nombreusuario='%s' and password='%s' and tipousuario='3')" % (Usuario, Password))
    encontro=False
    for fila in registro:
        encontro=True
    if encontro:
        if encontro==True:
            #si es valido abro la nueva ventana y destruyola vieja
            ventana.destroy()
            ventana2=Tk()

            #fecha
            Lfecha=Label(ventana2, text="Fecha (dia/mes): ")
            Lfecha.grid(column=0, row=0)
            Efecha=Entry(ventana2, width=20)
            Efecha.grid(column=1,  row=0)

            #hora
            Lhora=Label(ventana2, text="Hora (hs:min): ")
            Lhora.grid(column=0, row=1)
            Ehora=Entry(ventana2, width=20)
            Ehora.grid(column=1, row=1)

            #id alumno
            Lalumno=Label(ventana2, text="Id del alumno: ")
            Lalumno.grid(column=0, row=2)
            Ealumno=Entry(ventana2, width=20)
            Ealumno.grid(column=1, row=2)

            #otra funcion     
            def update():
                Fecha=Efecha.get()
                Hora=Ehora.get()
                Usuario=Ealumno.get()
                registro.execute("INSERT INTO asistencia (alumno, fecha, hora) values ('%s','%s','%s')" %(Usuario, Fecha, Hora))
                base.commit()

            #botones
            Bagregar=Button(ventana2, text="Agregar", command=update)
            Bagregar.grid(column=1, row=3)
            
            Blimpiar=Button(ventana2, text="Limpiar", command=limpiar2)
            Blimpiar.grid(column=1, row=4)

            #cierre
            ventana2.mainloop()
    else:
         MSGbox.showerror(message="datos no validos")
         limpiar()

#BOTON
Blogin=Button(ventana, text="Login", command=validar)
Blogin.grid(column=1, row=2)

#CIERRE
ventana.mainloop()
base.close()
