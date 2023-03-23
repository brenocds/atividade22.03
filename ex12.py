nomes = input("Digite uma lista de nomes separados por vírgulas: ")

nomes = nomes.split(",") 

nome_procurado = input("Digite o nome que você está procurando: ")

if nome_procurado in nomes: 
    print("O nome está na lista")
else:
    print("O nome não está na lista")
