from tkinter import *

vent = Tk() #el objeto ventana se llama vent 

vent.title("hola querid@s")

lbl = Label(vent, text="Hola Chiquis!!!!",  font=("Arial Bold", 24), bg="burlywood", fg="purple1")

lbl.grid(column=0, row=0)

vent.mainloop()