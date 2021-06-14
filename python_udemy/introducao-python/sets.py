s1 = {1, 2, 3, 4, 5}

#print(s1, type(s1))

s2 = set()
s2.add(1)
s2.add(2)
s2.discard(2)

#print(s2, type(s2))

l1 = [1, 2, 3, 4, 5, 1, 2, 1, 1, 2, 3, 3, 4]
l1 = set(l1)
l1 = list(l1)

# print(l1)

s3 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3, 4, 5, 6}
# s5 = s3 | s4 # union - pode usar o PIPE para unir 2 sets

# s5 = s3 & s4  # intersection & - somente os itens que estão nas duas listas
# print(s5)


s6 = s4 - s3  # o elemento apenas no set da esquerda
print(s6)

s7 = {1, 2, 3, 4, 5}
s8 = {2, 4, 5, 6, 7}
s9 = s7 ^ s8  # elementos que estão nos 2 sets mas não em ambos
print(s9)
