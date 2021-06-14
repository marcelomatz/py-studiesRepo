"""
Otimização
Escrever menos linhas de código
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(1, 11)]

l3 = ['Marcelo', 'Nico', 'Gabi']
ex4 = [v.replace('a', '@') for v in l3]
# print(ex4)
# print(l1)
# print(ex2)
# print(ex3)

l4 = list(range(100))
ex5 = [v for v in l4 if v % 2 == 0 if v % 8 == 0 if v % 16 == 0]
print(ex5)
