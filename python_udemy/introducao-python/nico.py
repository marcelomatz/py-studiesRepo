racao = 12.000
qtd_diaria = 0.140
dias_do_ano = 365
custo = 195.00

qtd_refeicoes = racao / qtd_diaria

refeicoes = qtd_refeicoes

custo_refeicoes = custo / qtd_refeicoes
print()
print(f'Um pacote de ração possui {racao:.2f} kg')
print(f'O Nico come diariamente {qtd_diaria:.2f} Kg')

print(
    f'O custo por refeição do Nico Bulldoguinho é de R$ {custo_refeicoes:.2f}')

print()


porcentagem = refeicoes / dias_do_ano * 100

print(f'Um saco de 12kg de ração dura {porcentagem:.2f}% do período de ano!')

print()
