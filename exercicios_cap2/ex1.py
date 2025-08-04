nome = input("Qual o seu nome?").strip()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))

partes_do_nome = nome.split()
partes_do_nome[-1] = "do Inatel"
print(" ".join(partes_do_nome))