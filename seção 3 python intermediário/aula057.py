"""
Exercícios
"""

# Crie uma função que recebe uma função como parâmetro e retorne o valor da segunda função executada


def function_1():
    return 'Qualquer coisa aqui'


def function_2(function):
    return function()

exe = function_2(function_1)
print(exe)
