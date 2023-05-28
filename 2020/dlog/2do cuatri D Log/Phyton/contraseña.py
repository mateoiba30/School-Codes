import string #equivale a los include 

def cantNros(texto): #recibe como parametro un string...
    cant=0
    for letra in texto: #recorro cada letra individual...
        if letra.isdigit(): #es un metodo que permite determinar si el caracter es un numero o no...
            cant+=1 #cuento cuantos numeros hay...
    return cant

def cantMay(texto):
    cant=0
    for letra in texto:
        if letra.isupper():
            cant+=1
    return cant


#definimos la funcion main --->( int main() )
if __name__=="__main__":
    
    valor=input("Define una contraseña: ")#en la variable valor se define un texto...
    if len(valor)<6: #len es la funcion que indica cuantos caracteres tiene la cadena...
        print("La constraseña debe tener al menos 6 caracteres!")
    elif cantNros(valor)==0:
        print("La contrasela debe tener al menos un numero!")
    elif cantMay(valor)==0:
        print("La contraseña debe tener al menos una mayuscula!")
    else:
        print("perfection")

