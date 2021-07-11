"""
Zip e Zip_longest - Unindo iteráveis
"""


"""
cidades = ['Natal', 'São Paulo', 'Rio de Janeiro']
estados = ['RN', 'SP', 'RJ']

cidade_estados = zip(cidades, estados)  # zip() --> une iteráveis.

for valor in cidade_estados:
    print(f'{valor[0]} - {valor[1]}')
"""


"""
from itertools import zip_longest

cidades = ['Natal', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Goias']
estados = ['RN', 'SP', 'RJ']

cidade_estados = zip_longest(cidades, estados, fillvalue='"Sem valor"')  # zip_longest() --> une independente do valor.

for valor in cidade_estados:
    print(f'{valor[0]} - {valor[1]}')
"""


from itertools import zip_longest, count

indice = count()  # count() --> Contador.
cidades = ['Natal', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Goias']
estados = ['RN', 'SP', 'RJ']

cidade_estados = zip(indice, cidades, estados)

for indices, cidade, estado in cidade_estados:
    print(indices, cidade, estado)
