nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Goku'} #os conjuntos não permitem duplicação
print(nomes)
nomes.add('Bulma') #em conjuntos a adição é por add
nomes.remove('Vegeta') #como é uma lista com hash, não temos garantia do índice, então a remoção é pelo valor
a = {2, 4, 6}
b = {1, 4, 5}
x = a | b #união
y = a - b #diferença
z = a & b #interseção
print(type(z)) #fala se é tupla, lista, conjunto ou dicionário