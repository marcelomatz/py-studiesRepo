"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos

Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

# pessoas = ['Marcelo', 'André', 'Ana', 'João', 'Larissa', 'Silvia']

# for grupo in product(pessoas, repeat=2):
#     print(grupo)


grupo_1 = ['Pessoa 1', 'Pessoa 2', 'Pessoa 3']
grupo_2 = ['Pessoa 4', 'Pessoa 5', 'Pessoa 6']
grupo_3 = ['Pessoa 7', 'Pessoa 8', 'Pessoa 9']

todos = grupo_1 + grupo_2 + grupo_3

for grupo in combinations(todos, 3):
    print(grupo)
