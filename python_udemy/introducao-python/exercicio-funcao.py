"""
1 - Criar uma função que exibe uma saudação com os parâmetros saudação e nome.

2 - Criar uma função que receba 3 números como parâmetros e exiba a soma entre eles.

3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex: 10%). Retorne o valor do primeiro número somado do aumento do percentual do mesmo.

4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne Fizz, se o parâmetro da função for divisível por 5, retorne Buzz. Se o parâmetro for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""

# 1


# def um(msg, nome):
#     return f'{msg} {nome}'


# v1 = um('Olá,', 'Marcelo')
# print(v1, type(v1))

# # 2


# def dois(n1, n2, n3):
#     return n1 + n2 + n3


# v2 = dois(2, 2, 2)
# print(v2, type(v2))

# 3


# def aumento_percentual(valor, percentual):
#     return valor + (valor * percentual / 100)


# ap = aumento_percentual(100, 100)
# print('R$', ap)

# 4


from random import randint


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'bizz, {n} é divisível por 3'
    return n


for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
