import re


class Produto:
    def __init__(self, nome, preco, *args):
        self.nome = nome
        self.preco = preco
        self.args = args

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            # este replace deveria ser substituído por um regex
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('camiseta', 50)
# p1.desconto(10)
print(p1.preco)
print(p1.nome)

p2 = Produto('caneca', 'R$15')
# p2.desconto(10)
print(p2.preco)
print(p2.nome)
