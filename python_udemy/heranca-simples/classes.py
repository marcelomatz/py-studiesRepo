class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):
        print('ESTOU EM CLIENTE')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')


class ClienteVIP(Cliente):
    def falar(self):
        super().falar()
        # Pessoa.falar(self)
        print(f'{self.nomeclasse} está falando')
