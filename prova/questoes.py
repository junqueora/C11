import numpy

ds = numpy.loadtxt('shopping_trends.csv', delimiter=',', dtype=str)
ds = numpy.char.strip(ds)

#questão 1
ds_age = ds[1:, 1].astype(float)
ds_gender = ds[1:, 2]

print(f"Q1: A média de idade dos homens é de {ds_age[ds_gender == "Male"].mean().round(2)} anos")

#questão 2
ds_amounts = ds[1:, 5].astype(float)

print(f"Q2: {ds_amounts[ds_amounts > ds_amounts.mean()].size} clientes gastaram mais que a média")

#questão 3
ds_item = ds[1:, 3]
item, n_purchases = numpy.unique(ds_item, return_counts=True)

print(f"Q3: O item menos vendido da loja representa {(ds_item[ds_item == item[n_purchases.argmin()]].size / ds_item.size) * 100}% das vendas")

#questão 4
ds_discount = ds[1:, 13]

print(f"Q4: {(ds_discount[ds_discount == "Yes"].size / ds_discount.size) * 100}% das vendas tiveram desconto")

#questão 5
ds_color = ds[1:, 8]
ds_season = ds[1:, 9]
color, n_purchases = numpy.unique(ds_color[ds_season == "Summer"], return_counts=True)

print(f"Q5: A cor mais vendida no verão foi {color[n_purchases.argmax()]}") #deu certo!