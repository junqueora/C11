import numpy

linhas = int(input("Quantas linhas? "))
colunas = int(input("Quantas colunas? "))
lxc = linhas * colunas

mtz = numpy.zeros((linhas, colunas), dtype=int)
print(mtz)

if lxc % 2 == 0:
    print(f"Terá um número par ({lxc}) de elementos!")
else:
    print(f"Terá um número ímpar ({lxc}) de elementos!")

print(mtz.reshape(1, lxc))