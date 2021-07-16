"""
Filter - Filtro de dados
"""

from aula079 import *

"""
nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))
"""


"""
def filtra(produto):
    if produto['preço'] > 100:
        return True


produtos_maiores = filter(filtra, produtos)

for produto in produtos_maiores:
    print(produto)
"""


def filtra(pessoa):
    if pessoa['idade'] > 18:
        return True

pessoas_maiores = filter(filtra, pessoas)

for pessoa in pessoas_maiores:
    print(pessoa)
