while True:
    sexo = input("qual seu sexo (M/F): ").strip().upper()
    if sexo == "M" or sexo == "F":
        break
    else:
        print("digite um sexo válido")