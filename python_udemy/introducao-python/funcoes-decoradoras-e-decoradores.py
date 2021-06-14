def master(funcao):
    def slave(*args, **kwargs):
        print('Agora sou uma função decorada')
        funcao(*args, **kwargs)
    return slave


@master  # isso é um decorador - neste caso ele referencia a função master que é uma função decoradora
def fala_oi():
    print('Oi')


def outra_funcao(msg):
    print(msg)


outra_funcao('Teste')
