#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Leer una base de datos alojada en Oracle
#
# Author:      Miguel Ángel
#
# Created:     19/01/2022
# Copyright:   (c) Miguel Ángel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE')
conn = cx_Oracle.connect(user='usuario', password='contrasenna', dsn=dsn_tns)
c = conn.cursor()
c.execute('select count(*) from Ejemplo')


for row in c:
   print(row)
conn.close()

