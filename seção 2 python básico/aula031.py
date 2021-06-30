"""
Formatando valores em Python
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE TIPO - s, d ou f)
> - Esquerda
^ - Centro
< - Direita
"""

nome = 1
print(f'{nome:~^11}')
