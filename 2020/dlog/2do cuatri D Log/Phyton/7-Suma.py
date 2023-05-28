from tkinter import *

window = Tk()
window.title("ejemplo")
window.geometry('350x200')

lbl = Label(window, text="Ingresa valor 1: ")
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Ingresa valor 2: ")
lbl2.grid(column=0, row=1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

txt2 = Entry(window,width=10)
txt2.grid(column=1, row=1)

lbl3=Label(window, text="Resultado: ")
lbl3.grid(column=0, row=3)

def clicked():
    nro1 = int(txt.get())
    nro2 = int(txt2.get())
    res=nro1+nro2
    lbl3.configure(text="el resultado es: " + str(res))

txt.focus()
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=4)

window.mainloop()
