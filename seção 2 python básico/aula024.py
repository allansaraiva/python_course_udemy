"""
Operadores relacionais
==, >, >=, <, <=, !=
"""
# n1 = 4
# n2 = 5
# ex1 = (n1 == n2)
# ex2 = (n1 > n2)
# ex3 = (n1 >= n2)
# ex4 = (n1 < n2)
# ex5 = (n1 <= n2)
# ex6 = (n1 != n2)
# print(ex1, ex2, ex3, ex4, ex5, ex6)

idade = int(input('Qual a sua idade? '))
idade_minima = 20
idade_maxima = 30
if idade_minima <= idade <= idade_maxima:
    print('Pode pegar o empréstimo.')
else:
    print('Não pode pegar o empréstimo.')
