"""
Tuplas em Python
"""


"""
tuple_1 = (1, 2, 3, 'a', 'b', 'c')

for index, value in enumerate(tuple_1):
    print(index, value)
"""


"""
tuple_1 = 1, 2, 3, 4, 5
tuple_2 = 6, 7, 8, 9, 10
tuple_3 = tuple_2 + tuple_1  # Pode-se concatenar tuplas.
print(tuple_3)
"""


tuple_1 = 1, 2, 3, 4, 5
tuple_1 = list(tuple_1)  # Transformando tuplas em listas.
tuple_1[2] = 3000  # Modificando um item da tupla (que agora é lista).
tuple_1 = tuple(tuple_1)  # Voltando a ser tupla.
print(tuple_1)
