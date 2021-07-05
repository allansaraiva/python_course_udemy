"""
Exercícios
"""


# Crie uma fução que receba 2 números. O primeiro é um valor e o segundo é um percentual (Ex. 10%). Retorne o valor do
# primeiro número somado com o percentual.


def percentage(n1, n2):
    return n1 + (n1 * n2 / 100)

var = percentage(100, 10)
print(var)
