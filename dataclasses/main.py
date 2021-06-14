from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Invalid type {type(self.nome).__name__} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Marcelo', 'Matzembacher')
p2 = Pessoa('Marcelo', '')

if __name__ == '__main__':
    print(p1)
    print(p1.nome)
    print(p1.sobrenome)
    print(p1.nome_completo)

    print(p2.nome)
    print(p2.sobrenome)
    print(p2.nome_completo)

    print(asdict(p1))
    print(astuple(p1))
