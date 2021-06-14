from classes import Cliente

print('------------------------------------------------')
cliente1 = Cliente('Marcelo', 37)
cliente1.insere_endereco('Florianópolis', 'SC')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()
print('------------------------------------------------')
cliente2 = Cliente('Gabi', 35)
cliente2.insere_endereco('Belo Horizonte', 'MG')
cliente2.insere_endereco('Florianópolis', 'SC')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()
print('------------------------------------------------')
cliente3 = Cliente('Nico', 1)
cliente3.insere_endereco('Zona França de Manaus', 'MA')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print('------------------------------------------------')

print('#######################################################')
