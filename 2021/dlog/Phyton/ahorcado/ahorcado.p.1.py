import random
AHORCADO=['''

	

  ------
  |    0
  |   
 /_\      ''', '''

  ------
  |    0
  |    I
 /_\      ''', '''

  ------
  |    0
  |    I
 /_\  /   ''', '''

  ------
  |    0
  |    I
 /_\  / \ ''', '''

  ------
  |    0
  |   /I
 /_\  / \ ''', '''
 

  ------
  |    X
  |   /I\
 /_\  / \ ''']
          
print(" __________")
print("|          |")
print("| AHORCADO | ")
print("|__________|")
print("(tenes que escribir en minuscula)\n")

palabra=input("Ingrese la palabra: ")
n=int(len(palabra))
v=int(6)
LetrasIncorrectas=" "
TodasLetras=" "
#from os import system
#system("cls")
#print(" \n"*100)

print(" _________________________________________________________ ")
print("|                                                         |")
print("| JUGEMOS AL AHORCADO, ADIVINA LA PALABRA (HASTA 6 VIDAS) |")	
print("|_________________________________________________________|")

print('''

  ------
  |    
  |   
 /_\      ''')

print("_\n"*n)
j=int(1)
while n!=0 and v>0:

    b=int(6-v)
    
    f=int(0)
    print()
    letra=input(print("Ingrese una letra ==> "))
    letra=letra.lower()
    
    if len(letra) != 1:
            print ('PONÉ UNA SOLA LETRA!')
            v=v+1
    elif letra in TodasLetras:
        print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
    elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('ESO NO ES UNA LETRA CAPO!')
            v=v+1
    else:
        espacio= '_' * len(palabra)  

        for i in range(len(palabra)):
            if palabra[i] in letra:
                espacio = espacio[:i] + palabra[i] + espacio[i+1:]
            
        if letra in palabra:
            f=f+1
            n=n-1
        else:
           LetrasIncorrectas=LetrasIncorrectas+letra+",  "
   

        for letra in espacio:
            print (letra, " ")
    

        if(f==0):
            v=v-1
            print(AHORCADO[b])
            


        print("[tenés ", v," vidas] \n")
        print("Letras incorrectas: ", LetrasIncorrectas)
        
    TodasLetras=TodasLetras+" "+letra  
    
if(v<1):
    print("FRACASADO")
    print("la palabra era: ", palabra)
    
else:
    print("MUY BIEN, FELICITACIONES!!!")
    print("La palabra era: ", palabra)
    

