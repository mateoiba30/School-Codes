import sqlite3

base=sqlite3.connect("basededatos.db")
registro=base.cursor()

ID=int(input("ingrese el ID de la fila a modificar: "))
Nombre=raw_input("Nombre: ")
Apellido=raw_input("Apellido: ")
Saldo=int(input("Saldo: "))
instruccion="UPDATE Usuarios SET 'nombre'='%s', 'apellido'='%s', 'saldo'='%d'  WHERE(id='%d');" %(Nombre, Apellido, Saldo, ID)
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
    
