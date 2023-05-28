import sqlite3
base=sqlite3.connect("basededatos.db")

def delete():
    registro=base.cursor()
    ID=int(input("Ingrese el id a borrar: "))
    instruccion="DELETE from Usuarios WHERE(ID='%d')"%(ID)
    print(instruccion)
    registro.execute(instruccion)
    base.commit()
    
def insert():
    registro=base.cursor()
    ID=int(input("ID: "))
    Nombre=raw_input("Nombre: ")
    Apellido=raw_input("Apellido: ")
    Saldo=int(input("Saldo: "))
    instruccion="INSERT INTO Usuarios('id', 'nombre', 'apellido', 'saldo') VALUES ('%d', '%s', '%s', '%d')" %(ID, Nombre, Apellido, Saldo)
    print(instruccion)
    registro.execute(instruccion)      
    base.commit()

def update():
    registro=base.cursor()
    ID=int(input("ingrese el ID de la fila a modificar: "))
    Nombre=raw_input("Nombre: ")
    Apellido=raw_input("Apellido: ")
    Saldo=int(input("Saldo: "))
    instruccion="UPDATE Usuarios SET 'nombre'='%s', 'apellido'='%s', 'saldo'='%d'  WHERE(id='%d');" %(Nombre, Apellido, Saldo, ID)
    print(instruccion)
    registro.execute(instruccion)      
    base.commit()
    
def select():
    registro=base.cursor()
    print("La base de datos se abriò correctamente")
    print(" ")
    print("ID |   NOMBRE |  APELLIDO |  SALDO")
    print("")
    registro.execute("SELECT * from Usuarios")
    for fila in registro:
        print("%d,   %s,   %s,   %d"%(fila[0], fila[1], fila[2], fila[3]))
    print("")
    print("Operacion satisfactoria")

if __name__=="__main__":
    op=int(0)

    while op!=5:
        op=int(input("Ingrese: \n 1 para borrar \n 2 para agregar \n 3 para modificar \n 4 para mostrar \n 5 para finalizar \n ==>"))

        if(op==1):
            print("borrar: ")
            print(delete())            
        elif(op==2):
            print("agregar: ")
            print(insert())
        elif(op==3):
            print("modificar: ")
            print(update())          
        elif(op==4):
            print("mostrar: ")
            print(select())            
        elif(op==5):
            print("programa finalizado")
        else:
            print("Eso no es 1, 2, 3, 4, o 5!!")
            print(">:(")
        print("\n")

    base.close()

