#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:     Hacer una consulta a Oracle
#
# Author:      Miguel Ángel
#
# Created:     20/01/2022
# Copyright:   (c) Miguel Ángel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import cx_Oracle

# mi tabla : drinks(Nregistro, Country, Beer, Spirit, Wine, Pure, Continent)

try:
   dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE')
   conn = cx_Oracle.connect(user='Curso_DataScience', password='contrasenna', dsn=dsn_tns)
   cur = conn.cursor()
   # Escribimos nuestra consulta en SQL
   Consulta_1="Select Country, Spirit from Curso_DataScience.drinks WHERE Spirit >= 12"
   #Ejecutamos la consulta con el cursor
   cur.execute(Consulta_1)

except Exception as err:
    print("Se produjo un error en las conexiones",err)

finally:
    for row in cur:
        print(row)
    cur.close()
    conn.close()
    print("Todo cerrado")


