chaves = range(1, 4)
podium = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto',
          'Quinto', 'Sexto', 'Sétimo', 'Oitavo', 'Nono', 'Décimo', 'Próximo']
podium[0] = 'Marcelo'
podium[1] = 'Nico'
podium[2] = 'Gabi'
print(list(zip(chaves, podium)))
