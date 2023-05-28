ahorros=int(input("Ingrese su cantidad de ahorros a invertir: "))
ganancia=int(0)
dinerototal=int(0)

for i in range(1, 4):
    ahorros=ahorros*1.04
    print("A fin del año ",i," los ahorros son de: $", round(ahorros, 2))

