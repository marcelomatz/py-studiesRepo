"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
string = "O Brasil é o país do futebol, o Brasil é penta. Marcelo programador. Marcelo Matzembacher. Marcelo ama a Gabi"

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print('#######')
print(lista_2)

# for item in lista_1:
#     print(f'A palavra {item} apareceu {lista_1.count(item)}X na frase.')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}X)')
