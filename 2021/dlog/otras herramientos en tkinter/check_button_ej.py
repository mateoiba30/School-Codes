#si hay solo una opcion es mejor usar un botón de selección. Son parecidos

from Tkinter import *

def selec():
    cadena = ""
    
    if (leche.get()):
        cadena += "Café con leche"
    else:
        cadena += "Café sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text=cadena)
    
root = Tk()
root.title("Cafetería")
root.config(bd=0)#el color de fondo

leche = IntVar()      # 1 si, 0 no
azucar = IntVar()    # 1 si, 0 no

imagen = PhotoImage(file="gif_cafe.gif")#insertamos imagen en la ventana
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")#frame es una sección de la ventana

Label(frame,text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=selec).pack(anchor="w")
Checkbutton(frame, text="Con azúcar",variable=azucar, onvalue=1, offvalue=0, command=selec).pack(anchor="w")

monitor=Label(frame)
monitor.pack()

root.mainloop()
