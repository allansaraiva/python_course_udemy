nome = 'Allan'
idade = 20
peso = 80
altura = 1.84
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / (altura ** 2)
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O imc de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}')
