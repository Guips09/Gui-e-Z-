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
    for navio in frota:
        for posicoes in frota[navio]:
            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro=[linha][coluna]
    return tabuleiro