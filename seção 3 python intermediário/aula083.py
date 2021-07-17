"""
Levantando exceções em Python (raise)
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro)
        raise

try:
    print(divide(2, 4))
except ZeroDivisionError as erro:
    print(erro)
