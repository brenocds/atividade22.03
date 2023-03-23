lista = []
numeros = input("Digite uma lista de numeros separados com virgula e espaço: ")

for numero in numeros.split(', '):
    if int(numero) % 2 == 0:
        lista.append(int(numero))

print("Numeros pares: ", lista)
