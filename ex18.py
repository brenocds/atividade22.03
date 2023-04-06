numeros = input("Digite uma lista de números separados por espaço: ")

numeros = list(map(int, numeros.split()))

divisiveis_por_3 = []

for numero in numeros:
    if numero % 3 == 0:
        divisiveis_por_3.append(numero)

print("Lista de números divisíveis por 3:", divisiveis_por_3)
