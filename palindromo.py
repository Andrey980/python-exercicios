def verificar_palin(palavra):
    return palavra == palavra[::-1]


palin = input("Digite a palavra: ")

if verificar_palin(palin):
    print("É um palindromo")

else:
    print("Não é um palindromo")
