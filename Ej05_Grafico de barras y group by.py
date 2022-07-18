#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Crear un gradico de barras con la informacion alojada en Oracle y usando una sentencia SQL con group_by
#
# Author:      Miguel Ángel
#
# Created:     21/01/2022
# Copyright:   (c) Miguel Ángel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cx_Oracle
import matplotlib.pyplot as plt



dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE')
conn = cx_Oracle.connect(user='Curso_DataScience', password='contrasenna', dsn=dsn_tns)
c = conn.cursor()
c.execute('select Continent, sum(Wine) from drinks  group by continent' )


## La estructura de drinks: (Nregistro : 0, Country : 1, Beer : , Spirit : 3, Wine : 4, Pure : 5, Continent : 6)


lista=()
for row in c:
    lista =lista +row
    print(lista)



## Declaramos valores para el eje x
eje_x = [lista[0], lista[2], lista[4], lista[6],lista[8],lista[10]]

## Declaramos valores para el eje y
eje_y = [lista[1], lista[3], lista[5], lista[7],lista[9],lista[11]]

## Creamos Gráfica
plt.bar(eje_x, eje_y)

## Legenda en el eje y
plt.ylabel('Porciones de Vino')

## Legenda en el eje x
plt.xlabel('6 Continentes')

## Título de Gráfica
plt.title('Consumo de Vino por continente')

## Mostramos Gráfica
plt.show()






conn.close()

