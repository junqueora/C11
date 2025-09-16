import pandas as pd
import numpy

df = pd.read_csv('paises.csv', delimiter=';')

#questão 1
df_region = df['Region'].str.strip()
df_country = df['Country'].str.strip()

print(df_country[df_region == 'OCEANIA'])
print(df_region[df_region == 'OCEANIA'].size)

#questão 2
df_population = df['Population']

print(df_country[df_population.argmax()], df_region[df_population.argmax()])

#questão 3
group_region = df.groupby('Region')

print(group_region['Literacy (%)'].mean())

#questão 4
df_coastline = df['Coastline (coast/area ratio)']

df_country[df_coastline == 0].to_csv('noCoast.csv', index=False, sep=';', header=False)

#questão 5
def need_help(deathrate):
    if deathrate >= 9:
        return 'Urgent'
    else:
        return 'Balanced'

df_deathrate = df['Deathrate']
df['Humanitarian Help'] = df_deathrate.apply(need_help)

print(df)