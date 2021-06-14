"""
Escopo de variáveis no Python
"""

# GLOBAL
# variavel = 'valor'  # aqui a variável é global no documento


# def func():
#     print(variavel)


# def func2():
#     global variavel  # não é uma boa prática, porém é possível alterar o valor global de uma variável de dentro da função
#     variavel = 'Outro valor'  # essa variável existe somente dentro do escopo da função
#     print(variavel)


# func()
# func2()
# print(variavel)
# =============================

# Passando o valor de uma variável de dentro de uma função, para dentro de outra função.
# Cada função tem seu próprio escopo. Se eu tentar acessar o valor de uma variável criada em outra função, dentro da função atual, eu vou ter um erro pq ela não existe.

# nova_var = 'Novo Valor'


# def nova_func():
#     nova_var = 'Marcelo'
#     return nova_var


# def nova_func2(arg):
#     print(arg)


# nf = nova_func()
# print(nf)

# nova_func2(nova_var)
# nova_func2(nf)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{nome},{saudacao}'


nome = 'Marcelo'
executando = mestre(fala_oi, nome)
executando2 = mestre(saudacao, nome, saudacao='seja bem vind@x ao Portal.')
print(executando)
print(executando2)
