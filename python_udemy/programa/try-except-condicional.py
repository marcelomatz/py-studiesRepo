def conver_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass  # quando não retornar um INT ou FLOAT vai retornar None e aí eu do um pass e trato na condicional if else


while True:
    numero = conver_numero(input('Digite um número: '))

    if numero is not None:
        print(numero * 2)
    else:
        print('\t Isso não é um número')
