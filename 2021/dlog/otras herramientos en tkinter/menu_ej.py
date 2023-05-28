from Tkinter import *

root = Tk()
##se suele llamar menumbrar
menubar = Menu(root)
root.config(menu=menubar)  # Lo asignamos a la base


##añadimos un submenú
filemenu = Menu(menubar)
##añadimos comandos de ejemplo
filemenu = Menu(menubar, tearoff=0)#le sacamos los elementos por defecto
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
##separador y comando quit
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)


##otro submenú
editmenu = Menu(menubar)
##más opciones de ejemplo
editmenu = Menu(menubar, tearoff=0)#le sacamos los elementos por defecto
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")


##otro submenú
helpmenu = Menu(menubar)
helpmenu = Menu(menubar, tearoff=0) #le sacamos los elementos por defecto
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

##los añadimos a la barra del menú
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)









helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

##finalmente bucle de la aplicación
root.mainloop()
