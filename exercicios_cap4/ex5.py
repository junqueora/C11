import numpy

numpy.random.seed(10)
mtz = numpy.random.randint(1, 51, 16).reshape(4, 4)

print(f"Média das linhas {mtz.mean(axis=1)}")
print(f"Média das linhas {mtz.mean(axis=0)}")

print(f"Maior valor da média das linhas {mtz.mean(axis=1).max()}")
print(f"Maior valor da média das colunas {mtz.mean(axis=0).max()}")

print(f"Cada número da matriz e quantas vezes se repete {numpy.unique(mtz, return_counts=True)}")

valores, repeticoes = numpy.unique(mtz, return_counts=True)

print(f"Valores que se repetem {valores[repeticoes == 2]}")