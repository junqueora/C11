import random
import numpy

campo = numpy.zeros((2, 2), dtype=int)
campo[random.randint(0, 1), random.randint(0, 1)] = 1

tentativas = 0

while True:
    linha = int(input("Escolha a linha (0 ou 1): "))
    coluna = int(input("Escolha a coluna (0 ou 1): "))

    tentativas += 1

    if campo[linha, coluna] == 1:
        print("Game Over! Faz o L!")
        break
    else:
        print("Posição limpa!")

        if tentativas >= 3:
            print("Congratulations! You beat the game! :)")
            break