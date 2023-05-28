import sqlite3

base=sqlite3.connect("basededatos.db")
registro=base.cursor()

ID=int(input("ID: "))
N=input("Nombre: ")
Apellido=input("Apellido: ")
Saldo=int(input("Saldo: "))
instruccion="INSERT INTO Usuarios('id', 'nombre', 'apellido', 'saldo') VALUES ('%d', '%s', '%s', '%d')" %(ID, N, Apellido, Saldo)
print(instruccion)
registro.execute(instruccion)      
base.commit()

print("La base de datos se abrio correctamente")
print(" ")
print("ID |   NOMBRE |  APELLIDO |  SALDO")
print("")
registro.execute("SELECT * from Usuarios")
for fila in registro:
    print("%d,   %s,   %s,   %d"%(fila[0], fila[1], fila[2], fila[3]))

print("")
print("Operacion satisfactoria")


base.close()
