numeros = input("Digite uma lista de números separados por vírgula: ").split(",")


numeros.sort()

print("A lista ordenada em ordem crescente é:")
for n in numeros:
    print(n)
