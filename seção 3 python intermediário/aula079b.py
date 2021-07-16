from aula079 import *

"""
nova_lista = [x * 2 for x in lista]
print(lista)
print(nova_lista)
"""


"""
def aumento(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p


novos_precos = map(aumento, produtos)

for preco in novos_precos:
    print(preco)
"""

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
