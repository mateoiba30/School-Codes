import sqlite3

base=sqlite3.connect("basededatos.db")
registro=base.cursor()
el_id=int(input("Ingrese el id a borrar: "))
instruccion="DELETE from Usuarios WHERE(id='%d')"%(el_id)
print(instruccion)
registro.execute(instruccion)
base.commit()

print("La base de datos se abriò correctamente")
print(" ")
print("ID |   NOMBRE |  APELLIDO |  SALDO")
print("")
registro.execute("SELECT * from Usuarios")
for fila in registro:
    print("%d,   %s,   %s,   %d"%(fila[0], fila[1], fila[2], fila[3]))

print("")
print("Operacion satisfactoria")


base.close()
