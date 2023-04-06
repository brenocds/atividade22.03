numeros = input("Digite uma lista de números separados por espaço: ")

numeros = [int(num) for num in numeros.split()]

numeros_repetidos = []

for num in numeros:
    if numeros.count(num) > 1 and num not in numeros_repetidos:
        numeros_repetidos.append(num)

print("Lista de números que aparecem mais de uma vez:", numeros_repetidos)
