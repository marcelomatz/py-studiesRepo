"""
Função anônima - Lambda
"""
# def a(x, y): return x * y


# print(a(2, 2))

lista = [
    ['P1', 16],
    ['P2', 15],
    ['P3', 14],
    ['P4', 13],
    ['P5', 12]
]


# def separador(item):
#     return item[1]


#lista.sort(key=lambda separador: separador[1], reverse=True)
# print(lista)
print(sorted(lista, key=lambda i: i[1], reverse=True))
