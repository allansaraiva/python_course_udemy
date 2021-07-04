from random import randint
from time import sleep

number = str(randint(100000000, 999999999))
new_cpf = number

total = 0
reverse = 10
for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        digit = 11 - (total % 11)

        if digit > 9:
            digit = 0
        total = 0
        new_cpf += str(digit)

print('Gerando um CPF válido...')
sleep(3)
print(new_cpf)
