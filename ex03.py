numeros = input("Digite uma lista de números separados por vírgula: ").split(",")


maximo = numeros[0]
minimo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n

print("O maior número da lista é ", maximo)
print("O menor número mínimo da lista é ", minimo)