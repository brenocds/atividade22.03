numeros = input("Digite uma lista de números separados por vírgulas: ")

numeros = numeros.split(",") 

numeros_sem_duplicatas = list(set(numeros)) 

for numero in numeros_sem_duplicatas:
    print(numero)
