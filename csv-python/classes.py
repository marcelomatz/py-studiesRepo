import csv


class AbreArquivo:

    def __init__(self, arquivo):
        self._arquivo = arquivo

    @property
    def arquivo(self):
        return self._arquivo

    def abre_arquivo(self):
        self.arquivo = arquivo
        with open(arquivo, 'r') as arquivo:
            self.dados = csv.DictReader(arquivo)
            for self.dado in self.dados:
                nome = dado['nome']
                sobrenome = dado['sobrenome']
                email = dado['email']
                telefone = dado['telefone']
                print(
                    f'NOME: {nome}\n SOBRENOME: {sobrenome}\n EMAIL: {email}\n TELEFONE: {telefone}\n ')
                return abre_arquivo()
