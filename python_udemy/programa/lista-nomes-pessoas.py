from dados import pessoas

print(pessoas)


def aumenta_idade(p):
    p['idade_aumentada'] = round(p['idade'] * 1.20)
    return p


pessoa_nome = map(aumenta_idade, pessoas)

for pessoa in pessoa_nome:
    print(pessoa)
