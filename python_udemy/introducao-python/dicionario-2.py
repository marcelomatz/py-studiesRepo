clientes = {
    '000001': {
        'nome': 'Marcelo',
        'sobrenome': 'Matzembacher'
    },
    '000002': {
        'nome': 'Nico',
        'sobrenome': 'Bulldoguinho'
    },
    '000003': {
        'nome': 'Gabi',
        'sobrenome': 'Antunes'
    },
}

for clientes_chave, clientes_valor in clientes.items():
    print(f'ID {clientes_chave}')
    for dados_chave, dados_valor in clientes_valor.items():
        print(f'\t{dados_chave} = {dados_valor}')
