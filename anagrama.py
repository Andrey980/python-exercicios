def sao_anagramas(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False

    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()

    palavra1_ordenada = ''.join(sorted(palavra1))
    palavra2_ordenada = ''.join(sorted(palavra2))

    if palavra1_ordenada == palavra2_ordenada:
        return True
    else:
        return False


palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sao_anagramas(palavra1, palavra2):
    print("As palavras", palavra1, "e", palavra2, "são anagramas.")
else:
    print("As palavras", palavra1, "e", palavra2, "não são anagramas.")
