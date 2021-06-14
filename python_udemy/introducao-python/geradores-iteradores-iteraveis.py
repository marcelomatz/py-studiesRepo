import sys
import time


def gera():
    for n in range(1000):
        yield n
        # time.sleep(0.1)


g = gera()

# for v in g:
#     print(v)

# print(hasattr(g, '__iter__'))
# print(hasattr(g, '__next__'))


# melhor forma de criar um gerador é usando a list comprehension porém mudando os colchetes por parênteses

l1 = [x for x in g]
l2 = (x for x in g)

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
print(type(l1))
print(type(l2))
