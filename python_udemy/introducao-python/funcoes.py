"""
Funções - def em Python
"""
import random


def saudacao(msg='Olá,', usuario='Visitante. Faça seu cadastro para ter acesso à todo conteúdo.'):
    return f'{msg} {usuario}'


saudacoes = ['Olá', 'Hey', 'Oi']
saudacoes_index = random.choice(saudacoes)
usuario = 'Marcelo'

variavel = saudacao(saudacoes_index, usuario)
print(variavel)
