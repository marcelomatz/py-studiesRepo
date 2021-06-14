"""
O que difere Tuplas de Listas é que nas Tuplas não é possível:
 - alterar o valor das tuplas
 - alterar o índice
 - alterar porra nenhuma
"""
# t1 = 1, 2, 3, 'a', 'Marcelo Matzembacher'

# print(t1)

# t1 = (1, 2, 3, 4, 5)
# t2 = (6, 7, 8, 9, 10)
# t3 = t1 + t2
# print(t3, type(t3))

# UMA TUPLA NÃO ACEITA TER SEU VALOR MODIFICADO.
# t2 = (1, 2, 3, 4, 5)
# t2[1] = 5000
# print(t2)

t = (1, 2, 3, 4, 5)
t = list(t)
t[1] = 'Marcelo'
t = tuple(t)
print(t)
