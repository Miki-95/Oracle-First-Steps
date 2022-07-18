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

import cx_Oracle
import matplotlib.pyplot as plt


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



#grafico
fig, axs = plt.subplots(1, 3, figsize=(15, 6), sharey=True)
axs[0].bar(beerC, beerQ)
axs[0].set_title('Cerveza')
axs[1].bar(wineC, wineQ, color='red')
axs[1].set_title('Vino')
axs[2].bar(licorC, licorQ, color='green')
axs[2].set_title('Licor')
fig.suptitle('Paises con más consumo de:')
plt.show()

