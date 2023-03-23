numeros = input("Digite uma lista de números separados por vírgulas: ")

numeros = numeros.split(",")

soma_impares = 0 

for numero in numeros:
    numero = int(numero) 
    if numero % 2 != 0: 
        soma_impares += numero 

print("A soma dos números ímpares é:", soma_impares)
