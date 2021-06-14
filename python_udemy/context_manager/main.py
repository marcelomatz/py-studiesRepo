"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()
        return True


with open('./context_manager/log.txt', 'w') as arquivo:
    arquivo.write('Texto Um\n')
    arquivo.write('TXT 2\n')
"""
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modulo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modulo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('./context_manager/log.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
