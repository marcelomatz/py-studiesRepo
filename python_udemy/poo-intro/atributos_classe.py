class A:
    vc = 123


a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
# posso invocar minha classe e imprimir os atributos de classe (que são variáveis de escopo da classe [e não das instâncias]) sem instanciar ela
print(A.vc)
