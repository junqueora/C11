import numpy
import matplotlib.pyplot as plt
import pandas as pd

df_paises = pd.read_csv('paises.csv', delimiter=';')
df_space = pd.read_csv('space.csv', delimiter=';')

#questão 1
paises_na = df_paises[df_paises['Region'].str.strip() == 'NORTHERN AMERICA']

plt.plot(paises_na['Country'], paises_na['Deathrate'], 'o-r', linewidth=2, markersize=5, label='Mortalidade')
plt.plot(paises_na['Country'], paises_na['Birthrate'], 'o-g', linewidth=2, markersize=5, label='Natalidade')
plt.show()

#questão 2
usa_missions = df_space[df_space['Location'].str.contains('USA', na=False)]
n_usa_company = usa_missions['Company Name'].nunique()

china_missions = df_space[df_space['Location'].str.contains('China', na=False)]
n_china_company = china_missions['Company Name'].nunique()

plt.bar(['USA', 'China'], [n_usa_company, n_china_company], color=['b', 'r'])
plt.show()

#questão 3
roscosmos_missions = df_space[df_space['Company Name'] == 'Roscosmos']
success = roscosmos_missions[roscosmos_missions['Status Mission'] == 'Success']
failure = roscosmos_missions[roscosmos_missions['Status Mission'] == 'Failure']
partial_failure = roscosmos_missions[roscosmos_missions['Status Mission'] == 'Partial Failure']

plt.pie([len(success), len(failure), len(partial_failure)], labels=['Sucesso', 'Falha', 'Falha parcial'], autopct='%1.1f%%')
plt.show()