nomes = input("Digite uma lista de nomes separados por espaço: ")

nomes = nomes.split()

nomes_com_e = []

for nome in nomes:
    if "e" in nome:
        nomes_com_e.append(nome)

print("Lista de nomes que contêm a letra 'e':", nomes_com_e)
