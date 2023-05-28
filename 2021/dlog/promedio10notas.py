mat=input("Ingrese la materia: ")
nom=input("Ingrese el nombre: ")
s=0

for i in range(10):
    n=float(input("Ingrese la nota %d: "%(i+1)))
    s=s+n

p=s/10

if(s>=7):
    print(nom, " aprobó ", mat, ", y el promedio fue de ", p)
else:
    print(nom, " NO aprobó ", mat, ", y el promedio fue de ", p)
