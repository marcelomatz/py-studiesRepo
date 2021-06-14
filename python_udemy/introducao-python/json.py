import json

d1 = {
    'Pessoa_1': {
        'nome': 'Marcelo',
        'idade': 37,
    },
    'Pessoa_2': {
        'nome': 'Gabi',
        'idade': 35,
    },
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)
