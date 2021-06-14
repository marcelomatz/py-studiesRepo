from typing import final


try:
    a = {}
    print(a[1])
except NameError as erro:
    print('A variável que você está usando não foi declarada:', erro)

except (IndexError, KeyError) as erro:
    print('O índice ou chave que você buscou não existe:', erro)

except Exception as erro:
    print('Ocorreu um erro inesperado.')

else:
    print('Código executado com sucesso :)')

finally:
    print('O software está funcionando.')

print('continua')
