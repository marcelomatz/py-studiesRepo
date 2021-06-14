from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'B'},
    {'nome': 'Silvia', 'nota': 'C'},
    {'nome': 'Carol', 'nota': 'D'},
    {'nome': 'Vanessa', 'nota': 'A'},
    {'nome': 'Bia', 'nota': 'B'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Kléber', 'nota': 'D'},
    {'nome': 'Rosana', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'Frank', 'nota': 'C'},
    {'nome': 'Tomy', 'nota': 'A'},
    {'nome': 'Caio', 'nota': 'B'},
    {'nome': 'Anderson', 'nota': 'D'},
]
def ordena(item): return item['nota']


alunos.sort(key=ordena)
alunos_agupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agupados:
    va1, va2 = tee(valores_agrupados)

    quantidade = len(list(va2))
    print(f'{quantidade} alunos com a nota {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')
    print()
