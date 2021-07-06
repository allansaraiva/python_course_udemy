"""
Funções (def) em Python - Parte 4
"""


"""
var = 'Valor'


def function():
    print(var)


def function_2():
    global var  # global -->
    var = 'Outro valor'
    print(var)

function()
function_2()
print(var)
"""


"""
var = 'Valor'


def function():
    other_var = 1234


def function_2():
    print(other_var)  # --> Não se pode chamar uma variável de um função para outra função.

function()
function_2()
"""


variable = 'Valor'


def function():
    other_var = 'Valor qualquer'
    return other_var


def function_2(arg):
    print(arg)

var = function()
function_2(var)
