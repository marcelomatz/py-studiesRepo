class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Algo de errado não está certo!')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
