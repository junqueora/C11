pessoa1 = {
            'Nome' : 'Goku',
            'Idade' : 43,
            'Sexo' : 'Masculino'
            } #trabalha com chave e valor
print(pessoa1)
pessoa1['Poder'] = 8000 #é possível adicionar novas chaves
pessoa2 = {
            'Nome' : 'Gohan',
            'Idade' : 23,
            'Sexo' : 'Masculino'
            }
pessoa3 = {
            'Nome' : 'Pan',
            'Idade' : 5,
            'Sexo' : 'Feminino'
            }
dbz = [pessoa1, pessoa2, pessoa3] #aninhamento de listas com dicionários
print(dbz[0])
pessoa1['Filhos'] = ['Gohan', 'Goten']
print(pessoa1)
print(dbz)
print(pessoa1['Filhos'][1]) #acessando o goten