from dados import produtos, pessoas, lista
# usando list-comprehension
#nova_lista = [x for x in lista if x > 5]

# usando filter
# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))


nova_lista = filter(lambda p: p['preco'] > 50, produtos)

for produto in nova_lista:
    print(produto)
