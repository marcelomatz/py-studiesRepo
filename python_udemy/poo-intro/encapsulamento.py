"""
Serve para esconder algumas partes do código para proteger métodos e classes
public
_protected
__private

no python existe apenas uma convenção que se vc usar um encapsulamento, ele deve ser respeitado no código. Todos são adultos e vacinados e sabem o que não deve ser feito dentro de uma classe.
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Marcelo')
bd.inserir_cliente(2, 'Nico')
bd.inserir_cliente(3, 'Gabi')
bd.lista_clientes()
print(bd.dados)
# print('#############################3')

# bd.lista_clientes()
