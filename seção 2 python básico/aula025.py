"""
Operadores lógicos
and, or, not
in, not in
"""
# nome = str(input('Seu nome: '))
# f nome == 'allan' or nome == 'roger':
#    print('True')
# else:
#     print('false')


# nome = str(input('Seu nome: '))
# if not nome:  # Se a variável estiver vazia, o programa imprime uma mensagem de erro.
#     print('por favor, nos informe o seu nome.')


# nome = str(input('Seu nome: '))
# if 'l' in nome:
#     print('Seu nome tem a letra L.')
# else:
#     print('Seu nome não tema letra L.')


# nome = str(input('Seu nome: '))
# if 'l' not in nome:
#     print('Não tem L no meu nome.')
# else:
#     print('Tem l no seu nome.')


user = str(input('Nome de usuário: '))
senha = int(input('Senha: '))

user_bd = 'allan'
senha_bd = 123456

if user == user_bd and senha == senha_bd:
    print('Você está logado.')
else:
    print('Usuário ou senha inválidos.')
