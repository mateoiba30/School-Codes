import random
n=int(random.randrange(20))
n=15
vidas=4
a=0
a=int(input("tienes 4 vidas, adivina el número entre 1 y 20: "))
while a!=n and vidas>0:
    vidas=vidas-1
    if a<n and vidas>0:
        a=int(input("el número es más grande, vuelve a intentar: "))
    elif a>n and vidas>0:a=int(input("el número es menor, vuelve a intentar: "))
    
if vidas>0:
    print("¡ADIVINASTE!")
else: print("PERDEDOR, el numero era: ", n)
