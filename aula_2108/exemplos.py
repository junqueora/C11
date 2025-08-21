import numpy

#slicing (fatiamento) de conjunto de dados

mtz = numpy.arange(1, 10, 1).reshape(3, 3)
print(mtz)

print(mtz[2]) #extraindo apenas a terceira linha
print(mtz[:, 1]) #extraindo apenas a segunda coluna
print(mtz[:, 1:]) #extraindo da segunda coluna para frente

#condicionais no numpy array

print(mtz > 5) #retorna uma matriz com false para quem não atende e true para quem atende
print(mtz[mtz > 5]) #retorna só os elementos que atendem
print(mtz[mtz % 2 == 0]) #retorna só os pares

#quando a chamada mtz[condicao logica] vai retornar os elementos que retornam true

#tratamento textual

arr = numpy.array(['Goku', 'Goten', 'Gohan', 'Trunks', 'Bulma'])
print(numpy.char.find(arr, 'Go')) #retorna um vetor com a posição em que o "Go" aparece em cada string
