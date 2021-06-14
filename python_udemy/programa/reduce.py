from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
media = round(soma_precos / float(len(produtos)), 2)
print(f'A média de preços dos produtos é {media}')


soma_idades = reduce(lambda acumulador, i: i['idade'] + acumulador, pessoas, 0)
print(f'A soma das idades é {soma_idades}')
media = round(soma_idades / len(pessoas))
print(f'A média das idades é {media}')
