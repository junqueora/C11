import numpy

ds = numpy.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

ds_mission_status = ds[1:, 7]
print(f"Taxa de sucesso nas missões: {(numpy.count_nonzero(ds_mission_status == 'Success') / ds_mission_status.size) * 100}%")

ds_cost = ds[1:, 6].astype(float)
print(f"Custo médio das missões com valores divulgados: U$ {ds_cost[ds_cost != 0].mean()} M")

ds_location = ds[1:, 2]
print(f"Número de missões realizadas pelos EUA: {numpy.count_nonzero(ds_location[numpy.char.find(ds_location, 'USA') >= 0])}")

ds_company = ds[1:, 1]
print(f"Valor da missão mais cara da SpaceX: U$ {ds_cost[ds_company == 'SpaceX'].max()} M")

companies, n_missions = numpy.unique(ds_company, return_counts=True)
for i in range(companies.size):
    print(f"Empresa: {companies[i]}, Número de missões: {n_missions[i]}")