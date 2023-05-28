from Tkinter import *
import sqlite3
base=sqlite3.connect("formulario.db")
registro=base.cursor()
ventana=Tk()
opcion = IntVar()
value=0
frame = Frame(ventana)
valid=False
cadena=""

label_nombre=Label(ventana, text="nombre: ")
label_nombre.grid(column=0, row=0)
entry_nombre=Entry(ventana, width=20)
entry_nombre.grid(column=1, row=0)

label_apellido=Label(ventana, text="apellido: ")
label_apellido.grid(column=0, row=1)
entry_apellido=Entry(ventana, width=20)
entry_apellido.grid(column=1, row=1)

label_calle=Label(ventana, text="calle: ")
label_calle.grid(column=0, row=2)
entry_calle=Entry(ventana, width=20)
entry_calle.grid(column=1, row=2)

label_numero=Label(ventana, text="nro calle: ")
label_numero.grid(column=0, row=3)
entry_numero=Entry(ventana, width=20)
entry_numero.grid(column=1, row=3)

label_telefono=Label(ventana, text="telefono: ")
label_telefono.grid(column=0, row=4)
entry_telefono=Entry(ventana, width=20)
entry_telefono.grid(column=1, row=4)

label_localidad=Label(ventana, text="localidad: ")
label_localidad.grid(column=0, row=5)
entry_localidad=Entry(ventana, width=20)
entry_localidad.grid(column=1, row=5)

label_usuario=Label(ventana, text="nombre usuario: ")
label_usuario.grid(column=0, row=6)
entry_usuario=Entry(ventana, width=20)
entry_usuario.grid(column=1, row=6)

label_pass=Label(ventana, text="password: ")
label_pass.grid(column=0, row=7)
entry_pass=Entry(ventana, width=20)
entry_pass.grid(column=1, row=7)

Label(ventana, text="estado civil: ").grid(column=0, row=8)
Radiobutton(ventana, value=1, text="soltero").grid(column=0, row=9)
Radiobutton(ventana, value=2, text="casado/en pareja").grid(column=0, row=10)
Radiobutton(ventana, value=3, text="divorciado").grid(column=0, row=11)
Radiobutton(ventana, value=4, text="prefiero no decirlo").grid(column=0, row=12)

entry_error=Entry(ventana, width=30)
entry_error.grid(column=0, row=14)

    
def insert():
    registro=base.cursor()
    NOMBRE=entry_nombre.get() 
    APELLIDO=entry_apellido.get()
    CALLE=entry_calle.get()
    NUMERO=int(entry_numero.get())
    TELEFONO=int(entry_telefono.get())
    LOCALIDAD=entry_localidad.get()
    USUARIO=entry_usuario.get()
    registro.execute("INSERT INTO Usuarios('nombre', 'apellido', 'calle', 'numero', 'telefono', 'localidad', 'usuario') VALUES ('%s', '%s', '%s', '%d', '%d', '%s', '%s')" %(NOMBRE, APELLIDO, CALLE, NUMERO, TELEFONO, LOCALIDAD, USUARIO))      
    base.commit()

    cadena="datos agregados"
    

def validar():
    texto_nombre=entry_nombre.get()
    texto_apellido=entry_apellido.get()
    valor_telefono=entry_telefono.get()
    U=len(entry_usuario.get())

    cadena=""
    
    if texto_nombre!="":
        valid=True
    else:
        cadena+=" nombre vacío"
        valid=False
        
    if texto_apellido!="":
        valid=True
    else:
        cadena+=" apellido vacío"
        valid=False
        
    if valor_telefono!="":
        valid=True
    else:
        cadena+=" telefono vacío"
        valid=False
        
    if value!=0:
        valid=True
    else:
        cadena+=" estado civil no seleccionado"
        valid=False
        
    if U<9:
        valid=True
    else:
        cadena+=" usuario con más de 8 dígitos"
        valid=False
        
    if Checkbutton==1:
        valid=True
    else:
        cadena+=" no aceptas los términos"
        valid=False
        
    return valid
    

if __name__=="__main__":
    boton=Button(ventana, text="AGREGAR", command=validar)
    boton.grid(column=1, row=8)
    
    Label(ventana,text="acepto términos").grid(column=0, row=13)
    Checkbutton(ventana, onvalue=1, offvalue=0).grid(column=1, row=13)

    
    if validar():
        insert()

    texto=StringVar()
    texto.set(cadena)
    entry_nombre.configure(text=texto)  
    
    monitor=Label(frame)

    ventana.mainloop()
    base.close()

