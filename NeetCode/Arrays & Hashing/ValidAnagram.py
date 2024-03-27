def sao_anagramas(s, t):
    if len(s) != len(t):
        return False

    s_ordenado = sorted(s)
    t_ordenado = sorted(t)

    return s_ordenado == t_ordenado


print(sao_anagramas("anagrama", "nagarama"))
print(sao_anagramas("rato", "carro"))
