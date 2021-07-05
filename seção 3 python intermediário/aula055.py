"""
Funções (def) em Python - Parte 3
"""

"""
list_1 = [1, 2, 3, 4, 5]
print(*list_1, sep='_')  # * --> desempacota a lista.  # sep= --> Separador.
"""


"""
def function(*args):  # *args --> Usa-se quando não se tem um total de valores definidos.
    print(args)
    print('índice 0:', args[0])
    print('índice 3:', args[3])
    print('Tamanho:', len(args))

function(1, 2, 3, 4, 5, 6)
"""


"""
def function(*args):   # *args --> Usa-se quando não se tem um total de valores definidos.
    args = list(args)
    args[0] = 20
    print(args)

function(1, 2, 3, 4, 5, 6)
"""


"""
def function(*args):  # *args --> Usa-se quando não se tem um total de valores definidos.
    print(args)

list_1 = [1, 2, 3, 4, 5]
function(*list_1, 6, 7, 8)
"""

"""
def function(*args, **kwargs):  # kwargs --> Key words arguments. --> Parâmetros nomeados. 
    print(args, kwargs['name'], kwargs['surname'])

list_1 = [1, 2, 4, 5]
list_2 = [10, 20, 30]
function(*list_1, *list_2, name='Allan', surname='Saraiva')
"""


def function(*args, **kwargs):
    print(args)

    age = kwargs.get('age')  # get() --> Busca o que for pedido, se não houver, retorna None.
    print(age)

list_1 = [1, 2, 4, 5]
list_2 = [10, 20, 30]
function(*list_1, *list_2, name='Allan', surname='Saraiva', age=20)
