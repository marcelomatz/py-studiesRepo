"""
considerando duas listas de inteiros ou floats (lista A e listaB)
Some os valores na s listas retornando uma nova lista com os valores somados:

se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.
"""

from itertools import zip_longest
lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4]
# zip só une as listas até o tamanho da menor lista
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

# FORMAS ALTERNATIVAS DE RESOLVER ESSE PROBLEMAS
#lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)

# Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.
