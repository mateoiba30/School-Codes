def sumar(n1, n2):
    s=float(n1+n2)
    return(s)
def restar(n1, n2):
    r=float(n1-n2)
    return(r)
def multiplicar(n1, n2):
    m=float(n1*n2)
    return(m)
def dividir(n1, n2):
    d=float(n1/n2)
    return(d)

if __name__=="__main__":
    x=float(input("Ingrese un número: "))
    y=float(input("Ingrese otro número: "))
    op=int(0)

    while op!=5:
        op=int(input("Ingrese: \n 1 para SUMAR \n 2 para RESTAR \n 3 para MULTIPLICAR \n 4 para DIVIDIR \n 5 para FINALIZAR \n ==>"))

        if(op==1):
            print(sumar(x, y))
        elif(op==2):
            print(restar(x, y))
        elif(op==3):
            print(multiplicar(x, y))
        elif(op==4):
            print(dividir(x, y))
        elif(op==5):
            print("programa finalizado")
        else:
            print("Eso no es 1, 2, 3, 4, o 5!!")
            print(">:(")
        print("\n")

