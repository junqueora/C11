import numpy
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('paises2.csv', delimiter=';')

#extraindo 6 maiores países em área (scatter)
maiores_areas = df.nlargest(6, 'Area (sq. mi.)')

print(maiores_areas['Country'])
plt.scatter(maiores_areas['Country'], maiores_areas['GDP ($ per capita)'], s=maiores_areas['Area (sq. mi.)'] / 100000, color='c') #scatter é gráfico de bolinha

plt.show()

#extraindo 5 maiores gdps (barplot)
maiores_gdps = df.nlargest(5, 'GDP ($ per capita)')

print(maiores_gdps['Country'])
plt.bar(maiores_gdps['Country'], maiores_gdps['GDP ($ per capita)'], width=0.2, color='b')

plt.show()

#extraindo países sem costa e com costa
no_coast = df[df['Coastline (coast/area ratio)'] == 0]
coast = df[df['Coastline (coast/area ratio)'] > 0]

qt_no_coast = len(no_coast)
qt_coast = len(coast)

print(no_coast['Country'])
plt.pie([qt_no_coast, qt_coast], labels=['Landlocked', 'Coastal'], autopct='%1.1f%%')

plt.show()