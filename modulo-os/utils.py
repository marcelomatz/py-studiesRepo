def formata_tamanho(tamanho):
    zero = 0
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho <= zero:
        tamanho = zero
        texto = 'ARQUIVO VAZIO'
    elif tamanho < kilo:
        tamanho = tamanho
        texto = 'bytes'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'Kb'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'Mb'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'Gb'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2)
    if tamanho > 0:
        return f'{tamanho}{texto}'.replace('.', ',')
    else:
        return f'{texto}'
