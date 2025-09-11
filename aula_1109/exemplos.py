import pandas as pd
import numpy

ds = pd.read_csv('paises.csv', delimiter=';')
print(ds.columns) #para ver as colunas (chaves)
print(ds.head(2)) #para ver os dois primeiros registros (linhas)
print(ds.tail(2)) #para ver os dois últimos registros

#adicionar nova coluna (% da população em relação ao mundo)
soma_populacao = numpy.sum(ds['Population']) #calculando a soma da população mundial (pode ser ds['Population'].sum())
print(soma_populacao)
population_percent = ds['Population'] / soma_populacao
print(population_percent)

#ds['Population Percentage'] = population_percent * 100 #adicionando coluna (no final
#print(ds)
ds.insert(3, 'Population Percentage', population_percent * 100) #adicionando coluna em um local específico
print(ds)

ds.to_csv('paises2.csv', sep=';') #criando novo dataset csv

#group by
group_region = ds.groupby('Region')
print(group_region.count()['Country']) #conta o número de países em cada região
print(group_region.sum()['Country']) #lança os países de cada região (não soma porque não tem como somar strings)
print(group_region.sum()['Population']) #soma a população de cada região

# funções no python
def ten_percent(x): #função que tira 10% de algo
    return x*0.9

original_deathrate = ds['Deathrate']
deathrate = original_deathrate.apply(ten_percent) #ao invés de chamar a função, usa o apply
print(deathrate)

df = pd.concat([original_deathrate, deathrate], axis=1)
print(df)
