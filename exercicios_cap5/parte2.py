import pandas as pd
import numpy

#questão 6
numpy.random.seed(10)

df = pd.DataFrame(data=numpy.random.randint(1, 50, [5,4]),
                  index=['A', 'B', 'C', 'D', 'E'],
                  columns=['W', 'X', 'Y', 'Z'])

print(df['X'][df['X'] < 30].mean())

#questão 7
print(df.loc['D'].mean())
print(df.iloc[4].sum())

#questão 8
print(df.loc[['A', 'C', 'E'],['X', 'Y']])
print(df.loc[['A', 'C', 'E'],['X', 'Y']].sum(axis=1))
print(df.loc[['A', 'C', 'E'],['X', 'Y']].sum(axis=0))