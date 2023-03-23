numeros = input("Digite uma lista de números separados por vírgulas: ")

numeros = numeros.split(",") 

for numero in numeros:
    numero = int(numero) 
    if numero > 10:
        print(numero)
