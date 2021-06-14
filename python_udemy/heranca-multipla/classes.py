class A:
    def falar(self):
        print('Falando de A')


class B(A):
    def falar(self):
        print('Falando de B')


class C(B):
    def ouvir(self):
        print('Ouvindo em C')


class D(B, C):
    pass


d = D()
d.falar()
d.ouvir()
