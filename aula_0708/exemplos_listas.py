nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan'] #exemplo com listas, agora mutáveis (fecha em [])
print(nomes)
nomes.append('Bulma') #com o append, você coloca o elemento no final da lista
nomes.insert(1, 'Kuririn') #com o insert você insere em um index específico
del nomes[2] #deleta o elemento pelo index (pode ser nomes.pop(2))
nomes.remove('Gohan') #delete pelo valor, se existir
if 'Vegeta' in nomes:
    nomes.remove('Vegeta') #função para evitar erros em tempo de execução
nomes.sort() #outra maneira de ordenar se for do mesmo tipo
nomes.sort(reverse=True) #ordenando decrescente