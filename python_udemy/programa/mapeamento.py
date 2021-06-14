from dados import produtos, pessoas, lista
# print(lista)
# print()

# nova_lista = map(lambda x: x * 2, lista)
# print(list(nova_lista))

# nova_lista = [x * 2 for x in lista]
# print(nova_lista)

# for produto in produtos:
#     print(produto)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)
