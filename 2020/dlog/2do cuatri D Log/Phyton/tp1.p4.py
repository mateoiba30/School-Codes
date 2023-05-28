p=0
contador=0
p=input("ingrese una palabra: ")

for letra in p:
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        contador=contador+1
print ("en la palabra hay", contador, " vocales")
