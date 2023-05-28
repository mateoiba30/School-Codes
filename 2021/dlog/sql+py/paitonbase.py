import sqlite3

base=sqlite3.connect("basededatos.db")
registros=base.cursor()
print("La base de datos se abriò correctamente")
print(" ")
print("ID |   NOMBRE |  APELLIDO |  SALDO")
print("")
registros.execute("SELECT * from Usuarios")
for fila in registros:
    print("%d,   %s,   %s,   %d"%(fila[0], fila[1], fila[2], fila[3]))

print("")
print("Operacion satisfactoria")

base.close()
