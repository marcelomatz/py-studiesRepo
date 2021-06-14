perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '0',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2 + 3? ',
        'respostas': {
            'a': '1',
            'b': '5',
            'c': '0',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2 + 4? ',
        'respostas': {
            'a': '1',
            'b': '6',
            'c': '0',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 3 * 7? ',
        'respostas': {
            'a': '21',
            'b': '16',
            'c': '44',
        },
        'resposta_certa': 'b',
    },
}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha uma das opções abaixo: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite uma alternativa como resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('ACERTOU!!')
        respostas_certas += 1
    else:
        print('IXI, errou!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
