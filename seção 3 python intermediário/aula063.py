"""
Sets em Python (Conjuntos)
"""
"""
s1 = set()  # Não aceita elementos duplicados.
s1.add(5)  # add() --> Adiciona.
s1.add(9)
s1.add(6)
s1.add(6)
s1.update('python')  # update() --> Adiciona.
s1.remove(5)  # remove() --> Remove.
s1.discard(9)  # discard() --> Remove.
print(s1)
"""


"""
list_1 = [1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 'allan', 'allan']
list_1 = set(list_1)  # Elimina os valores duplicados.
list_1 = list(list_1)  # Convertendo em lista.

print(list_1)
"""


"""
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2  # | ou union() --> une
print(s3)
"""


"""
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1.intersection(s2)  # & ou intersection() --> Retorna os elementos presentes em ambos os sets.
print(s3)
"""


"""
s1 = {1, 2, 3, 8}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1.difference(s2)  # - ou difference() --> Retorna o elemento que só está presente no set da esquerda.
print(s3)
"""


s1 = {1, 2, 3, 11}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 ^ s2  # ^ ou symmetric_difference() --> Retorna elementos que estão nos sets, mas não em ambos.
print(s3)