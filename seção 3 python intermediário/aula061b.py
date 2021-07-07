"""
Dicionários em Python
"""

"""
dictionary = {1: 'a', 2: 'b', 3: 'c'}
c = dictionary.copy()  # copy() --> Faz uma cópia.
c[1] = 'Allan'
print(dictionary)
print(c)
"""


"""
import copy

dictionary = {1: 'a', 2: 'b', 3: 'c', 'd': ['Allan', 'Saraiva']}
copia = copy.deepcopy(dictionary)  # deepcopy() --> Faz uma cópia profunda sem compremeter na mudança de valores.

copia[1] = 'Allan'
copia['d'][0] = 'Allany'

print(dictionary)
print(copia)
"""


"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 4000
}

dictionary.popitem()  # pop() --> Exclui o item desejado.
print(dictionary)
"""


"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 4000
}

dictionary.popitem()  # popitem() --> Exclui o último item.
print(dictionary)
"""


dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 4000
}

dictionary_2 = {
    'Produto 4': 2000,
    'Produto 5': 5000,
    'Produto 6': 6000
}

dictionary.update(dictionary_2)  # Concatenar os dicionários.
print(dictionary)
