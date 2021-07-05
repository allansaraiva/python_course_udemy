"""
Funções (def) em Python - Parte 1
"""


def salutation(message='Olá', name='Allan'):
    name = name.lower().replace('a', '4')  # Troca a letra "a" por "4".
    print(message, name)

salutation()  # Você pode mudar o nome das variáveis.
