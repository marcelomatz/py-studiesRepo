import vendas.calc_preco
from vendas.formata import preco as formata

preco = 49.90
preco_com_aumento = vendas.calc_preco.aumento(preco, 15, formata=True)
print(preco_com_aumento)


preco_com_reducao = vendas.calc_preco.reducao(preco, 15, formata=True)
print(preco_com_reducao)


print(formata.real(150))
