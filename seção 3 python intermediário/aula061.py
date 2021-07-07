"""
Dicionários em Python
"""

"""
dictionary = {'Chave 1': 'Valor da chave 1'}
dictionary['Chave 2'] = 'Valor valor da chave 2'  # Adiciona item ao dicionário.

print(dictionary['Chave 1'])  # Retorna o valor da chave.
"""

"""
dictionary = dict(chave_1='Valor 1', chave_2='Valor 2')  # Outra forma de fazer dicionários.
print(dictionary['chave_2'])
"""

"""
dictionary = {
    (1, 2, 3, 4): 'Tupla'
}

print(dictionary[(1, 2, 3, 4)])  # Pode-se usar tuplas em dicionários.
"""

"""
dictionary = {
    'Produto 1': 3000,
    'Produto 2': 5000
}
dictionary['Produto 3'] = 6000
if 'Produto 3' in dictionary:
    print(dictionary['Produto 3'])
else:
    print(dictionary['Produto 1'])
"""

"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
}
dictionary['Produto 3'] = 2000

if dictionary.get('Produto 3') is not None:  # 
    print(dictionary['Produto 3'])
else:
    print('Essa chave não existe.')
"""

"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
}
dictionary.update({'Produto 3': 2000})  # update() --> Adiciona uma chave ao dicionário.
print(dictionary['Produto 3'])
"""

"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 2000
}
del dictionary['Produto 1']  # del --> Exclui uma chave do dicionário.

print(dictionary)
"""

"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 2000
}

print(1000 in dictionary.values())  # values() --> Encontra valores.
print('Produto 9' in dictionary.keys())  # keys() --> Encontra chaves.
"""

"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 2000
}

for k in dictionary:  # Acessa apenas as chaves no laço FOR.
    print(k)

for v in dictionary.values():  # Acessa apenas os valores no laço FOR.
    print(v)
"""


"""
dictionary = {
    'Produto 1': 1000,
    'Produto 2': 3000,
    'Produto 3': 2000
}

for k, v in dictionary.items():  # Acessas as chaves e os valores e imprime na tela.
    print(k, ':', v)
"""


"""
client = {
    'Cliente 1': {
        'nome': 'Allan',
        'Sobrenome': 'Saraiva'
    },
    'Cliente 2': {
        'nome': 'Allany',
        'Sobrenome': 'Saraiva'
    },
    'Cliente 3': {
        'nome': 'Kaline',
        'sobrenome': 'Saraiva'
    }
}

for client_k, client_v in client.items():
    print(f'{client_k}')
    for dados_k, dados_v in client_v.items():
        print(f'\t{dados_k} = {dados_v}')
"""

