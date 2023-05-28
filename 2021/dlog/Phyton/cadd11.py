nombre=input("nombre: ")
p=("000000")
precio=input("precio: ")
c=("000")
cantidad=input("cantidad: ")

x=int(11-len(p))
print(p[0:x:1]+precio)

y=int(8-len(p))
print(c[0:y:1]+cantidad)
