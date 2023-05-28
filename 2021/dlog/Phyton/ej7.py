peso=float(input("Ingrese su peso en kg: "))
estatura=float(input("Ingrese su estatura en metros: "))
imc=float(0)
imc=peso/(estatura)**2


print("Tu índice de masa corporal es de: ")
print(round(imc, 2))
