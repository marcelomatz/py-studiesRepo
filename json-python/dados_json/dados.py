"""
https://exchangeratesapi.io/
https://api.exchangeratesapi.io/latest
"""

clientes_dicionario = {
    1: {
        'nome': 'Marcelo Matzembacher',
        'sobrenome': 'Coelho',
        'idade': 37,
        'altura': 1.77,
        'peso': 80.00,
    },
    2: {
        'nome': 'Nico',
        'sobrenome': 'Bulldoguinho',
        'idade': 2,
        'altura': 0.30,
        'peso': 9,
    },
    3: {
        'nome': 'Gabriela',
        'sobrenome': 'Xavier',
        'idade': 35,
        'altura': 1.65,
        'peso': 65,
    },
}

clientes_json = """
{
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobrenome": "Miranda",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}
"""
