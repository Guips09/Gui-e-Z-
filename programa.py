from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

quantidades = { 
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4
}

tamanhos = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1
}

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


for navio in frota:
    tamanho = tamanhos[navio]

    while len(frota[navio]) < quantidades[navio]:
        linha = int(input())
        coluna = int(input())

        if navio != "submarino":
            opcao = int(input())

            if opcao == 1:
                orientacao = "vertical"
            elif opcao == 2:
                orientacao = "horizontal"
            else:
                continue
        else:
            orientacao = "vertical"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(
                frota, navio, linha, coluna, orientacao, tamanho
            )

jogador = posiciona_frota(frota)
oponente = posiciona_frota(frota_oponente)

while afundados(frota_oponente, oponente) < 10:
    jogadal = int(input())
    jogadac = int(input())

    if 0 <= jogadal < 10 and 0 <= jogadac < 10:
        oponente = faz_jogada(oponente, jogadal, jogadac)

print("Parabéns! Você derrubou todos os navios do seu oponente!")