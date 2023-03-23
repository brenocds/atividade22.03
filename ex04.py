numeros = input("Digite uma lista de números separados por vírgula: ").split(",")
numeros = [float(n) for n in numeros]

media = sum(numeros) / len(numeros)

print(f"A média dos números na lista é {media:.2f}")
