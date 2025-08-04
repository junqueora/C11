num = int(input("digite um número: "))
a = int(input("digite o início do intervalo da tabuada: "))
b = int(input("digite o final do intervalo da tabuada: "))

for i in range(a, b + 1):
    print(f"{num} x {i} = {num * i}")