#no encontré en ningún lado una función que determine la cantidad de dígitos no decimales
nombre=input("nombre: ")
precio=float(input("precio: "))
cantidad=int(input("cantidad: "))

if(precio<10):
    t=("00000")
elif(precio<100):
    t=("0000")
elif(precio<1000):
    t=("000")
elif(precio<10000):
    t=("00")
elif(precio<100000):
    t=("0")
else:
    t=("")

if(cantidad<10):
    c=("00")
elif(cantidad<100):
    c=("0")
else:
    c=("")

costo=float(precio*cantidad)

if(costo<10):
    a=("0000000")
elif(costo<100):
    a=("000000")
elif(costo<1000):
    a=("00000")
elif(costo<10000):
    a=("0000")
elif(costo<100000):
    a=("000")
elif(costo<100000):
    a=("00")
elif(costo<100000):
    a=("0")
else:
    a=("")
    
print("nombre: ",nombre, "\n precio: ", t, round(precio, 2), "\n cantidad: ",c, cantidad,"\n costo: ", a, round(costo, 2))
