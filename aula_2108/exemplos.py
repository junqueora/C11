import numpy

#slicing (fatiamento) de conjunto de dados

mtz = numpy.arange(1, 10, 1).reshape(3, 3)
print(mtz)

print(mtz[2]) #extraindo apenas a terceira linha
print(mtz[:, 1]) #extraindo apenas a segunda coluna
