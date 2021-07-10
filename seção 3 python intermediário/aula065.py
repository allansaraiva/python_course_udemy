"""
List Comprehension em Python
"""
lista = [1, 2, 3, 4, 5, 6]
ex_1 = [variavel for variavel in lista]

ex_2 = [valor * 2 for valor in lista]  # Multiplicando os valores da lista por 2

ex_3 = [(v, v2) for v in lista for v2 in range(3)]


l2 = ['allan', 'Carlos', 'Lima', 'Saraiva']
ex_4 = [v.replace('a', '@') for v in l2]


tupla = (
    ('chave', 'valor'),
    ('chave 2', 'valor 2')
)
ex_5 = [(valor, chave) for chave, valor in tupla]


l3 = list(range(31))
ex_6 = [v for v in l3 if v % 3 == 0 if v % 5 == 0]

ex_7 = [v if v % 3 == 0 else 'NO' for v in l3]
print(ex_7)
