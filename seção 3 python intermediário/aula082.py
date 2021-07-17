"""
Try, Except - Tratando Exceções em Python
"""

try:
    a = []
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor.')
except (KeyError, IndexError) as erro:
    print('Erro do índice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Código executado.')
finally:
    print('FIM.')
