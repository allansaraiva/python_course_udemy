"""
Groupby - Agrupando valores
"""
from itertools import groupby

alunos = [
    {'Nome': 'Allan', 'Nota': 'A'},
    {'Nome': 'Allany', 'Nota': 'A'},
    {'Nome': 'Kaline', 'Nota': 'B'},
    {'Nome': 'Josè', 'Nota': 'D'},
    {'Nome': 'Gilberto', 'Nota': 'F'},
    {'Nome': 'Fábio', 'Nota': 'C'},
    {'Nome': 'João', 'Nota': 'F'},
    {'Nome': 'Jacinto', 'Nota': 'A'},
    {'Nome': 'Martha', 'Nota': 'D'},
    {'Nome': 'Ana', 'Nota': 'F'}
]

ordena = lambda item: item['Nota']
alunos.sort(key=ordena)  # sort() --> Ordena os valores.
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))

    if quantidade == 1:
        print(f'{quantidade} aluno tirou a nota {agrupamento}')
    else:
        print(f'{quantidade} alunos tiraram a nota {agrupamento}')
    print()
