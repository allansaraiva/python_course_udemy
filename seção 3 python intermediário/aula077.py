"""
Combinations, Permutations e Product - Itertools

Combinations --> Combinações possíveis (a ordem não importa).

Permutations --> Combinações possíveis (a ordem importa).

Combinations e Permutations (ambos não repetem os valores).

Product --> Combinações possíveis (a ordem importa e repete os valores).
"""

from itertools import combinations

pessoas = ['Allan', 'Martha', 'Allany', 'Kaline', 'Jacinto', 'Gabriel']

for grupo in combinations(pessoas, 3):
    print(grupo)
