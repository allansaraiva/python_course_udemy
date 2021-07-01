"""
For in em Python
"""

texto = 'python'
novo_texto = ''

for letra in texto:
    if letra == 'p':
        novo_texto += letra.upper()
    elif letra == 'n':
        novo_texto += letra.upper()
    else:
        novo_texto += letra

print(novo_texto)
