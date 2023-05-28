cociente=int(0)
resto=int(0)
n=int(input("Ingrese el dividendo: "))
m=int(input("Ingrese el divisor: "))

cociente=n/m
resto=cociente-(round (cociente))

print(n, "entre ", m, " da un cociente de ", round(cociente), "y un resto de ", round(resto, 3))
