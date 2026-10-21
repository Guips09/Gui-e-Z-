def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "vertical":
            lista.append([linha + i, coluna])
        elif orientacao == "horizontal":
            lista.append([linha, coluna + i])

    return lista

linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

print(define_posicoes(linha, coluna, orientacao, tamanho))
