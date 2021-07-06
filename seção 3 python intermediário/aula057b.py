"""
Exercícios
"""

# Crie uma função que recebe uma função como parâmetro e retorne o valor da função 2 executada. Faça a função 1 executar
# duas funções que recebam um número diferente de argumentos.


def master(function, *args, **kwargs):
    return function(*args, **kwargs)


def say_hi(name):
    return f'Oi {name}'


def salutation(name, greeting):
    return f'{greeting} {name}'

exe = master(say_hi, name='Allan')
exe_2 = master(salutation, name='Allan', greeting='Boa noite!')
print(exe)
print(exe_2)
