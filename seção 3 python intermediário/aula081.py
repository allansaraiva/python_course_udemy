"""
Reduce
"""
from aula079 import *
from functools import reduce

soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(soma_precos)
