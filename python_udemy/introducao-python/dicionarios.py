"""
Dicionário é uma estrutura de dados que suporta dados em par como chave e valor
"""
# dicionario = {'chave': 'valor da chave'}
# dicionario['nova_chave'] = 'Valor da Nova Chave'
# print(dicionario, type(dicionario))
# print(dicionario['chave'])
# print(dicionario['nova_chave'])


from typing import Tuple


d1 = {
    'chave1': 'valor da chave 1',
    'chave2': 'valor da chave 2',
    'chave3': 'valor da chave 3'
}

for k, v in d1.items():
    print(k, v)

# d1['chave1'] = 'valor da chave 1 ATUALIZADO'

# d1['chave4'] = 'valor da chave 4'

# d1.update({'chave2': 'valor da chave 2 ATUALIZADO'})

# # print(d1.get('chave1'))

# if d1.get('chave1') is not None:
#     print(d1.get('chave1'))

# del d1['chave4']

# print('chave1' in d1)
# print('chave1' in d1.keys())
# print('chave1' in d1.values())


# if d1.get('chave3') is not None:
#     d1.update({'chave4': 'valor da chave 4 RENASCEU'})


# print(len(d1))

# for v in d1.values():
#     print(v)


# d1['naoexiste'] = 'Agora existe!'

# if 'naoexiste' in d1:
#     print(d1)
