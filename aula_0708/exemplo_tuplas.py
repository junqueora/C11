tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan') #usada como uma lista (fecha em ())
print(tupla) #print de toda a tupla
print(tupla[1]) #print de um elemento
#tupla[0] = 'Bulma' NÃO EXECUTA EM TEMPO DE COMPILAÇÃO, TUPLAS SÃO IMUTÁVEIS
print(tupla[1:4]) #print do elemento 1 até o 3 (n - 1)
#em python sempre vai ser intervalo a <= x < b
tupla2 = ('Goku', 20, 5.5, 'Gohan') #aceitam vários tipos
print(tupla[-1]) #indíce negativo na tupla retorna na ordem inversa
print(sorted(tupla)) #tuplas podem ser ordenadas com a função sorted
x = (2, 6 ,8)
y = (5, 6, 9, 1)
z = x + y
print(z) #operações entre tuplas gera uma tupla do conjunto união (porém duplica elementos iguais)
print(z.count(6)) #conta todas as ocorrências de um elemento
print(max(z), min(z)) #verifica maior e menor valor
print(z.index(5)) #retorna o index de um elemento se houver