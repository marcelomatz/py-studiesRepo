def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'José'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Pedro', 'Jonas'])
clientes3 = lista_de_clientes(['Zico'])


print(clientes1)
print(clientes2)
print(clientes3)
