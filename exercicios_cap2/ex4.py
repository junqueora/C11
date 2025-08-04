distancia = float(input("digite a distância em km até o destino: "))

if distancia < 200:
    print(f"o valor da passagem é R$ {distancia * 0.5}")
else:
    print(f"o valor da passagem é R$ {distancia * 0.45}")