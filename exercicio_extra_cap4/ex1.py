import numpy

ds = numpy.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')
ds = numpy.char.strip(ds)

ds_resumido = ds[1:, 0:4]
print(ds_resumido)

ds_regions_unique = numpy.unique(ds_resumido[1:, 1])
print(ds_regions_unique)

ds_literacy = ds[1:, 9].astype(float)
print(f"A taxa de alfabetização global média é {ds_literacy.mean()}%")

ds_regions = ds[1:, 1]
print(f"Tem {ds_regions[ds_regions == 'NORTHERN AMERICA'].size} países da américa do norte")

ds_gdp = ds[1:, 8].astype(float)
ds_countries = ds[1:, 0]
print(f"O país com o maior PIB na Ámerica do Sul é {ds_countries[ds_regions == 'LATIN AMER. & CARIB'][ds_gdp[ds_regions == 'LATIN AMER. & CARIB'].argmax()]}")