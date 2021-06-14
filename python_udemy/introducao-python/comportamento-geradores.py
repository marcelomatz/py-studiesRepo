# lists, tuples, str -> Sequences -> Iterável
nome = 'Marcelo Matzembacher'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

for letra in gerador:
    print(letra)

# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     # print(next(iterador))
#     # print(next(iterador))
#     # print(next(iterador))
# except:
#     pass


# print('CADÊ AS LETRAS DO MEU FOR?')

# for letra in iterador:
#     print(letra)
