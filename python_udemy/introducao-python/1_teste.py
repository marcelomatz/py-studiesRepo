texto = 'Quando ele chegou ela logo falou que ele estava demitido e todos ficaram estarrecidos, apesar de todas as diferenças eles jamais imaginaram aquilo.'


def remove_genero(y, z):
    novo_texto = texto
    for item in texto:
        return novo_texto.replace(y, z)


listinha = ['ele', 'ela']
for item in listinha:
    print(item)
x = item
p1 = remove_genero(x)

print(p1)
