class A:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Operação inválida.'
        else:
            self.__dict__[key] = value


a = A()
a.nome = 'Marcelo'
a.qualquer_coisa = 'ISSO PODE'
print(a.nome, a.qualquer_coisa)
