#importando a biblioteca numpy
import numpy

arr = numpy.array([1,2,3]) #se colocar uma única string ele converte todos em string
#numpy é uma biblioteca de base C, por isso não permite dupla tipagem

print(arr)
print(type(arr))

mtz = numpy.array([[1,2,3],[4,5,6]])
print(mtz)
#a matriz da mesma maneira que em outras linguagens é uma lista de listas

#funções para estruturar numpy arrays
#array 1d de só 1
arr1 = numpy.ones(3)
print(arr1)
#array 2d (matriz) só de zeros
mtz1 = numpy.zeros(10).reshape(2,5) #reshape só funciona se a matriz for convertível 10*1 = 2*5
print(mtz1)

mtz2 = numpy.zeros([3,3]) #sem precisar usar o reshape
print(mtz2)

arr2 = numpy.arange(10,31,2) #criando um array 1d que vai de 10 a 30 a cada 2
print(arr2)

#operações com numpy arrays
print(arr2.min(), arr2.max(), arr2.mean()) #funções para retornar valor min, max e média
print(arr2.argmin()) #função que retorna o índice do menor valor
print(arr2.sum()) #função que retorna a soma dos elementos

#operações aritméticas (apenas com arrays de mesmo tamanho)
arr3 = numpy.arange(1,10,1)
arr4 = numpy.arange(9,0,-1)
print(arr3)
print(arr4)
print(arr3 + arr4)
print(arr3 - arr4)
print(3 * arr3)

print(numpy.concatenate([arr3,arr4])) #função de concatenar arrays
mtz3 = numpy.array([50,10,100,60,25,100,75,80,100]).reshape(3,3)
print(mtz3)
#a função .T retorna a transposta
print(mtz3.sum(axis=1)) #axis 1 retorna a soma das linhas e axis 0 retorna as colunas
print(mtz3.sum(axis=1)[0]) #[0] faz o retorno ser o da primeira linha

#para gerar o mesmo número aleatório em diferentes máquinas use seed (semente aleatória)
numpy.random.seed(10)
arr5 = numpy.random.randint(1,101,9) #para gerar um vetor de ints aleatórios
print(arr5)

arr6 = numpy.random.randint(1,11,10)
print(arr6)
print(numpy.unique(arr6)) #a função unique retorna os elementos únicos e os ordena
print(numpy.unique(arr6, return_counts=True)) #essa função retorna quantas repetições de cada elementos
#o retorno acima é uma tupla com uma comparação