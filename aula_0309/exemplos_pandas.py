import pandas as pd
import numpy

#pode haver series (1d) e dataframes (2d+)

#pandas series (você pode passar os índices)
indexes = ['a', 'b', 'c']
valores = [10, 20, 30]

series = pd.Series(index=indexes, data=valores) #trabalha como dicionário (chave, valor)
print(series)

dic1 = {'a': 10, 'b': 20, 'c': 30} #você pode passar um dicionário direto
series1 = pd.Series(dic1)
print(series1)
print(series1['a']) #como um dicionário, você chama o elemento pela chave

dic2 = {'a': 10, 'b': 20, 'd': 40}
series2 = pd.Series(dic2)
print(series2)

#operações entre series (as operações concatenam e realizam as operações entre quem possui as mesmas chaves)
print(series1 + series2)
print(series1 - series2)
print(series1.add(series2, fill_value=0)) #para operar e tratar quem não compatível como zero, use essa função

#condicionais no pandas (iguais numpy)
print(series1[series1 <= 20])

#pandas dataframes (como se fossem planilhas, pode identificar a coluna)
numpy.random.seed(10)

#criando dataframe
df = pd.DataFrame(data=numpy.random.randint(1, 50, [5,4]),
                  index=['A', 'B', 'C', 'D', 'E'],
                  columns=['W', 'X', 'Y', 'Z'])
print(df) #slice funciona diferente
print(df[['W', 'Y']]) #tudo nas colunas W e Y
print(df.head(1)) #retorna n primeiras linhas
print(df.tail(1)) #retorna n últimas linhas

#silcing
print(df.iloc[0:2, :]) #iloc para fatiar com índices numéricos
print(df.iloc[1:, 3])

print(df.loc[['A', 'B'],['W', 'Y']]) #loc para usar as chaves

