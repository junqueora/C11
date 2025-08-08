nome = input('Qual o seu nome? ')
media = int(input('Qual foi sua média? '))

registro = {'Nome': nome, 'Média': media}
if media < 50:
    registro['Situação'] = 'RP'
else:
    registro['Situação'] = 'AP'

print(registro)