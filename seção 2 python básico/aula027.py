"""
funções built-in
"""

# num_1 = input('Digite um número: ')
# num_2 = input('Digite outro número: ')

# if num_1.isdigit() and num_2.isdigit():
#     num_1 = int(num_1)
#     num_2 = int(num_2)
#     print(num_1 + num_2)
# else:
#     print('Não pude calcular seus valores.')


num_1 = input('Digite um valor: ')
num_2 = input('Digite outro valor: ')

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    print(num_1 + num_2)

except:
    print('Não pude calcular os dois valores.')
