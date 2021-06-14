from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 15000)
p3 = Produto('Caneca', 20)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)
carrinho.lista_produtos()
print(carrinho.soma_total())
carrinho.remove_produto(p3)
carrinho.remove_produto(p2)
carrinho.lista_produtos()
print(carrinho.soma_total())
