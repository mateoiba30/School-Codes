from tkinter import *

vent = Tk()

def funcion():
    lbl.configure(text="Aguante River!!", bg="Red", fg="white")

vent.title("Hola querid@s")

lbl = Label(vent, text="Holis",  font=("Arial Bold", 25), bg="yellow", fg="purple1")
lbl.grid(column=0, row=0)

btn = Button(vent, text="Hacer click aqui", command=funcion)
btn.grid(column=0, row=1)

vent.mainloop()
