numeros = input("Digite uma lista de números separados por vírgulas: ")

numeros = numeros.split(",") 

numeros = [int(numero) for numero in numeros] 
numeros_ordenados = sorted(numeros, reverse=True) 

segundo_maior = None

for numero in numeros_ordenados:
    if numero < max(numeros_ordenados): 
        segundo_maior = numero 
        break 

if segundo_maior is not None: 
    print("O segundo número mais alto é:", segundo_maior)
else:
    print("Não há segundo número mais alto")
