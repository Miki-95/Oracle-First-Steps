#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Miguel Ángel
#
# Created:     25/01/2022
# Copyright:   (c) Miguel Ángel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


import cx_Oracle
import matplotlib.pyplot as plt

#CREAMOS UNA FUNCION QUE NOS GRAFIQUE LOS RESULTADOS QUE VAMOS A OBTENER
def grafico(x,y, alcohol):

    ## Declaramos valores para el eje x
    eje_x = x

    ## Declaramos valores para el eje y
    eje_y = y

    ## Creamos Gráfica
    plt.bar(eje_x, eje_y)

    ## Leyenda en el eje y
    plt.ylabel('Porciones de '+ alcohol)

    ## Leyenda en el eje x
    plt.xlabel('Paises')

    ## Título de Gráfica
    plt.title('Los 5 paises en los que más '+ alcohol+ ' se consume en el mundo (porciones/año)')

    ## Mostramos Gráfica
    plt.show()




## La estructura de drinks: (Nregistro : 0, Country : 1, Beer : , Spirit : 3, Wine : 4, Pure : 5, Continent : 6)

dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE')
conn = cx_Oracle.connect(user='Curso_DataScience', password='contrasenna', dsn=dsn_tns)
c = conn.cursor()

#Seleccciono los 5 paises donde más cerveza se consume gracias a Oracle y lo guardo en dos listas en Python, una para el nombre de los paises y otra pa ra la cantidad de cerveza consumida
c.execute('SELECT * FROM (SELECT Country, Beer FROM drinks ORDER BY Beer DESC) where rownum < 6' )

beerC=[]
beerQ= []

for row in c:
    beerC.append(row[0])
    beerQ.append(row[1])


#IDEM para vino
c.execute('SELECT * FROM (SELECT Country, Wine FROM drinks ORDER BY Wine DESC) where rownum < 6' )
wineC=[]
wineQ= []
for row in c:
    wineC.append(row[0])
    wineQ.append(row[1])

#IDEM para licores
c.execute('SELECT * FROM (SELECT Country, Spirit FROM drinks ORDER BY Spirit DESC) where rownum < 6' )
licorC=[]
licorQ= []
for row in c:
    licorC.append(row[0])
    licorQ.append(row[1])



#Pedimos que nos grafiquen la cerveza
grafico(beerC,beerQ,"cerveza")

#Pedimos que nos grafiquen el vino
grafico(wineC,wineQ,"vino")

#Pedimos que nos grafiquen el licor
grafico(licorC,licorQ,"licor")