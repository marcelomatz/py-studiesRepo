import os
import shutil

caminho_original = '/home/ruivo/Development/Buscar/'
caminho_novo = '/home/ruivo/Development/Buscar2/'

try:
    os.mkdir(caminho_novo)

except FileExistsError as e:
    print(
        f'INFO: O diretório de destino já existia em: {caminho_novo} e não precisou ser criado.')

finally:
    print('INFO: PROCESSO DE DIRETÓRIOS CONCLUÍDO COM SUCESSO!')


for raiz, diretorios, arquivos in os.walk(caminho_original):
    for file in arquivos:
        caminho_antigo_do_arquivo = os.path.join(raiz, file)
        caminho_novo_do_arquivo = os.path.join(caminho_novo, file)

        if '.mp4' in file:
            shutil.copy(caminho_antigo_do_arquivo, caminho_novo_do_arquivo)
            print(f'Arquivo {file} copiado com sucesso')
