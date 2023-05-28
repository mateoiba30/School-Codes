n=int(67)
a=0
A=0
a=input("adivina el número: ")
A=int(a)
while A!=n:
    if A<n:
        A=int(input("el número es más grande, vuelve a intentar: "))
    else:A=int(input("el número es menor, vuelve a intentar: "))
print("¡ADIVINASTE!")
