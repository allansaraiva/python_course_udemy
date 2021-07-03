"""
FOR / ELSE em Python
"""
# list_1 = ['eu', 'tu', 'ele', 'nós', 'vós', 'eles']
#
# for value in list_1:
#     if value.startswith('n'):  # startswith() - checa se começa com algo.
#         print(f'Começa com "n" {value}.')
#     else:
#         print(f'Não começa com "n" {value}')


list_1 = ['eu', 'tu', 'ele', 'nós', 'vós', 'eles']

starts_with_e = False
for value in list_1:
    if value.startswith('e'):
        starts_with_e = True

if starts_with_e:
    print(f'Existe uma palavra que começa com "e"')
else:
    print('Não existe uma palavra que começa com "e"')
