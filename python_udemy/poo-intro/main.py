from pessoa import Pessoa
from produto import Produto


# Quando eu estou instanciando uma classe, eu estou criando um objeto
p1 = Pessoa('Marcelo', 37)
p2 = Pessoa('Gabi', 35)
p3 = Pessoa.por_ano_nascimento('Bulldoguinho', 2000)
print(p3.nome, p3.idade)
print(p3.idade)
print(p1.gera_id())
print(Pessoa.gera_id())

produto_novo = Produto('tênis', 100, 'info', Pessoa.gera_id())
print(produto_novo.nome, produto_novo.preco, produto_novo.args)
print(type(produto_novo.args))
print(produto_novo.kwargs)
