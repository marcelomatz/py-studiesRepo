import re


def just_numbers(just_number):
    return re.sub(r'[^0-9]', '', just_number)


cpf = 'marcelo'
cpf_tratado = just_numbers(cpf)
print(cpf_tratado)
