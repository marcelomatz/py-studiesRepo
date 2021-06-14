print('Olá. Este é o jogo do AMOR')
nome = input('Qual o seu nome? ')
print(f'Olá {nome} :)')
pessoa = input('Quem você quer que ame você? ')
print(f'Vamos lá que {pessoa} vai amar você quantas vezes você quiser.')

amor = 0

qtd_vezes = input(f'Quantas vezes você deseja receber o amor de {pessoa}? ')
qtd_vezes = int(qtd_vezes)

if qtd_vezes == 0:
    print(f'Você não deseja o amor de {pessoa}')

while amor < qtd_vezes:
    print(f'{pessoa} TE AMA')
    amor += 1

    if amor == qtd_vezes:
        print(
            f'Você pediu que {pessoa} te amasse {qtd_vezes}X e {pessoa} te amou {qtd_vezes}X')
print('##########')
print('FIM DE JOGO')
