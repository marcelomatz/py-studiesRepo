# Método é uma função que pertence à uma classe
# Quando uma função está dentro de uma classe ela é um [método] desta classe
from datetime import date, datetime
from random import randint


class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer enquanto estiver falando')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto estiver comendo!')
            return

        if self.falando:
            print(
                f'{self.nome} não consegue falar sobre dois assuntos ao mesmo tempo')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} já está calado!')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
