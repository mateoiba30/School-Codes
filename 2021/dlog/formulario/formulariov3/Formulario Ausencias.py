from Tkinter import *
import tkMessageBox as MSGbox
import ttk
import sqlite3
base=sqlite3.connect("Formulario.db3")
root=Tk()

Label1=Label(root, text="Ingrese usuario")
Label1.grid(column=0, row=0)
entry1=Entry(root, width=20)
entry1.grid(column=1,  row=0)
label2=Label(root, text="Ingrese password")
label2.grid(column=0, row=1)
entry2=Entry(root, width=20, show="*")
entry2.grid(column=1, row=1)



def validar():
    base=sqlite3.connect("Formulario.db3")
    datos=base.cursor()
    Nombre_Usuario=entry1.get()
    Password=entry2.get()
    datos.execute("Select * from Registro where (Nombre_Usuario='%s' and Password='%s' and Tipo_Usuarios='2')" % (Nombre_Usuario, Password))
    encontro=False
    for fila in datos:
        encontro=True
    if encontro:
        if encontro==True:
            root2=Tk()
            Label_Fecha=Label(root2, text="Ingrese la fecha")
            Label_Fecha.grid(column=0, row=0)
            entry_Fecha=Entry(root2, width=20)
            entry_Fecha.grid(column=1,  row=0)
            label_Hora=Label(root2, text="Ingrese la hora de llegada")
            label_Hora.grid(column=0, row=1)
            entry_Hora=Entry(root2, width=20)
            entry_Hora.grid(column=1, row=1)
            label_Usuario=Label(root2, text="Ingrese el ID del usuario")
            label_Usuario.grid(column=0, row=2)
            entry_Usuario=Entry(root2, width=20)
            entry_Usuario.grid(column=1, row=2)

            def agregar():
                base=sqlite3.connect("Formulario.db3")
                datos=base.cursor()
                Fecha=entry_Fecha.get()
                Hora=entry_Hora.get()
                Usuario=entry_Usuario.get()
                datos.execute("INSERT INTO Asistencia (ID_Usuario, Fecha, Hora) values ('%s','%s','%s')" %(Usuario, Fecha, Hora))
                base.commit()
            
            ButtonAgregar=Button(root2, text="Agregar", command=agregar)
            ButtonAgregar.grid(column=1, row=3)
    else:
         MSGbox.showerror(message="Usuario no valido")
    base.close()



ButtonLogin=Button(root, text="Login", command=validar)
ButtonLogin.grid(column=1, row=2)


root.mainloop()
