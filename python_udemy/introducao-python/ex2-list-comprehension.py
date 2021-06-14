string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

n = 10

contadores = [i for i in range(0, len(string), n)]
print(contadores)
print()

tuplas = [(i, i + n) for i in range(0, len(string), n)]
print(tuplas)
print()

lista = [string[i:i + n] for i in range(0, len(string), n)]

mascarado = '.'.join(lista)
print(lista)
print()
print(mascarado)
print()
