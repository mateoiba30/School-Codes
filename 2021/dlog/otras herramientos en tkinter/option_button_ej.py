#botones radiales, para elegir entre opciones

from Tkinter import *

def selec():
    monitor.config(text = "Opción {}".format(opcion.get() ) )#para qué es esto?
def reset():#para resetear
    opcion.set(None)          # Reiniciamos el seleccionable
    monitor.config(text='')   # Reiniciamos la etiqueta

root = Tk()
root.config(bd=15)#color

opcion = IntVar() # Como StrinVar pero en entero

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=selec).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=selec).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=selec).pack()

Button(root, text="Reiniciar", command=reset).pack()

monitor = Label(root)
monitor.pack()

root.mainloop()
