lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)
print()
print('# OU USANDO UM JEITO MAIS SIMPLES \t dict \t PORÉM SEM ALGUNS RECURSOS DE USAR OUTRAS FUNÇÕES NATIVAS')
print()
d1 = dict(lista)
print(d1)


# Usando enumerate para criar uma chave - meio sem utilidade porém prático para relembrar enumerate

d2 = {x: y for x, y in enumerate(range(21))}
print(d2)


d3 = {f'chave_{x}': x * 2 for x in range(15)}
print(d3)
