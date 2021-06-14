# from types import GeneratorType

# variavel = ((x, y) for x, y in zip('Ali', 'Alo'))
# print(isinstance(variavel, GeneratorType))

"""
count - Itertools
"""
from itertools import count

contador = count(start=5, step=1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break
