import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Marcelo', 'Matzembacher']}
v = copy.deepcopy(d1)

v[1] = 'Nico'
v['d'][0] = 'Ruivo'

print(d1)
print(v)

d1.popitem()
print(d1)


d2 = {
    'nome': 'Marcelo',
    'sobrenome': 'Matzembacher'
}

d3 = {
    'idade': 37,
    'sexo': 'Masculino',
    'admin': True
}

d2.update(d3)
print(d2, type(d2))
