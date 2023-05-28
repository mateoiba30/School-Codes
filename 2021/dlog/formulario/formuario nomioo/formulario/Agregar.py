from Tkinter import *
import sqlite3
base=sqlite3.connect("Formulario.db3")
root=Tk()

label_Nombre=Label(root, text="Nombre")
label_Nombre.grid(column=0, row=0)
entry_Nombre=Entry(root, width=12)
entry_Nombre.grid(column=1, row=0)

label_Apellido=Label(root, text="Apellido")
label_Apellido.grid(column=0, row=1)
entry_Apellido=Entry(root, width=12)
entry_Apellido.grid(column=1, row=1)

label_Calle=Label(root, text="Calle")
label_Calle.grid(column=0, row=2)
entry_Calle=Entry(root, width=12)
entry_Calle.grid(column=1, row=2)

label_NRO=Label(root, text="NRO de su Calle")
label_NRO.grid(column=0, row=3)
entry_NRO=Entry(root, width=12)
entry_NRO.grid(column=1, row=3)

label_Telefono=Label(root, text="Telefono")
label_Telefono.grid(column=0, row=4)
entry_Telefono=Entry(root, width=20)
entry_Telefono.grid(column=1, row=4)

label_Localidad=Label(root, text="Localidad")
label_Localidad.grid(column=0, row=5)
entry_Localidad=Entry(root, width=12)
entry_Localidad.grid(column=1, row=5)


label_ecivil=Label(root, text="Estado Civil")
label_ecivil.grid(column=0, row=6)
entry_ecivil=Entry(root, width=12)
entry_ecivil.grid(column=1, row=6)

Label_Usuario=Label(root, text="Ingrese usuario")
Label_Usuario.grid(column=0, row=7)
entry_Usuario=Entry(root, width=12)
entry_Usuario.grid(column=1,  row=7)

label_Password=Label(root, text="Ingrese password")
label_Password.grid(column=0, row=8)
entry_Password=Entry(root, width=12, show="*")
entry_Password.grid(column=1, row=8)

def agregar():
    base=sqlite3.connect("Formulario.db3")
    datos=base.cursor()
    Nombre=entry_Nombre.get()
    Apellido=entry_Apellido.get()
    Calle=entry_Calle.get()
    NRO=entry_NRO.get()
    Telefono=entry_Telefono.get()
    Localidad=entry_Localidad.get()
    Estado_Civil=entry_ecivil.get()
    Usuario=entry_Usuario.get()
    Password=entry_Password.get()
    datos.execute("INSERT INTO Registro (Nombre, Apellido, Calle, Nro_calle, Telefono, Localidad, Estado_Civil, Nombre_Usuario, Password) values ('%s','%s','%s','%s','%s', '%s','%s','%s','%s')" %(Nombre, Apellido, Calle, NRO, Telefono, Localidad, Estado_Civil, Usuario, Password))
    print("Se agrego correctamente")
    base.commit()

ButtonAgregar=Button(root, text="Agregar", command=agregar)
ButtonAgregar.grid(column=4, row=8)

root.mainloop()

base.close()
