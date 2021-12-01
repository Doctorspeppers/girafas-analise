import MySQLdb
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

cnx = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="girafas"  
)

cursor = cnx.cursor()

cursor.execute("SELECT id,regiao,estado,cidade FROM franquias")

infos = cursor.fetchall()

cidades = []
estados = []
regioes = []

for info in infos:
    cidades.append(info[3])
    estados.append(info[2])
    regioes.append(info[1])

regioes = dict(Counter(regioes))


plt.rcdefaults()
fig, ax = plt.subplots()

tuplaregioes = tuple(regioes.keys())
nregioes = len(tuplaregioes)
valoresregioes = tuple(regioes.values())

y = np.arange(len(tuplaregioes))
ax.barh(y, valoresregioes)
ax.set_yticks(y,labels=tuplaregioes)
ax.invert_yaxis() 
ax.set_xlabel('Restaurantes')
ax.set_title('Quantos restaurantes a em cada regiao?')

plt.savefig("regioes.png")


estados = dict(Counter(estados))

plt.rcdefaults()
fig, ax = plt.subplots()

tuplaestados = tuple(estados.keys())
nestados = len(tuplaestados)
valoresestados = tuple(estados.values())

y = np.arange(len(tuplaestados))
ax.barh(y, valoresestados)
ax.set_yticks(y,labels=tuplaestados)
ax.invert_yaxis() 
ax.set_xlabel('Restaurantes')
ax.set_title('Quantos restaurantes a em cada estado?')

plt.savefig("estados.png")

