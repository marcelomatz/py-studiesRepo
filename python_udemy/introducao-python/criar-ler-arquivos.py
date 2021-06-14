# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha Nova AQUI\n')
#     file.write('Linha Nova AQUI 2\n')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# with open('abc.txt', 'w+') as file:
#     #     file.write('Linha 1\n')
#     #     file.write('Linha 2\n')
#     #     file.write('Linha 3\n')

#     file.seek(0, 0)
#     print(file.read())

# with open('abc.txt', 'a+') as file:
#     file.write('Outra linha\n')
#     file.seek()
#     print(file.read())

import os

os.remove('abc.txt')
