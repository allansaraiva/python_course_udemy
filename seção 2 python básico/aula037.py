"""
Listas em python
"""
# lista = ['allan', 'carlos', 'lima', 'saraiva']
# lista[3] = 'qualquer outra coisa'
# print(lista[3].title())


# lista = ['allan', 'carlos', 'lima', 'saraiva']
# print(lista[::-1])


# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]              # extend() - adiciona.
# lista_1.extend(lista_2)
# print(lista_1)


# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# del lista_1[0:2]                    # del - deleta.
# print(lista_1)


# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_2.append('b')                # append() - adiciona um valor no final da lista.
# print(lista_2)


# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_1.insert(0, 8)  # insert(índice, o que adicionar) - adiciona um item na lista na posição escolhida.
# print(lista_1)


# lista_1 = [1, 2, 3]
# lista_1.pop()                       # pop() - remove o último índice da lista.
# print(lista_1)


# lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lista_1))  # max() - maior valor da lista.
# print(min(lista_1))  # min() - menor valor da lista.


# lista_1 = list(range(1, 10))  # list() - cria uma lista.
# print(lista_1)


# lista_1 = [1, 2, 3, 4, 5]
# soma = 0
# for valor in lista_1:
#     soma += valor
#
# print(soma)


secreto = 'perfume'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale. Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print(secreto_temporario)
