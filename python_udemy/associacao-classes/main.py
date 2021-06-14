from classes import Caneta, MaquinaDeEscrever
from classes import Escritor


escritor = Escritor('Marcelo')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()
