def func(*args, **kwargs):
    print(args, kwargs, type(kwargs))

    idade = kwargs.get('idade')
    print(type(idade))
    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]


func(*lista, *lista2, nome='Marcelo', sobrenome='Matzembacher', idade='37')
