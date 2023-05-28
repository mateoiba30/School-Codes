from Tkinter import *
import sqlite3
#la idea no es usar prints

root=Tk()
#le doy atributos de ventana
label1=Label(root, text="Ingrese usuario: ")
label1.grid(column=0, row=0)

entry1=Entry(root, width=20)
entry1.grid(column=1, row=0)
#entry1.pack(), otra forma de lo del renglon de arriba

label2=Label(root, text="Ingrese password: ")
label2.grid(column=0, row=1)

entry2=Entry(root, width=20)
entry2.grid(column=1, row=1)

def validar():
    base=sqlite3.connect("basequinto.db")
    registros=base.cursor()
    Usuario=entry1.get()
    Password=entry2.get()
    txtSQL="Select * from Alumnos WHERE(Usuario='%s'and Password='%s')"%(Usuario, Password)
    print(txtSQL)
    registros.execute(txtSQL)    
    encontro=False
    
    for fila in registros:
        encontro=True
    if encontro:
        print("Bienvenido")
        print("La base de datos se abrio correctamente")
        print(" ")
        print("ID |   USUARIO |  PASSWORD ")
        print("")
        registros.execute("SELECT * from Alumnos WHERE(Usuario='%s')"%(Usuario))
        for fila in registros:
            print("%d,   %s,   %s"%(fila[0], fila[1], fila[2]))
        print("")
        
    else:
        print("El usuario no es valido")

    base.close()


btnLogin=Button(root, text="Login", command=validar)
btnLogin.grid(column=1, row=2)

root.mainloop()

