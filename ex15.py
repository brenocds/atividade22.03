numeros = input("Digite uma lista de números separados por espaço: ")

numeros = [int(num) for num in numeros.split()]

numeros_sem_duplicatas = list(set(numeros))

print("Nova lista sem números duplicados:", numeros_sem_duplicatas)
