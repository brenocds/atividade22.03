numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros.sort(reverse=True)

print("A lista ordenada em ordem decrescente é:")
for n in numeros:
    print(n)
