n = int(input('Quantas pessoas deseja cadastrar? '))

pessoas =[]

for i in range(n):
    nome = input('Qual o seu nome? ')
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo (M/F)? ').strip().upper()
    pessoas.append({'Nome': nome, 'Idade': idade, 'Sexo': sexo})

soma = sum(pessoa['Idade'] for pessoa in pessoas)
media = soma / n

n_mulheres = 0

for pessoa in pessoas:
    if pessoa['Idade'] <= 20 and pessoa['Sexo'] == 'F':
        n_mulheres += 1

print(media)
print(n_mulheres)