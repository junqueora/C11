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

arr = numpy.array(['Goku', 'Goten', 'Gohan', 'Trungoks', 'Bulma'])
print(arr)
print(numpy.char.find(arr, 'Go')) #retorna um vetor com a posição em que o "Go" aparece em cada string
print(numpy.char.find(arr, 'Go') >= 0) #retorna true para quem tem "Go"
print(arr[numpy.char.find(arr, 'Go') >= 0]) #retorna quem tem "Go" no nome

#fiz upload de um dataset
ds = numpy.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') #indicar separador (;), converte tudo para string e indica o encoding dos caracteres

#calculando a média do custo do dataset
ds_cost = ds[1:, 6].astype(float) #parsing para float da coluna dos custos
print(ds_cost)