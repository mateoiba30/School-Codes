import math
from tkinter import *

ventana= Tk()
ventana.title("tkinter-2")
ventana.geometry('500x300')

etiqueta= Label(ventana, text="Ingrese a: ")
etiqueta.grid(column=1, row=1)

etiqueta2= Label(ventana, text="Ingrese b: ")
etiqueta2.grid(column=1, row=2)

etiqueta3= Label(ventana, text="Ingrese c: ")
etiqueta3.grid(column=1, row=3)

etiqueta4= Label(ventana, text="resultado1: ")
etiqueta4.grid(column=1, row=4)

etiqueta5= Label(ventana, text="resultado2: ")
etiqueta5.grid(column=1, row=5)

texto = Entry(ventana,width=25)
texto.grid(column=2, row=1)

texto2 = Entry(ventana,width=25)
texto2.grid(column=2, row=2)

texto3 = Entry(ventana,width=25)
texto3.grid(column=2, row=3)

def click():
    a=float(texto.get())
    b=float(texto2.get())
    c=float(texto3.get())
    x =(b**2)-(4*a*c)
    
    if x < 0:
        x1=print("Solucion solo en numeros complejos")
        x2=print("se requieren numero imaginarios")
    elif x==0:
        x1 = (-b) / (2*a)
        print("%.5f" % x1)
        x2 = (-b) / (2*a)
        print("%.5f" % x2)
    else:
        x1 = ((-b) + math.sqrt(x)) / (2*a)
        x2 = ((-b) - math.sqrt(x)) / (2*a)
            
    etiqueta4.configure(text="resultado1: "+ str(x1))
    etiqueta5.configure(text="resultado2: "+ str(x2))

texto.focus()
boton= Button(ventana, text=">click<", command=click)
boton.grid(column=1, row=6)

ventana.mainloop()


    
