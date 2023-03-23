a = []
palavra = input("Digite uma lista de palavras separando as com virgula e espaço: ")

for palavra in palavra.split(', '):
    if palavra[0] == "a" or palavra[0] == "A":
        a.append(palavra)

print('Palavras que começam com "a": ', a)