#no estoy 100% seguro si es esto lo que hay que hacer, entendí que el interés es el porcentaje de incremento de la inversion por año
inversion=int(input("Ingrese su cantidad a invertir: "))
interes=int(input("Ingrese el porcentaje de interés anual: "))
anios=int(input("Ingrese el número de años: "))
ganancia=int(0)
dinerototal=int(0)

interes=(interes+100)/100

for i in range(0, anios):
    inversion=inversion*interes

dinerototal=inversion

print("El dinero total es de: ", dinerototal)


