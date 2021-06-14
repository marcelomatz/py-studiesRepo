from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca
help(Banco)
banco = Banco()

cliente1 = Cliente('Marcelo', 37)
cliente2 = Cliente('Gabi', 35)
cliente3 = Cliente('Nico', 2)


conta1 = ContaPoupanca(1111, 123, 0)
conta2 = ContaCorrente(2222, 456, 0)
conta3 = ContaPoupanca(1212, 789, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)


# cliente1.conta.depositar(100)
# cliente2.conta.depositar(200)
# cliente3.conta.depositar(200)

# cliente1.conta.sacar(10)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(100)
else:
    print('Cliente não autorizado')
print('$$$$$$$$$$$$$$$$$$$$')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(100)
else:
    print('Cliente não autorizado')
