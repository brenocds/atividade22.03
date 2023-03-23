nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

mais_longo = mais_curto = nomes[0]

for nome in nomes:
    if len(nome) > len(mais_longo):
        mais_longo = nome
    elif len(nome) < len(mais_curto):
        mais_curto = nome

print(f"O nome mais longo é: ", mais_longo, "e o nome mais curto é : ", mais_curto)
