carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 40))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 150))


total = sum([float(y) for x, y in carrinho])
print(total)
