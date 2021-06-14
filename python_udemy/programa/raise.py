def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(f'Houve um erro no seu software: {error}')
        raise


try:
    print(divide(2, 0))
except:
    print('Houve um erro no seu software')
