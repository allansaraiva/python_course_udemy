"""
Desempacotamento de listas em Python
"""
# list_1 = ['Allan', 'Carlos', 'Lima', 'Saraiva']

# n1, *another_list, last_on_the_list = list_1  # * + variável gera outra lista.
# print(n1, another_list, last_on_the_list)  # last_on_the_list - mostra o último valor da variável list_1.


list_1 = ['Allan', 'Carlos', 'Lima', 'Saraiva']
*another_list, n1, n2 = list_1  
print(n2, another_list)
