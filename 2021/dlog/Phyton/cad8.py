p=float(input("Ingrese el precio del producto: "))
pesos=int(round(p))
centavos=float(p-pesos)

print("euros: ", pesos)
print("céntimos: ", round(centavos, 2))
