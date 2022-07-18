#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Miguel Ángel
#
# Created:     19/01/2022
# Copyright:   (c) Miguel Ángel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cx_Oracle


try:
   dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE')
   conn = cx_Oracle.connect(user='Curso_DataScience', password='contrasenna', dsn=dsn_tns)
   cur = conn.cursor()

except Exception as err:
    print("Error en las conexiones",err)



# Abrimos el csv y lo leemos
f = open("drinks.csv", "r")
g = f.readlines()
f.close()


# Introducimos los registros de lo que estamos leyendo en la base de datos Oracle
key = 1

for linea in g:
        # Eliminamos el salto de línea
        linea = linea.rstrip()
        # Ahora convertimos la línea en un array con split
        separador = ","
        lista = linea.split(",")
        # Tenemos la lista.
        if lista[0]!= 'country':
            cur.execute ("insert into drinks(Nregistro, Country, Beer, Spirit, Wine, Pure, Continent) values ( :1,:2,:3,:4,:5,:6,:7)", (key, lista[0],int(lista[1]),int(lista[2]),int(lista[3]),float(lista[4]),lista[5]))
            key = key+1



conn.commit()
cur.close()
conn.close()
print("Todo cerrado")