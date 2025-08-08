pessoas = []

for i in range(3):
    nome = input('Qual o seu nome? ')
    peso = int(input('Qual seu peso? '))
    pessoas.append({'Nome': nome, 'Peso': peso})

pesado = max(pessoas, key=lambda x: x['Peso'])
leve = min(pessoas, key=lambda x: x['Peso'])

print(pesado['Nome'])
print(leve['Nome'])