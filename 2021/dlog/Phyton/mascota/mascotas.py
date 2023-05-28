class mascota():
    nombre=" "
    especie=" "
    kilos=0
    energia=50
    hambre=50
    felicidad=50
    suciedad=50
    anos=0
    centimetros=0

    def random(self):
        n=random.randint(0, 100)

        if n==1:
            print("%d se ha enfermado" %self.nombre)
            self.energia-=50
            self.felicidad-=40
        elif n==2:
            print("%d se ha muerto" %self.nombre)
            self.energia=0
            self.hambre=0
            self.felicidad=0
            self.suciedad=100
            self.kilos=self.kilos*0.2
            op=10  
    
    def cargardatos(self):
        nombre=raw_input("ingrese el nombre: ")
        especice=raw_input("ingrese la especie: ")
        centimetros=raw_input("ingrese la altura en centimetros: ")
        kilos=raw_input("ingrese el peso en kilos: ")
        anos=raw_input("ingrese la edad en años: ")
        
    def mostrardatos(self):
        print("la energía es de %d" %self.energia)
        print("el peso en kilos es de %d" %self.kilos)
        print("el hambre es de %d" %self.hambre)
        print("la felicidad es de %d" %self.felicidad)
        print("la suciedad es de %d" %self.suciedad)
        print("la edad en años es de %d" %self.anos)
        print("la altura en centimetros es de %d" %self.centimetros)

    def alimentar(self):
        self.kilos+=0.1
        self.energia+=30
        self.hambre-=50
        self.felicidad+=30
        self.suciedad+=1

    def pasear(self):
        self.kilos-=0.5
        self.energia-=20
        self.hambre-=20
        self.felicidad+=40
        self.suciedad+=10

    def jugar(self):
        self.kilos-=0.8
        self.energia-=30
        self.felicidad+=50
        self.suciedad+=15

    def banar(self):
        self.kilos-=0.1
        self.energia-=15
        self.hambre+=5
        self.felicidad+=10
        self.suciedad=0

    def acariciar(self):
        self.felicidad+=20

    def vestir(self):
        self.felicidad-=5

    def enfermar (self):
        self.energia-=50
        self.felicidad-=40

    def curar (self):
        self.energia+=50
        self.felicidad+=40

    def dormir (self):
        self.energia+=80
        self.hambre+=50
        self.felicidad+=20

    def morir (self):
        self.energia=0
        self.hambre=0
        self.felicidad=0
        self.suciedad=100
        self.kilos=self.kilos*0.2
        

if __name__=="__main__":

    print(" ____________________")
    print("|                    |")
    print("| CUIDA A TU MASCOTA |")
    print("|____________________|\n")

    mascota1=mascota()
    mascota1.cargardatos()
    op=int(input("ingrese opción==>\n1-alimentar 2-pasear 3-jugar 4-banar 5-acariciar 6-vestir 7-enfermar 8-curar 9-dormir 10-morir 11-salir: "))

    while op!=11 and op!=10:
        if op==1:
            mascota1.alimentar()
        elif op==2:
            mascota1.pasear()
        elif op==3:
            mascota1.jugar()
        elif op==4:
            mascota1.banar()
        elif op==5:
            mascota1.acariciar()
        elif op==6:
            mascota1.vestir()
        elif op==7:
            mascota1.enfermar()
        elif op==8:
            mascota1.curar()
        elif op==9:
            mascota1.dormir()
        elif op==10:
            mascota1.morir()
        elif op!=11:
            print("numero incorrecto")

        mascota1.random()
        
        op=int(input("ingrese opción==> "))

    mascota1.mostrardatos()
