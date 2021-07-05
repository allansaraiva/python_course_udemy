"""
Exercícios
"""


# Fizz Buzz - So o parâmetro da função for divisível por 2, retorne FIZZ, se o parâmetro da função for divisível por 5,
# retorne BUZZ. Se o parâmetro da função for divisível por 5 e por 3, retorne FIZZBUZZ, caso contrário, retorne o número
# enviado.


def division(n1):
    if n1 % 5 == 0 and n1 % 3 == 0:
        return 'FIZZBUZZ'
    if n1 % 3 == 0:
        return 'FIZZ'
    if n1 % 5 == 0:
        return 'BUZZ'
    return n1


var = division(45)
print(var)
