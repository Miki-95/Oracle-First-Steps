#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Crear un gráfico de barras con la información alojada en Oracle 
#
# Author:      Miguel Ángel
#
# Created:     21/01/2022
# Copyright:   (c) Miguel Ángel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cx_Oracle
import matplotlib.pyplot as plt



try:
   dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE')
   conn = cx_Oracle.connect(user='Curso_DataScience', password='contrasenna', dsn=dsn_tns)
   cur = conn.cursor()
except Exception as err:
    print("Se produjo un error en las conexiones",err)


# La estructura de drinks: (Nregistro : 0, Country : 1, Beer : , Spirit : 3, Wine : 4, Pure : 5, Continent : 6)


#Creamos los continentes

Asia = 0
Africa = 0
NAmerica = 0
SAmerica = 0
Oceania = 0
Europa = 0


#Leer y filtrar por continente

cur.execute('select * from drinks')
for row in cur:

   if row[6] == 'Asia':
        Asia = Asia + (row[4])

   elif row[6] == 'Africa':
        Africa = Africa + (row[4])

   elif row[6] == 'South America':
        SAmerica = SAmerica + (row[4])

   elif row[6] == 'North America':
        NAmerica = NAmerica + (row[4])

   elif row[6] == 'Oceania':
        Oceania = Oceania + (row[4])

   elif row[6] == 'Europe':
        Europa = Europa + (row[4])


America = NAmerica + SAmerica

#Para comprobar que ha funcionado:
#print (Asia, Africa, America, Oceania, Europa)


## Declaramos valores para el eje x
eje_x = ['Asia', 'Africa', 'América', 'Oceania','Europa']

## Declaramos valores para el eje y
eje_y = [Asia, Africa, America, Oceania, Europa]

## Creamos Gráfica
plt.bar(eje_x, eje_y)

## Legenda en el eje y
plt.ylabel('Porciones de Vino')

## Legenda en el eje x
plt.xlabel('5 Continentes')

## Título de Gráfica
plt.title('Consumo de Vino por continente')

## Mostramos Gráfica
plt.show()



conn.close()

