"""
Desafio - Valide um CPF
"""
while True:

    cpf = input('Digite um CPF: ')
    new_cpf = cpf[:-2]

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

    if new_cpf == cpf:
        print('CPF válido.')
    else:
        print('CPF inválido.')
