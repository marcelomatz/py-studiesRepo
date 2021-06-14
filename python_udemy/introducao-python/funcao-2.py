# def funcao(var):
#     return var


# variavel = funcao('Valor que eu quero')
# print(variavel)
# if variavel:
#     print(variavel)
# else:
#     print('Nada a retornar')

# def divisao(n1, n2):
#     if n2 > 0:
#         return n1 / n2
#     else:
#         print('Não posso dividir um número por zero')


# divide = divisao(10, 2)

# if divide:
#     print(divide)

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(10, 2)

if divide:
    print(divide)
else:
    print('Conta inválida')
