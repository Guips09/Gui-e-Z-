def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "vertical":
            lista.append([linha + i, coluna])
        elif orientacao == "horizontal":
            lista.append([linha, coluna + i])

    return lista
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in frota:
        frota[nome_navio] = []
    lista= define_posicoes(linha, coluna, orientacao, tamanho)
    frota[nome_navio].append(lista)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    total = 0

    for tipo in frota:
        for navio in frota[tipo]:
            acertos = 0

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] == 'X':
                    acertos += 1

            if acertos == len(navio):
                total += 1

    return total