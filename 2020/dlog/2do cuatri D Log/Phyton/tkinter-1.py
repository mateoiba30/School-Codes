from tkinter import *

ventana = Tk()
ventana.title("tkinter-1")
ventana.geometry('350x200')

etiqueta = Label(ventana, text="Ingresa su peso en kilogramos: ")
etiqueta.grid(column=0, row=0)

etiqueta2 = Label(ventana, text="Ingresa su altura en metros: ")
etiqueta2.grid(column=0, row=1)

texto = Entry(ventana,width=25)
texto.grid(column=1, row=0)

texto2 = Entry(ventana,width=25)
texto2.grid(column=1, row=1)

etiqueta3=Label(ventana, text="IMC: ")
etiqueta3.grid(column=0, row=3)

def clicked():
    n1 = float(texto.get())
    n2 = float(texto2.get())
    res=n1/(n2*n2)
    etiqueta3.configure(text="IMC: " + str(res))

texto.focus()
boton = Button(ventana, text=">click<", command=clicked)
boton.grid(column=0, row=4)

ventana.mainloop()
