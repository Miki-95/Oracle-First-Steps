#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:     Introducir registros en Oracle usando Python
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
   c = conn.cursor()
   sql="insert into Ejemplo(empno, nombre, profesion, salario) values (02, 'Laura', 'Astronauta', 150000)"
   c.execute(sql)

except Exception as err:
    print("Se produjo un error en las conexiones",err)
else:
    conn.commit()
    print ("Registro insertado")
finally:
    c.close()
    conn.close()
    print("Todo cerrado")


