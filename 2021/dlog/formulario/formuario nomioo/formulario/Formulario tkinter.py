from Tkinter import *
import tkMessageBox as MSGbox
import ttk
import sqlite3
base=sqlite3.connect("Formulario.db3")
root=Tk()
RadioBTN = IntVar()
RadioBTN2 = IntVar()

label_Nombre=Label(root, text="Nombre")
label_Nombre.grid(column=0, row=0)
entry_Nombre=Entry(root, width=20)
entry_Nombre.grid(column=1, row=0)

label_Apellido=Label(root, text="Apellido")
label_Apellido.grid(column=0, row=1)
entry_Apellido=Entry(root, width=20)
entry_Apellido.grid(column=1, row=1)

label_Calle=Label(root, text="Calle")
label_Calle.grid(column=0, row=2)
entry_Calle=Entry(root, width=20)
entry_Calle.grid(column=1, row=2)

label_NRO=Label(root, text="NRO de su Calle")
label_NRO.grid(column=0, row=3)
entry_NRO=Entry(root, width=20)
entry_NRO.grid(column=1, row=3)

label_Telefono=Label(root, text="Telefono")
label_Telefono.grid(column=0, row=4)
entry_Telefono=Entry(root, width=20)
entry_Telefono.grid(column=1, row=4)

LabelBTN2=Label(root, text="Ingrese su tipo de usuario")
LabelBTN2.grid(column=0, row=5)

profesor=Radiobutton(root, text="Profesor", variable=RadioBTN2, value=1)
profesor.grid(column=1, row=5)

preceptor=Radiobutton(root, text="Preceptor", variable=RadioBTN2, value=2)
preceptor.grid(column=2, row=5)

alumno=Radiobutton(root, text="Alumno", variable=RadioBTN2, value=3)
alumno.grid(column=3, row=5)

label_Localidad=Label(root, text="Localidad")
label_Localidad.grid(column=0, row=6)
comboLocalidad=ttk.Combobox(root, width=20)
comboLocalidad=ttk.Combobox(values=["San Carlos de Bariloche",
                                    "Norquinco",
                                    "Rio Colorado",
                                    "San Martin",
                                    "Viedma",
                                    "Choele Choel",
                                    "General Conesa",
                                    "El Cuy",
                                    "General Roca",
                                    "Sierra Colorada",
                                    "Pilcaniyeu",
                                    "San Antonio Oeste",
                                    "Valcheta",
                                    "Maquinchao"])
comboLocalidad.grid(column=1, row=6)

LabelBTN=Label(root, text="seleccione su estado civil")
LabelBTN.grid(column=0, row=7)

soltero=Radiobutton(root, text="Soltero", variable=RadioBTN, value=1)
soltero.grid(column=1, row=7)

casado=Radiobutton(root, text="Casado/ En pareja", variable=RadioBTN, value=2)
casado.grid(column=2, row=7)

nodecirlo=Radiobutton(root, text="Prefiero no decirlo", variable=RadioBTN, value=3)
nodecirlo.grid(column=3, row=7)

divorciado=Radiobutton(root, text="Divorciado", variable=RadioBTN, value=4)
divorciado.grid(column=4, row=7)

Label_Usuario=Label(root, text="Ingrese usuario")
Label_Usuario.grid(column=0, row=8)
entry_Usuario=Entry(root, width=20)
entry_Usuario.grid(column=1,  row=8)

label_Password=Label(root, text="Ingrese password")
label_Password.grid(column=0, row=9)
entry_Password=Entry(root, width=20, show="*")
entry_Password.grid(column=1, row=9)


def validar():
    validacion=True
    if entry_Nombre.get()=="":
        validacion=False
    if entry_Apellido.get()=="":
        validacion=False
    if entry_Telefono.get()=="":
        validacion=False
    if comboLocalidad.get()=="":
        validacion=False
    if RadioBTN.get()=="":
        validacion=False
    if entry_Usuario.get()=="":
        validacion=False
    if entry_Password.get()=="":
        validacion=False
    return validacion

def validar2():
    verificacion=True
    CONTRA=entry_Password.get()
    largoCON=len(CONTRA)
    y=CONTRA.isalnum()
    if y== False:
        MSGbox.showerror(message="La contraseña puede contener solo letras y números")
        verificacion=False
    if largoCON <8:
        MSGbox.showerror(message="La contraseña tiene que tener más de 8 caracteres")
        verificacion=False
    if largoCON > 50: 
        MSGbox.showerror(message="La contraseña no puede contener mas de 50 caracteres")
        verificacion=False
    return verificacion
                

def agregar():
    base=sqlite3.connect("Formulario.db3")
    datos=base.cursor()
    Nombre=entry_Nombre.get()
    Apellido=entry_Apellido.get()
    Calle=entry_Calle.get()
    NRO=entry_NRO.get()
    Telefono=entry_Telefono.get()
    Tipo_Usuario=RadioBTN2.get()
    Localidad=comboLocalidad.get()
    Estado_civil=RadioBTN.get()
    Usuario=entry_Usuario.get()
    Password=entry_Password.get()
    if validar()==True and validar2()==True:
        datos.execute("INSERT INTO Registro (Nombre, Apellido, Calle, Nro_calle, Telefono, Tipo_Usuarios, Localidad, Estado_civil, Nombre_Usuario, Password) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(Nombre, Apellido, Calle, NRO, Telefono, Tipo_Usuario, Localidad, Estado_civil, Usuario, Password))
        print("bienvenido")
        base.commit() 
    elif validar()==False:
        MSGbox.showerror(message="Todos los campos deben ser completados")
          
ButtonAgregar=Button(root, text="Agregar", command=agregar)
ButtonAgregar.grid(column=4, row=9)

root.mainloop()

base.close()

