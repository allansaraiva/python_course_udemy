"""
Split, Join e Enumerate em Python.

Splip - Dividir uma string  # str
Join - Juntar uma lista  # str
Enumarate - Enumerar elementos da lista  # list / iteráveis
count - Contagem  # str
"""
# string = 'O Brasil é o país da corrupção, Brasil é uma merda'
# list_1 = string.split(' ')  # split() - Separa todas as palavras da string em uma lista
#
# word = ''
# score = 0
# for value in list_1:
#     quantity_times = list_1.count(value)
#
#     if quantity_times > score:
#         score = quantity_times
#         word = value
#
# print(f'A palavra que apareceu mais vezes foi a palavra: {word} ({score}x)')


# string = 'O Brasil é o país da corrupção'
# list_1 = string.split(' ')
# string_2 = ' '.join(list_1)  # join() - Juntar uma lista  # str
#
#
# print(string)
# print(list_1)
# print(string_2)


# list_1 = ['Allan', 'Carlos', 'Lima', 'Saraiva']
#
# for index, value in enumerate(list_1):
#     print(index, list_1[index])


# list_1 = ['Allan', 'Carlos', 'Lima', 'Saraiva']
#
# n1, n2, n3, n4 = list_1
# print(n4)

list_1 = [
    ['Allan', 'Carlos', 'Lima', 'Saraiva'],
    ['Allany', 'Liste', 'Lima', 'Saraiva'],
    ['Kaline', 'Cristina', 'Araújo', 'Lima', 'Saraiva']
]
for index, value in enumerate(list_1):
    print(index, value)
