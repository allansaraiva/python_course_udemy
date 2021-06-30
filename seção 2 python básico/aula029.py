# EXERCÍCIO 1/3
"""
num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print('Você digitou um número PAR.')
    elif num % 2 == 1:
        print('Você digitou um número ÍMPAR.')
else:
    print('Você não digitou um número inteiro.')
"""

# EXERCÍCIO 2/3
"""
horas = input('Que horas são? ')
if horas.isdigit():
    horas = int(horas)
    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 12 <= horas <= 18:
        print('Boa tarde.')
    else:
        print('Boa noite.')
else:
    print('Você não me deu uma informação clara.')
"""

# EXERCÍCIO 3/3
"""
nome = input('Qual o seu nome? ')
nome_qtd = len(nome)
if nome_qtd <= 4:
    print('Seu nome é CURTO.')
elif 5 <= nome_qtd <= 6:
    print('Seu nome é NORMAL.')
else:
    print('Seu nome é MUITO GRANDE.')
"""