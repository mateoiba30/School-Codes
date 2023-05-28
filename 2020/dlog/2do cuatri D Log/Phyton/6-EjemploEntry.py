from tkinter import *

mivent = Tk() #mivent se llama la ventana ppal
mivent.title("ejemplo")
mivent.geometry('300x300')

lbl = Label(mivent, text="Ingresa Nombre: ", fg="red")
lbl.grid(column=0, row=0)

lbl2 = Label(mivent, text="")
lbl2.grid(column=0, row=1)

txtNombre = Entry(mivent,width=25)
txtNombre.grid(column=1, row=0)

def clicked():
    res = "Hola  " + txtNombre.get()
    lbl2.configure(text= res)

btn = Button(mivent, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

mivent.mainloop()
