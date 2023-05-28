frase=input("Escriba una frase: ")
vocal=input("Ingrese una vocal en minúscula: ")
if(vocal=="a" or vocal=="e" or vocal=="i" or vocal=="o" or vocal=="u"):
    print(frase.replace(vocal, vocal.upper()))
else:
    print("Eso no es una vocal en minúscula!")
