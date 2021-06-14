import os
from utils import formata_tamanho

caminho_procura = '/home/ruivo/Development/Buscar/'
termo = ''

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o arquivo ', arquivo)
                print('Caminho ', caminho_completo)
                print('Nome', nome_arquivo)
                print('Extensão ', ext_arquivo)
                print('Tamanho (em bytes)', tamanho_arquivo)
                print('Tamanho do arquivo ', formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido:', e)

print()
print(f'{conta} arquivo(s) encontrado(s)')
