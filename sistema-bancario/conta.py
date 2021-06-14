"""
Conjunto de classes para gerenciamento da Conta

Composto por:
Uma Classe abstrata (Conta)
Uma Classe (ContaCorrente) que herda os métodos da Classe Conta e gerencia um [Limite] no método de inicialização
Uma Classe (ContaPoupanca) que herda os métodos da Classe Conta.

Este é apenas um exemplo criado para entendimento sobre criação de classes abstratas e herança, fazendo um polimorfismo nos métodos das classes que herdam a Super.
"""

from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(
            f'Agência: {self.agencia} \n Conta: {self.conta} \n Saldo: {self.saldo}\n')

    @abstractclassmethod
    def sacar(self, valor): pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
