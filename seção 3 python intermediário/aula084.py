"""
Uso de try e except como condicional
"""


def converte_inteiro(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_inteiro(input('Digite um número: '))

    if numero is None:
        print('Digite apenas números.')
    else:
        print(numero * 5)
