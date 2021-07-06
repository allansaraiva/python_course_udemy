"""
Expressões lambda (funções anônimas) em Python
"""


"""
list_1 = [
    ['P1', 50],
    ['P2', 30],
    ['P3', 40],
    ['P4', 20],
    ['P5', 60]
]


def function(item):
    return item[1]

list_1.sort(key=function, reverse=True)  # sort() --> classifica a lista em ordem crescente por padrão.
print(list_1)
"""


"""
list_1 = [
    ['P1', 50],
    ['P2', 30],
    ['P3', 40],
    ['P4', 20],
    ['P5', 60]
]

list_1.sort(key=lambda item: item[1], reverse=True)  # sort() --> classifica a lista em ordem crescente por padrão.
print(list_1)
"""


list_1 = [
    ['P1', 50],
    ['P2', 30],
    ['P3', 40],
    ['P4', 20],
    ['P5', 60]
]

print(sorted(list_1, key=lambda item: item[1], reverse=True))
