"""
Count - Contadores infinitos --> itertools
"""


from itertools import count

"""
contador = count(start=5)

for valor in contador:
    print(valor)

    if valor == 10:
        break
"""

contador = count(start=1)
lista = ['Allan', 'Carlos', 'Lima', 'Saraiva']
lista = zip(contador, lista)
nomes = zip(lista)

for index, valor in lista:
    print(index, valor)