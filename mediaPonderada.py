def calcular_media_ponderada(notas, pesos):
    if len(notas) != len(pesos):
        return "O número de notas deve ser igual ao número de pesos."

    soma_produtos = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)

    if soma_pesos == 0:
        return "A soma dos pesos não pode ser zero."

    return soma_produtos / soma_pesos


notas = [float(x)
         for x in input("Digite as notas separadas por espaço: ").split()]
pesos = [float(x) for x in input(
    "Digite os pesos correspondentes separados por espaço: ").split()]

media_ponderada = calcular_media_ponderada(notas, pesos)

print("A média ponderada é:", media_ponderada)
