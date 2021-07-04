"""
Operação ternária em Python
"""
# logged_user = True
#
# if logged_user:
#     message = 'Usuário logado.'
# else:
#     message = 'Usuário precisa fazer login.'
#
# print(message)


# logged_user = False
# message = 'Usuário logado' if logged_user else 'Usuário precisa fazer login.'
# print(message)


age = input('Qual a sua idade? ')

if not age.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    age = int(age)
    of_age = (age >= 18)
    message = 'Pode acessar.' if of_age else 'Não pode acessar.'
    print(message)
